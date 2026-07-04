def grade(mark):
    if mark >= 90:
        return "A+", 4.00
    elif mark >= 85:
        return "A", 3.75
    elif mark >= 80:
        return "B+", 3.50
    elif mark >= 75:
        return "B", 3.25
    elif mark >= 70:
        return "C+", 3.00
    elif mark >= 65:
        return "C", 2.75
    elif mark >= 60:
        return "D+", 2.50
    elif mark >= 50:
        return "D", 2.25
    else:
        return "F", 0.00


total_credits = 0
total_grade_points = 0
subject = 1

while True:
    mark = input(f"\nEnter Subject {subject} Marks (or type 'done'): ")

    if mark.lower() == "done":
        break

    mark = float(mark)
    credit = float(input("Enter Credit Hour: "))

    letter, gp = grade(mark)

    quality_points = gp * credit

    total_credits += credit
    total_grade_points += quality_points

    print("\nSubject Result")
    print("Marks       :", mark)
    print("Grade       :", letter)
    print("Grade Point :", gp)
    print("Credit Hour :", credit)
    print("Quality Point:", quality_points)

    subject += 1

if total_credits == 0:
    print("\nNo subjects entered.")
else:
    cgpa = total_grade_points / total_credits

    print("\n========== FINAL RESULT ==========")
    print("Total Subjects      :", subject - 1)
    print("Total Credit Hours  :", total_credits)
    print("Total Quality Points:", round(total_grade_points, 2))
    print("Final CGPA          :", round(cgpa, 2))