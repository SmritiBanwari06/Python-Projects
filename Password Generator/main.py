import string
import random

if __name__ == "__main__":

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.punctuation
    s4 = string.digits
    # print(s1)
    # print(s2)
    # print(s3)
    # print(s4)
    plen = int(input("Enter the length of your password: "))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)
    random.shuffle(s)
    print("Your password is","".join(s[0:plen]))