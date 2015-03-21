def is_triangle(a,b,c):
    if a < b + c or b < a + c or c < b + a:
        return True
    else:
        return False
    

def area(a,b,c):
    p = (a + b + c) // 2
    area = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return area

def is_pythagorean(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

def max_area(triangles):
    first_sideA = triangles[0][0]
    first_sideB = triangles[0][1]
    first_sideC = triangles[0][2]
    max = area(first_sideA,first_sideB,first_sideC)
    for triangle in triangles:
        if max < area(triangle[0],triangle[1],triangle[2]):
            max = area(triangle[0],triangle[1],triangle[2])
    return max
    
