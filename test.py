'''
Author: Jahar Persad

Date: 5 September 2025

Intended function: Just test scripts to learn how to manage git

Version1: Functional, ready to commit to main branch, version 2 should include subtraction.

Version2: includes subtraction - no version change in the name'''

def calculator():

    title =  str("This is a addition/subtraction calculator, please enter what you would like to add/subtract\n type done when you would like the result")
    
    print(title)

    function = input("Add of Subtract (A/S) ?")
    if str(function) == "A" or str(function) == "a":
     value = input("What would you like to add ? ")
     value_total = 0

     while str(value) != "done":

         value_total = value_total + float(value)
         value = input("What would you like to add ? ")


     print("Your result is = ", value_total)
    
    elif str(function) == "S" or str(function) == "s":
     first_value = input("What is the value you want to subtract from ? ")
     value = input("What would you like to subtract ? ")
     value_total = float(first_value)

     while str(value) != "done":

         value_total = value_total - float(value)
         value = input("What would you like to subtract ? ")


     print("Your result is = ", value_total)

def run():
    calculator()

if __name__ == "__main__":
    run()