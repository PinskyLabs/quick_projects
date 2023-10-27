'''

Today, we will try to find the approx value for W(x) by using the Newton's Method

'''
# Importing math module for e
import math

### INTRO
print("Welcome to the Lambert function or W(x) calculator!\n")

print("Please put a decimal value only...\n")

funcn = input("You must have W(x) where x = ")
print("Now, your function for calculating is f(x)= xe^x - " + funcn + "\n")

### METHOD
print("\nSo, by using Newton's method,")
print("By using this formula, Xn+1 = Xn - (f(x)/f'(x))")
i=1
x=1
# print("Value of X" + str(i) + " is 1")
while i < 6:
    fx = x*(math.exp(x)) - float(funcn) # The original function
    # print("fx is " + str(round(fx, 4)))
    fdashx = (x+1)*(math.exp(x)) # The derivative to of the original function
    # print("f'x is " + str(round(fdashx, 4)))
    i=i+1 
    x=x-((fx)/(fdashx)) # <== This is the Newton's formula we used to calculate W(x)
    # print("Value of X" + str(i) + " is " + str(x))

# print("After this all the values converge to X6....")

### FINAL ANSWER
print("The final answer, \033[1mW(" + str(funcn) + ") is " + str(x) + "\033[0m")
# This is the final answer to W(x) which is approx because after this, all the values converge to this value(X6).
# To BOLD ==> \033[1m______\033[0m

### CREDITS
print("\n\n\n***\nThis program is created by\033[1m Pinak Parate\033[0m.\nIf you are using it for your purpose, feel free.If there is any mistake in this please lemme know!\n***")