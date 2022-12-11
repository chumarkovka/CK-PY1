import string
import random
def get_random_password() -> str:
    leng = string.digits + string.ascii_letters
    passw = "".join(random.sample(leng,8))
    return passw

print(get_random_password())
