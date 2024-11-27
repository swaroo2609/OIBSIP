import random
alphabets='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
symbols='!','@','#','$','%','^','&','*','(',')','_','}','{',']','['
numbers='0','1','2','3','4','5','6','7','8','9'
print("Welcome to Password Generator!")
n=int(input("Enter the length for the password :"))
if(n<=8 and n>=0):
      
   letters=int(input("How many letters (both upper & lower) do you want in your password ?"))
   specialcharacter=int(input("How many Special characters do you need in your password ?"))
   digits=int(input("How many digits do you want in your password ?"))
   password=""
   for i in range(1,letters+1):
       temp = random.choice(alphabets)
       password += temp

   for i in range(1,specialcharacter+1):
       temp = random.choice(symbols)
       password +=temp

   for i in  range(1,digits+1):
       temp=random.choice(numbers)
       password +=temp

   print(password)

else:
    print("invalid password length!")