class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display_info(self):
        print("User Information:")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Password:", self.password)

users = [] # User database
def user_registration():

        # Get user input
        name = input("Enter your name: ")
        email = input("Enter your email address: ")
        password = input("Enter your password: ")

        # Check if email already exists
        for user in users:
            if user.email == email:
                print("Email already exists. Please choose a different email.")
                return

        # Create a new user
        new_user = User(name, email, password)
        users.append(new_user)

        print("Registration successful!")
        new_user.display_info()


    # Test the user registration
if __name__== "__main__":  
 user_registration()