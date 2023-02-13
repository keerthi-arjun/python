def check_password(username, password):
    if username == "admin" and password == "1234":
        return True
    return False
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    retyped_password = input("Re-type your password: ")
    if password != retyped_password:
        print("The passwords do not match.")
        return
    attempts = 0
    while not check_password(username, password) and attempts < 3:
        print("Incorrect password.")
        password = input("Enter your password again: ")
        attempts += 1
    if attempts == 3:
        print("Too many attempts. Access denied.")
    else:
        print("Access granted.")

login()
