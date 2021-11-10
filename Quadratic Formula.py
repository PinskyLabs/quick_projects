
print("\nYour quadratic equation should be in this form: ax^2 + bx + c = 0\n")

print("NOTE: This program will give you an error if your equation's roots are imaginary/complex\n")

coeff_a = int(input("Enter 'a' from your equation: "))
coeff_b = int(input("Enter 'b' from your equation: "))
coeff_c = int(input("Enter 'c' from your equation: "))

def formula():
    ans1 = int(((1)*(coeff_b) + ((coeff_b)**2 - 4*(coeff_a)*(coeff_c))**0.5)/2*coeff_a)
    ans2 = int(((1)*(coeff_b) - ((coeff_b)**2 - 4*(coeff_a)*(coeff_c))**0.5)/2*coeff_a)
    if ans1 == ans2:
        print("\nRoots of your equation are same i.e. ", str(ans1), ",", str(ans2), sep=" ")
    elif ans1 or ans2 == complex:
        print("\nOne of the roots are imaginary, not real.")
    else:
        print("\nRoots of your equation are same i.e. ", str(ans1), str(ans2), sep=" ")
        
formula()
