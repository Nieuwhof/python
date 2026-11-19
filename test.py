
# blokked email
blocked_email = ["koos@outlook.nl", "bep@gmail.com", "piet@pm.me"]
emails = ["test@gmail.com","koos@gmail.com","piet@gmail.com","bep@gmail.com"]

for email in emails:
    if email in blocked_email:
        print(f' {email} is blocked')
    else:
        print(f' {email} is not blocked')
