'''
Author: Jahar Persad

Date: 5 September 2025

Intended function: Just test scripts to learn how to manage git

Version1: Functional, ready to commit to main branch, version 2 should include subtraction.'''

def calculator():

    title =  str("This is a additive calculator, please enter what you would like to add\n type done when you would like the result")
    
    print(title)

    value = input("What would you like to add ? ")
    value_total = 0

    while str(value) != "done":

        value_total = value_total + float(value)
        value = input("What would you like to add ? ")


    print("Your result is = ", value_total)

def run():
    calculator()

if __name__ == "__main__":
    run()