import random
import string
def generate_password(length):
    lalpha = string.ascii_lowercase
    ualpha = string.ascii_uppercase
    char = "@#$%^&*/?"
    num = string.digits
    if length is None: 
        length = random.randint(8,10)
    dig = lalpha + ualpha + char + num
    digcompl = [random.choice(char), random.choice(lalpha), random.choice(ualpha), random.choice(num)]
    ranlen = length - 4
    bpass = [random.choice(dig) for i in range(ranlen)]
    apass = digcompl + bpass
    random.shuffle(apass)
    password = ''.join(apass)
    return password
