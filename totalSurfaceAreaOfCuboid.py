length = float(input("Enter the length of the cuboid: "))
breadth = float(input("Enter the breadth of the cuboid: "))
height = float(input("enter the height of the cuboid: "))

totalSurfaceArea = 2*((length*breadth) + (length*height) + (breadth*height))
print("The total surface area of the cuboid is: " + str(totalSurfaceArea))