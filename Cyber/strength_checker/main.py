import re
def check_password_strength(password):
    score = 0
    errors = []
    length = len(password)
    if length <=5:
        print("Password should consist atleast 6 digits")
        return "Password too short"
    else:
        if re.search(r"[A-Z]", password):
            score += 1
        else: errors.append("Password should contain uppercase values")
        if re.search(r"[a-z]", password):
         score +=1
        else: errors.append("Password should contain lowercase values")
        if re.search(r"\d", password):
            score +=1
        else: errors.append("Password should contain numbers")
        if re.search(r"[^a-zA-Z0-9]", password):
            score+=1
        else: errors.append("Password should contain special characters")
    
    if score==4:
        strength = "Strong"
    elif score>=3:
        strength = "Medium"
    else:
        strength = "Weak"
    return strength, errors

# password = input("Enter password: ")
# strength, errors = check_password_strength(password)
# print(strength)
# if errors: 
#     print("Suggestions: ")
#     for i in errors:
#         print("-", i)
