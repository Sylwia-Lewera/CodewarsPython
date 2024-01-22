"""
Your job is to find the gravitational force between two spherical objects (obj1 , obj2).

input
Two arrays are given :

arr_val (value array), consists of 3 elements
1st element : mass of obj 1
2nd element : mass of obj 2
3rd element : distance between their centers
arr_unit (unit array), consists of 3 elements
1st element : unit for mass of obj 1
2nd element : unit for mass of obj 2
3rd element : unit for distance between their centers
mass units are :

kilogram (kg), gram (g), milligram (mg), microgram (μg), pound (lb)

distance units are :

meter (m), centimeter (cm), millimeter (mm), micrometer (μm), feet (ft)

Note:
value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)
"""

def solution(arr_val, arr_unit):
  
  try:
    
    G = 6.67 * (10 ** -11)
    F = G * arr_val[0] * arr_val[1] / (arr_val[2] ** 2)
    for i in range(2):  
        if arr_unit[i] == "g": F = F / 10 ** 3
        if arr_unit[i] == "mg": F = F / 10 ** 6
        if arr_unit[i] == "μg": F = F / 10 ** 9
        if arr_unit[i] == "μg": F = F * 0.45359237 
        if arr_unit[2] == "cm": F = F / 10 ** 2
        if arr_unit[2] == "mm": F = F / 10 ** 3
        if arr_unit[2] == "μm": F = F / 10 ** 6
        if arr_unit[2] == "ft": F = F * 0.3048
    return F
  except TypeError:
    pass


print(solution([1000, 1000, 100], ["kg", "kg", "cm"])) #, 0.0000667