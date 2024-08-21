Final_Vel = float(input("Enter the final veleocity of the car: "))
Initial_Vel = float(input("Enter the initial veleocity of the car: "))
acceleration = float(input("Enter the acceleration of the car: "))


dispacement = (Final_Vel**2-Initial_Vel**2)/(2*acceleration)
print("The displacement of the car is: " +  str(dispacement))
