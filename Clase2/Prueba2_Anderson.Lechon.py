n=100

frase3="Fizz"
frase5="Buzz"
frase35="FizzBuzz"

for i in range(1,n+1):
    if(i%5==0 and i%3==0):
            print(str(i)+" "+frase35) 
    else:  
        if(i%3==0):
            print(str(i)+" "+frase3)
        if(i%5==0):
            print(str(i)+" "+frase5)
  