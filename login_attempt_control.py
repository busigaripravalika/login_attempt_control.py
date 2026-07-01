import time

# Correct credentials
USERNAME = "admin"
PASSWORD = "password123"

MAX_ATTEMPTS = 3
LOCK_TIME = 30  # seconds

attempts = 0

print("===== Login Attempt Control System =====")

while True:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!")
        break
    else:
        attempts += 1
        remaining = MAX_ATTEMPTS - attempts

        if remaining > 0:
            print(f"\nIncorrect credentials!")
            print(f"Attempts remaining: {remaining}\n")
        else:
            print("\nToo many failed attempts!")
            print(f"Account locked for {LOCK_TIME} seconds...\n")
            time.sleep(LOCK_TIME)
            attempts = 0
            print("You can try logging in again.\n")