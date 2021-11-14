## app  <------ two integers    <---- user  
##      <----- chiose operation <---- user  
##      <----- display resolts  ----> user  
## ---------------------------------------------------------

def input_integer(which) :           # = "first"
    print("Enter ", which, "integer: ", end = "")
    return int(input())

a = input_integer ("first")
b = input_integer ("second")

op = input("Chiose operation (*, /, +, -, **): ")   ## op = "+"
resolt = 0
## HW1. next operations : /, -, **, 
# if the user chiose inexisten operation --- print "WRONG operation" 
if op == "+":
    resolt = a+b
elif op == "-":
    resolt = a-b
elif op == "/":
    resolt = a/b
elif op == "*":
    resolt = a*b
elif op == "**":
    resolt = a**b
else: 
    print (op, "is a Wrong operation -------- Try again")  
print("Resolt: a", op, "b = ", resolt)

##______________________________________________________________________________
"""

def input_integer(which) :           # = "first"
    print("Enter ", which, "integer: ", end = "")
    return int(input())

a = input_integer ("first")
b = input_integer ("second")

op = input("Chiose operation (*, /, +, -, **): ")   ## op = "+"
resolt = 0
## HW1. next operations : /, -, **, 
# if the user chiose inexisten operation --- print "WRONG operation" 
if op == "+":
    resolt = a+b
if op == "-":
    resolt = a-b
if op == "/":
    resolt = a/b
if op == "*":
    resolt = a*b
if op == "**":
    resolt = a**b
else: 
    print (op, "is a Wrong operation -------- Try again")  
print("Resolt: a", op, "b = ", resolt)
"""