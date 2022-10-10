largest = None
smallest = None
numeros = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue    
    numeros.append(n)

for x in numeros:  
    if smallest is None:
        smallest = x   
    elif x < smallest:
        smallest = x
    
    if largest is None:
        largest = x   
    elif x > largest:
        largest = x
        
print("Maximum is", largest)
print("Minimum is", smallest)

############################################################################################################

score = input("Enter Score:")

try:
    s = float(score)
except:
    print("Error, ingrese un número")
    
if s<=1.0 and s>= 0.0:
    if s>= 0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>= 0.7:
        print("C")
    elif s>=0.6:
        print("D")
    else:
        print("F")
elif s>1.0 or s<0.0:
    print("Fuera de rango")

############################################################################################################
