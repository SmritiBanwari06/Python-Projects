SECURE =(('s','$'),('i','!'),('a','@'),('o','0'),('I','|'),('x','*'))

def securePswd(password):
    for a,b in SECURE:
        password  = password.replace(a,b)
    return password

if __name__=='__main__':
    password = input("ENTER YOUR PASSWORD: ")
    password = securePswd(password)
    print(f"Your secured password is {password}")
