import bcrypt
from datetime import datetime


def hashPassword(password: str) -> str:
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.decode("utf-8")
    except Exception as e:  # Catch any other general exceptions
        print(f"{datetime.now()}, Error Occured:{e}")
        raise Exception(f"An unexpected error occurred: {str(e)}")


def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
    # Hash the plain password
    hashedInput = hashPassword(plainPassword)

    # Compare the hashed password with the stored hashed password
    if hashedInput == hashedPassword:
        print("Password matched")
        return True
    else:
        print("Password did not match")
        return False
