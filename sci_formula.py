print("============================================")
print("||         Area & Volume Calculator       ||")
print("============================================")
print("\n[A] Cylinder [B] Cube [C] Prism")
shape = str(input("Choose shape to measure: "))
if shape == "A":
    print("\n[1] Area [2] Volume")
    formula = int(input("Choose parameter to compute: "))
    if formula == 1:
        radius = float(input("\nPlease key in radius (m): "))
        heightc = float(input("Please key in height (m): "))
        areacy = (2 * 3.1416 * radius * heightc) + (2 * 3.1416 * radius * radius)
        print("\nThe area of cylinder is {} sq.m.".format(areacy))
    if formula == 2:
        radius = float(input("\nPlease key in radius (m): "))
        height = float(input("Please key in height (m): "))
        volumecy = 3.1416 * radius * radius * height
        print("\nThe volume of cylinder is {} cu.m.".format(volumecy))
if shape == "B":
    print("\n[1] Area [2] Volume")
    formula = int(input("Choose parameter to compute: "))
    if formula == 1:
        side = float(input("\nPlease key in side (m): "))
        areacb = 6 * side * side
        print("\nThe area of cube is {} sq.m.".format(areacb))
    if formula == 2:
        side = float(input("\nPlease key in side (m): "))
        volumecb = side * side * side
        print("\nThe volume of cube is {} cu.m.".format(volumecb))
if shape == "C":
    print("\n[1] Area [2] Volume")
    formula = int(input("Choose parameter to compute: "))
    if formula == 1:
        base = float(input("\nPlease key in base (m): "))
        heightp = float(input("Please key in height (m): "))
        lengthp = float(input("Please key in length (m): "))
        sidep = float(input("Please key in side (m): "))
        areap = base * heightp + 2*lengthp*sidep
        print("\nThe area of prism is {} sq.m.".format(areap))
    if formula == 2:
        lengthp = float(input("\nPlease key in length (m): "))
        width = float(input("Please key in width (m): "))
        heightp = float(input("Please key in height (m): "))
        volumep = lengthp * width * heightp
        print("\nThe volume of cube is {} cu.m.".format(volumep))
if shape == "D":
    print("\n[1] Area [2] Volume")
    formula = int(input("Choose parameter to compute: "))
    if formula == 1:
        base = float(input("\nPlease key in base (m): "))
        heightp = float(input("Please key in height (m): "))
        lengthp = float(input("Please key in length (m): "))
        sidep = float(input("Please key in side (m): "))
        areap = base * heightp + 2*lengthp*sidep
        print("\nThe area of prism is {} sq.m.".format(areap))
    if formula == 2:
        lengthp = float(input("\nPlease key in length (m): "))
        width = float(input("Please key in width (m): "))
        heightp = float(input("Please key in height (m): "))
        volumep = lengthp * width * heightp
        print("\nThe volume of cube is {} cu.m.".format(volumep))

<<<<<<< HEAD
        ## Testing push by Sandy Kalugdan
=======
'''
Testing Update Only!
'''
>>>>>>> a7057d5acd0ba05e272c36d7f73df6d604879fe5
