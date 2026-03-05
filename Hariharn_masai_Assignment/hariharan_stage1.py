def calculator(a,b,choose):
    match choose:
        case 1:
            sum = a + b
            print(sum)
        case 2:
            sub = a - b
            print(sub)
        case 3:
            mul = a * b
            print(mul)
        case 4:
            div = a / b
            print(div) 
calculator(10,5,1)                    