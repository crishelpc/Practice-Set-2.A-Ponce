
def calculate_triangle( a: float, b: float, c: float):
     ''''
    Calculates the area of a triangle given three sides.

    Args: 
        sp = semi-perimeter 
         a = the length of side a 
        b = the length of side b 
        c = the length of side c 

    Return 
        The calculated area of triangle
    '''
     perimeter = (a + b + c)
     sp = perimeter / 2
     area = (sp*(sp - a)*(sp - b)*(sp-c))**0.5
     return area

SideA = float(input("Enter the length of side A: "))
SideB = float(input("Enter the legth of side B: "))
SideC = float(input("Enter the legth of side C: "))

area = calculate_triangle(SideA, SideB, SideC)

print("Area of the  triangle is: "+ str(area))