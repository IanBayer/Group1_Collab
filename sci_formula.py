import os
import platform
import time


def head():
    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    print("░▓░▓░▓░▓░▓                 Group #1 & Group #2 Collab                   ░▓░▓░▓░▓░▓")
    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓\n")

def aarea():
    print("\t\t============================================")
    print("\t\t||             Area Calculator            ||")
    print("\t\t============================================")

def vvolume():
    print("\t\t============================================")
    print("\t\t||            Volume Calculator           ||")
    print("\t\t============================================")

def clean():
    if platform.system() == "Windows":
        os.system("cls")
        os.system("MODE CON: COLS=82 LINES=17")
    else:
        os.system("clear")

def AoV(): #fuction to choose which measurement
    global shape
    print("\t\t============================================")
    print("\t\t||         Area & Volume Calculator       ||")
    print("\t\t============================================")
    print("\n\t\t[A] Cylinder [B] Cube [C] Prism\n")
    shape = str(input("Choose shape to measure: "))
    clean()

def calc():
    if shape == "A" or shape == "a":
        head()
        print("\n\t\t[1] Area [2] Volume")
        formula = int(input("\nChoose parameter to compute: "))
        clean()
        if formula == 1:
            head()
            aarea()
            radius = float(input("\nPlease key in radius (m): "))
            heightc = float(input("Please key in height (m): "))
            areacy = (2 * 3.1416 * radius * heightc) + (2 * 3.1416 * radius * radius)
            print("\nThe area of cylinder is {} sq.m.".format(areacy))
        if formula == 2:
            head()
            vvolume()
            radius = float(input("\nPlease key in radius (m): "))
            height = float(input("Please key in height (m): "))
            volumecy = 3.1416 * radius * radius * height
            print("\nThe volume of cylinder is {} cu.m.".format(volumecy))
    if shape == "B" or shape == "b":
        head()
        print("\n\t\t[1] Area [2] Volume\n")
        formula = int(input("Choose parameter to compute: "))
        clean()
        if formula == 1:
            head()
            aarea()
            side = float(input("\nPlease key in side (m): "))
            areacb = 6 * side * side
            print("\nThe area of cube is {} sq.m.".format(areacb))
        if formula == 2:
            head()
            vvolume()
            side = float(input("\nPlease key in side (m): "))
            volumecb = side * side * side
            print("\nThe volume of cube is {} cu.m.".format(volumecb))
    if shape == "C" or shape == "c":
        head()
        print("\n[1] Area [2] Volume\n")
        formula = int(input("Choose parameter to compute: "))
        clean()
        if formula == 1:
            head()
            aarea()
            base = float(input("\nPlease key in base (m): "))
            heightp = float(input("Please key in height (m): "))
            lengthp = float(input("Please key in length (m): "))
            sidep = float(input("Please key in side (m): "))
            areap = base * heightp + 2*lengthp*sidep
            print("\nThe area of prism is {} sq.m.".format(areap))
        if formula == 2:
            head()
            vvolume()
            lengthp = float(input("\nPlease key in length (m): "))
            width = float(input("Please key in width (m): "))
            heightp = float(input("Please key in height (m): "))
            volumep = lengthp * width * heightp
            print("\nThe volume of cube is {} cu.m.".format(volumep))

        if shape == "D" or shape == "d":
        head()
        print("\n[1] Area [2] Volume\n")
        formula = int(input("Choose parameter to compute: "))
        clean()
        if formula == 1:
            head()
            aarea()
            PI = 3.14
            radius = float(input("Please key in radius (cm): "))
            areap = radius**3 * 4/3 * PI
            print("\nThe Surface area of sphere is {} cm2.".format(areap))
        if formula == 2:
            head()
            vvolume()
            PI = 3.14
            radius = float(input("Please key in radius (cm): "))
            heightp = float(input("Please key in height (cm): "))
            volumep = radius**2 * h * PI / 3
            print("\nThe volume of sphere is {} cm.".format(volumep))


repeat = "Y"

'''Main Procedure'''
while repeat=="Y" or repeat=="y":
    clean()
    head()
    AoV()
    if shape == "A" or shape == "a" or shape == "B" or shape == "b" or shape == "C" or shape == "c":
        calc()
    else:
        print("\n\n\n\t\t============================================")
        print("\t\t||             Inavalid Input!            ||")
        print("\t\t============================================")


    print("\n\n░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
    repeat = input("░▓░▓░▓░▓░▓ Calculate again?: ([Y]/[N]) ")
    print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")

clean()
print("\n\n\n\n\n\n")

print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓")
print("░▓░▓░▓░▓░▓               Thank You for using Calculator                 ░▓░▓░▓░▓░▓")
print("░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓░▓\n")

time.sleep(3)
#Primary


