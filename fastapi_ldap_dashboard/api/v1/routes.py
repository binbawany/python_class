from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..auth import create_access_token, verify_token
from ..monitor import get_system_metrics
from ldap3 import Server, Connection, ALL, NTLM

router = APIRouter(prefix="/api/v1")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login")

LDAP_SERVER = "ldap://your-ldap-server"
LDAP_DOMAIN = "YOURDOMAIN"

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    ldap_user = f"{LDAP_DOMAIN}\\{username}"

    server = Server(LDAP_SERVER, get_info=ALL)
    try:
        conn = Connection(server, user=ldap_user, password=password, authentication=NTLM, auto_bind=True)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid LDAP credentials")

    role = "admin" if username in ["adminuser"] else "user"
    token = create_access_token({"sub": username, "role": role})
    return {"access_token": token, "token_type": "bearer"}


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload


@router.get("/profile")
def profile(user: dict = Depends(get_current_user)):
    return {"username": user["sub"], "role": user["role"]}


@router.get("/monitor")
def monitor(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return get_system_metrics()
