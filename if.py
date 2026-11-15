
country = "Canada"

match country:
    case "USA":
        print("United States of America")
    case "Canada":
        print("Canada") 
    case "Mexico":
        print("Mexico")
    case _:
        print("Unknown country")    


score = 100
Cert = True

if score >= 90 and Cert:
    print("A+")
    if score >= 100:
        print("certified")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")



age = 25

match age:
     case x if x < 18:
         print("You are a minor.")
     case x if x >= 18 and x < 65:
        print("You are an adult.")
     case x if x >= 65:
        print("You are a senior citizen.")



