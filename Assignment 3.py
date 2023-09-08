class Stack:
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

    def isEmpty(self):
      if self.elements == 0:
        return True
      else:
        return

def is_palindrome():
    user_input = input("Enter a sentence: ").lower() #This serves to convert all the characters to lower case 
    #reference: https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/
    user_input = "".join(user_input.split()) #This serves to remove all spaces in the sentence
    s = Stack() # initialize an empty stack

    for ch in user_input:
        s.push(ch) # append the sentence character by character

    reversed_str = "" # empty string to store the poped characters
    while len(s.elements) > 0: #check that the stack is not empty 
        reversed_str += s.pop() # store all characters poped in reversed_str
    if user_input == reversed_str: #condition to check is sentence is a palindrome
        print("The input is a palindrome.")
    else:
        print("The input is not a palindrome.")

# is_palindrome()

class Car:
   def __init__(self,make,color,plate_number):
     self.make = make
     self.color = color
     self.plate_number = plate_number
class Queue:
  def __init__(self):
    self.elements= []

  def enqueue(self,car):
    self.elements.append(car)

  def dequeue(self):
    if  not self.isEmpty():
      self.elements.pop(0)
    else:
      return None

  def size(self):
    return len(self.elements)
  
  def isEmpty(self):
    if self.elements == 0:
      return True
    else:
      return

  def front(self):
    if not self.isEmpty():
      return self.elements[0]
    else:
      return None

def car_wash_menu():
  car_wash=Queue()
  choice=None 
  while choice!=3:
    print("Enter:")
    print("1. insert a car to the queue")
    print("2. remove the car from the queue")
    print("3. exit")
    choice=int(input())
    if choice == 1:
      make = input("Enter car make: ")
      color = input("Enter car color: ")
      plate_number = int(input("Enter car plate number: "))
      current_car = Car(make, color, plate_number)
      car_wash.enqueue(current_car)
      print("The current car is: ", current_car.make, "Its color is: ", current_car.color,"Its plate number is:", current_car.plate_number)
    elif choice == 2:
      if not car_wash.isEmpty():
        removed_car=car_wash.dequeue()
        done_car = Car(make, color, plate_number)
        print("This car", removed_car, "make",done_car.make,"color", done_car.color,"plate number",done_car.plate_number,"is finished")
      else:
        print("The queue is empty. No cars to remove.")
    elif choice == 3:
      break
    else:
      print("Invalid choice. Please enter a valid option")

# car_wash_menu()

def decode_message():
  user_input = input("Enter your message: ")
  s = Stack()
  decoded_message = []
  for ch in user_input:
    #reference:https://www.entechin.com/python-check-if-character-is-letter-in-string/?expand_article=1
    if ch.isalpha() or ch.isspace():
      s.push(ch)
    elif ch == "*":
      decoded_message.append(s.pop())
  while not s.isEmpty():
    decoded_message.append(s.pop())
  
  return ''.join(decoded_message)    
  print(decode_message)

# decode_message()

    
