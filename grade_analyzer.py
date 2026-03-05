# Task 1 — Process Scores
def process_scores(students):
    averages = {}

    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages


# Task 2 — Classify Grades
def classify_grades(averages):
    classified = {}

    # grading thresholds defined locally
    grade_A = 90
    grade_B = 75
    grade_C = 60

    for name, avg in averages.items():
        if avg >= grade_A:
            grade = "A"
        elif avg >= grade_B:
            grade = "B"
        elif avg >= grade_C:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


# Task 3 — Generate Report
def generate_report(classified, passing_avg=70):
    passed = 0
    failed = 0

    print("===== Student Grade Report =====")

    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"

        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    total_students = len(classified)

    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")

    return passed


# Main block
if __name__ == "__main__":

    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62],
        "Clara": [95, 98, 96]
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    passed_count = generate_report(classified)