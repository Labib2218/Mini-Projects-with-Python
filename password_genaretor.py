import random
import string

sign_list = '!@#$%&*_-/<>?'
p_lenth = int(input("Enter the length of your password: "))
def password():
    new_pass = ''.join(random.choice(string.ascii_letters + string.digits+sign_list) for i in range(p_lenth))
    return new_pass
final_pass =password()
print(f"Your Genareted Password is: {final_pass}")
