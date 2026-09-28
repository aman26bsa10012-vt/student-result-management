from src.database import pull_student_data

def calculate_grades(roll_num):
    dataset = pull_student_data()
    idx = 0
    student = None
    while idx < len(dataset):
        if dataset[idx]["roll"] == roll_num:
            student = dataset[idx]
            break
        idx = idx + 1
    if student is None: return None
    total_marks = student["math"] + student["sci"] + student["eng"]
    percentage = total_marks / 3.0
    grade = "F"
    if percentage >= 90: grade = "A+"
    elif percentage >= 75: grade = "A"
    elif percentage >= 60: grade = "B"
    elif percentage >= 50: grade = "C"
    elif percentage >= 33: grade = "D"
    return {"name": student["name"], "total": total_marks, "percentage": percentage, "grade": grade}

def generate_class_report():
    dataset = pull_student_data()
    if len(dataset) == 0: return "No students in database."
    class_total = 0.0
    highest_pct = 0.0
    topper = "None"
    idx = 0
    while idx < len(dataset):
        st = dataset[idx]
        curr_pct = (st["math"] + st["sci"] + st["eng"]) / 3.0
        class_total = class_total + curr_pct
        if curr_pct > highest_pct:
            highest_pct = curr_pct
            topper = st["name"]
        idx = idx + 1
    class_avg = class_total / len(dataset)
    return "Class Average: " + str(round(class_avg, 2)) + "% | Class Topper: " + topper + " (" + str(round(highest_pct, 2)) + "%)"
