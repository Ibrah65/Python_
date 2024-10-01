def grading_system(score):
    if score>=80:
        return "A"
    elif score>=70:
        return "B"
    elif score>=60:
        return "C"
    elif score>=50:
        return "D"
    else:
        return "E"
    
try:
    score = int(input("Enter your score: "))
    if 0<=score<=100:
        grade=grading_system(score)
        print(f"The Grade is: {grade}")
    else:
        print(f"Please enter a valid score.")
except ValueError:
    print("Invalid input. Please enter a valid score.")