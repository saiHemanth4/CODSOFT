import string
import random
print("..................PASSWORD GENERATOR........................")
print("""Note:for 'STRONG PASSWORD' you should enter four categories 
        i.e.,lowercase,uppercase,numbers,special symbols\n""")
c=1
while(True):
    if c==1:
        len=int(input("A.enter the how many digits you require:"))
        lower_len=int(input("1.enter the how many lower digits you require:"))
        if lower_len==0:
            a=input("lower case digit are missing ......are you sure you did not want any lower case for password generation (yes/no)")
            if a=="NO" or a=="no":
               lower_len=int(input("1.enter the how many lower digits you require:")) 
        upper_len=int(input("2.enter the how many  upper digits you require:"))
                
        if upper_len==0:
            a=input("upper case digit are missing ......are you sure you did not want any lower case for password generation (yes/no)")
            if a=="NO" or a=="no":
               upper_len=int(input("1.enter the how many lower digits you require:")) 
        number_len=int(input("3.enter the how many numbers you require:"))
        if number_len==0:
            a=input("numbers are missing ......are you sure you did not want any lower case for password generation (yes/no)")
            if a=="NO" or a=="no":
               number_len=int(input("1.enter the how many lower digits you require:")) 
        symbols_len=int(input("4.enter the how many special symbols you require:"))
        if symbols_len==0:
            a=input("special symbols are missing ......are you sure you did not want any lower case for password generation (yes/no)")
            if a=="NO" or a=="no":
               symbols_len=int(input("1.enter the how many lower digits you require:")) 
        password_len=lower_len+upper_len+number_len+symbols_len
        if len==password_len:
            lower=string.ascii_lowercase
            upper=string.ascii_uppercase
            digit=string.digits
            symbol=string.punctuation
            randompassword=random.choices(lower,k=lower_len)+random.choices(upper,k=upper_len)+random.choices(digit,k=number_len)+random.choices(symbol,k=symbols_len)
            password="".join(randompassword)
            print(password)
            break
        else:
            print("""The  no.of digits required for a password is more/less 
                                 ................. so the password is invalid password so please try again\n""")
            c=1
            
            
    else:
        break