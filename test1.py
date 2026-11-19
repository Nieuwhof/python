line =" Email must not be empty"    
line =" Email must not special caractores"
line =" Email must have @ and . "
line = "Email must contain .com .net .org"
line = "Email must not be longer than 256 characters"
line = "Email must not contain spaces"

email = "bep@  gmail.c   o  m".replace(" ","")

#Email must not be empty"

if email == "":
    print("Email must not be empty")
    #  Email must not special caractores"
elif not email[0].isalnum() and email[-1].isalnum():
    print("Email must not special caractores")
    # Email must have @ and . "
elif "@" not in email or "." not in email:
    print("Email must have @ and . ")
    # Email must contain .com .net .org"
elif not email.endswith(".com") or email.endswith(".net") or email.endswith(".org"):
    print("Email must contain .com .net .org")
    # Email must not be longer than 256 characters"
elif len(email) > 256:
    print("Email must not be longer than 256 characters")
else:
    print(email + " Email valid")
