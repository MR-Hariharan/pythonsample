def calculator(a,b,choose):
    match choose:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case 4:
            return a / b
print(calculator(10,5,1))  
if calculator(10,5,1) > 1:
    print("Positive") 
elif calculator(10,5,1) == 0:
    print("Zero")  
else:
    print("Negative")          
               