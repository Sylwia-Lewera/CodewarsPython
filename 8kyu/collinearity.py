"""
You are given two vectors starting from the origin (x=0, y=0) with coordinates (x1,y1) and (x2,y2). Your task is to find out if these vectors are collinear. 
Collinear vectors are vectors that lie on the same straight line. They can be directed in the same or opposite directions. 
One vector can be obtained from another by multiplying it by a certain number. 
In terms of coordinates, vectors (x1, y1) and (x2, y2) are collinear if (x1, y1) = (kx2, ky2) , where k is any number acting as a coefficient.

Write the function collinearity(x1, y1, x2, y2), which returns a Boolean type depending on whether the vectors are collinear or not.

Notes:
All vectors start from the origin (x=0, y=0).
Be careful when handling cases where x1, x2, y1, or y2 are zero to avoid division by zero errors.
A vector with coordinates (0, 0) is collinear to all vectors.
"""

def collinearity(x1, y1, x2, y2):
    try:
        if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or ((x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0)):
            return True        
        else:
            return x1 / x2 == y1 / y2 
    except ZeroDivisionError:
        return False
    
"""
 if (x1, y1) = (kx2, ky2) => x1 * y2 == x2 * y1
"""