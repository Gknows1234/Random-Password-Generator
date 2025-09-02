import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    
    all_chars = lowercase + uppercase + digits + special
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    print("-" * 20)
    
    while True:
        print("\n1. Generate password")
        print("2. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            length = input("Password length (press enter for 12): ")
            if length:
                length = int(length)
            else:
                length = 12
            
            password = generate_password(length)
            print(f"Your password: {password}")
        
        elif choice == "2":
            print("Bye")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
