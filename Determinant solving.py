print("Please enter the values in the correct format\n\nThe format is: ")

print("|  a1  a2  a3  |")
print("|  b1  b2  b3  |")
print("|  c1  c2  c3  |")

a1 = input("\nEnter value for a1: ")
a2 = input("Enter value for a2: ")
a3 = input("Enter value for a3: ")

b1 = input("\nEnter value for b1: ")
b2 = input("Enter value for b2: ")
b3 = input("Enter value for b3: ")

c1 = input("\nEnter value for c1: ")
c2 = input("Enter value for c2: ")
c3 = input("Enter value for c3: ")

def solving_3x3():
    bc1 = (int(b2)*int(c3)) - (int(c2)*int(b3))
    bc2 = (int(b1)*int(c3)) - (int(c1)*int(b3))
    bc3 = (int(b1)*int(c2)) - (int(c1)*int(b2))
    answer = (int(a1)*int(bc1)) - (int(a2)*int(bc2)) + (int(a3)*int(bc3))
    final_answer = str(answer)
    print("\nYour determinant answer is: " + final_answer)

solving_3x3()



