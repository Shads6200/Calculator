def add(n1,n2):
  return n1 + n2
def subtract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
next = True 
import art
print(art.logo)
while next is True: 
  num1= int(input("What is the first number?: " ))
  for operation in operations:
    print(operation) 
  ki = input("Which of the above operation would you like to perform?: ")
  num2= int(input("What is the second number?: " ))
  
  calc_fun = operations[ki]
  result=calc_fun(num1,num2)
  print(result)
  print(f"{num1} {ki} {num2} = {result}")
  again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
  if again == "n":
     next = False
     print ("Goodbye!")
  else:
    while again =="y":
      ki = input("What is your next operation?: ")
      num3= int(input("What is the next number?: " ))
      calc_fun = operations[ki]
      result=calc_fun(num1,num2)
      print(f"{result} {ki} {num3} = {result}")
      again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
