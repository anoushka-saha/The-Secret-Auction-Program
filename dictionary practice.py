user_input = input("Who's grades are you looking for?")

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

found = False
for key in student_scores:
    if key == user_input:
        print("The student you are looking for is " + user_input + " and their grade is " + str(student_scores[key]))
        if student_scores[key] >= 91:
            print("This grade is outstanding")
        elif student_scores[key] >= 81 and student_scores[key] <= 90:
            print("This grade exceeds expectations")
        elif student_scores[key] >= 71 and student_scores[key] <= 80:
            print("This grade is acceptable")
        else:
            print("This grade is a fail")
        found = True
        break

if not found:
    print("The student you are looking for is not in our system")
