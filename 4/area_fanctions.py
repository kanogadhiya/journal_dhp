def area_circle():
    r=float(input("Enter Radius in cm :"))
    ar_circle=round((22/7)*r*r,2)
    return ar_circle

def area_triangle():
    b=float(input("Enter Base in cm :"))
    h=float(input("Enter Height in cm :"))
    ar_triangle=round(0.5*b*h,2)
    return ar_triangle

def area_square():
    s=float(input("Enter side of square in cm :"))
    ar_square=round(s*s,2)
    return ar_square

