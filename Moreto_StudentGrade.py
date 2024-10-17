#input Student info and grade
print("please input your Name, Section, and grade.")
name = str(input("Name: "))
section = input("Section: ")

#input of grades
prelim = float(input("Prelim: "))

if prelim <40 or prelim >100:
    print("Error! Please input your grade between 40 and 100")
else:
    midterm = float(input("Midterm: "))
    if midterm <40 or midterm >100:
        print("Error! Please input your grade between 40 and 100")
    else:
        finals = float(input("finals: "))
        if finals <40 or finals >100:
            print("Error! Please input your grade between 40 and 100")
        else:
            final_grade = (0.333333*prelim) + (0.3333*midterm) + (0.3333*finals)
            rounded_final = round(final_grade)
            print("final grade =", rounded_final)
            #GPA evaluation
            if rounded_final >=99 and rounded_final <=100:
                GPA = 1.00
                print("Your GPA is", GPA,"(Excellent)!")
            elif rounded_final >=96 and rounded_final <=98:
                GPA = 1.25
                print("Your GPA is", GPA,"(Outstanding)!")
            elif rounded_final >=93 and rounded_final <=95:
                GPA = 1.50
                print("Your GPA is", GPA,"(Superior)!")
            elif rounded_final >=90 and rounded_final <=92:
                GPA = 1.75
                print("Your GPA is", GPA,"(Very Good)!")
            elif rounded_final >=87 and rounded_final <=89:
                GPA = 2.00
                print("Your GPA is", GPA,"(Good)!")
            elif rounded_final >=84 and rounded_final <=86:
                GPA = 2.25
                print("Your GPA is", GPA,"(Satisfactory)!")
            elif rounded_final >=81 and rounded_final <=83:
                GPA = 2.50
                print("Your GPA is", GPA,"(Fairly Satisfactory)!")
            elif rounded_final >=78 and rounded_final <=80:
                GPA = 2.75
                print("Your GPA is", GPA,"(Fair)!")
            elif rounded_final >=75 and rounded_final <=77:
                GPA = 3.00
                print("Your GPA is", GPA,"(Passed)!")
            elif rounded_final <75:
                GPA = 5.0
                print("Your GPA is", GPA,"(Failed).")
            exit
                