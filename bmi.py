def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))
    BMI = weight/(height **2)
    print ("BMI = ", round(BMI))
    print ("Weight Classification: ", end="")
    if BMI < 18.5:
        print("Under Weight")
        return -1
    elif BMI >25.0:
        print("Over Weight")
        return 1
    else:
        print("Normal Weight")
        return 0

result = calculate_bmi(weight=700, height=1.73)
print ("Result = ", result)
