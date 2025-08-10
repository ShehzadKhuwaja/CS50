import validators

print("Valid" if validators.email(input("What's your email address? ")) else "Invalid")
