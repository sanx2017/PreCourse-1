""" This module implements a Stack data-structure using an array"""
class myStack:
  
  # Time Complexity: 
  # Space Complexity: 
     def __init__(self):
       self.stack_list=[]     # initialize the stack
       self.max_length = 100  # max size of stack allowed
         
     def isEmpty(self):
       if len(self.stack_list) == 0:
         return True
         
     def push(self, element):
       if len(self.stack_list) < self.max_length:
         self.stack_list.append(element)
         print ( f"Element {element} added")
       else:
         print ("Error: Stack overflow")
         
     def pop(self):
       if len(self.stack_list) == 0:
         print("Error: Stack underflow")
         return 0
       else:
         return self.stack_list.pop(-1)

     def peek(self):
       if len(self.stack_list) == 0:
         print("Stack is empty")
       else:
         return self.stack_list[-1]
        
     def size(self):
       return len(self.stack_list)
         
     def show(self):
       return self.stack_list

s = myStack()  # initialize a stack object
s.push('1')
s.push('2')
s.push('20')
s.push('30')
print(f"Peeking...{s.peek()}")
s.push('40')
print(s.pop() + " popped from the stack")
print(s.show())
s.size()

# Test for Stack Underflow
# It should print the error message
for i in range(len(s.stack_list) + 1):
  print (f"{s.pop()} popped from stack")
  
# Test for Stack Overflow.
# Add 100 elements. 
# It should print an error message at the end
for i in range(s.max_length+1):
  s.push(i)


  
