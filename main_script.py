#function
def muh_func():
    print("This is main function")


#check if this is main function
if __name__ == "__main__":  #by default built-in function that use for checking 
    print("running main_script directly")
    muh_func()
else:
    print("main_script has been imported")
