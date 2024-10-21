#SOPs
city  = ["Karachi", "Islamabad", "Sargodha", "Bahawalpur", "Lahore", "peshawar", "Quetta"]

age = 18

gender = "Male" 

#user input
userCity = "Lahore"

userage = 31

usergender = "female"

print("you are eligible to make NIC" if userCity in city and userage >= age or usergender == gender else "you are not eligible")

