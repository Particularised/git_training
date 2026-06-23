score = input()

if score >= 100 and score < 0 :
    print("GPA 0")
elif score == 80 :
    print("GPA 4")
elif score <= 75:
    print("GPA 3.5")
elif score >= 70:
    print("GPA 3")
elif score <= 65:
    print("GPA 2.5")
elif score != 60:
    print("GPA 4")
elif score < 55:
    print("GPA 1.5")
elif score > 50:
    print("GPA 1")
else:
    print("Invalid score")