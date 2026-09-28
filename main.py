from src.auth import register_admin, login_admin
from src.database import add_student_record, pull_student_data, remove_student_record
from src.calculator import calculate_grades, generate_class_report

def teacher_dashboard_loop():
    keep_running = True
    while keep_running:
        print("\n=== TEACHER PANEL ===")
        print("1) Add Student  2) View All  3) Delete Student  4) Student Report Card  5) Class Analytics  6) Logout")
        selection = input("Action selection: ").strip()
        if selection == "1":
            r = input("Enter Roll No: ")
            n = input("Enter Name: ")
            m = input("Maths Marks: ")
            s = input("Science Marks: ")
            e = input("English Marks: ")
            print(add_student_record(r, n, m, s, e))
        elif selection == "2":
            rows = pull_student_data()
            idx = 0
            while idx < len(rows):
                line = rows[idx]
                print("Roll:" + line['roll'] + " | Name: " + line['name'] + " | Math: " + str(line['math']) + " | Sci: " + str(line['sci']) + " | Eng: " + str(line['eng']))
                idx = idx + 1
        elif selection == "3":
            roll_to_drop = input("Enter Roll No to drop: ")
            print(remove_student_record(roll_to_drop))
        elif selection == "4":
            roll_card = input("Enter Roll No for Report Card: ")
            res = calculate_grades(roll_card)
            if res is not None:
                print("\n--- REPORT CARD ---")
                print("Name: " + res["name"] + "\nTotal Marks: " + str(res["total"]) + "/300\nPercentage: " + str(round(res["percentage"], 2)) + "%\nFinal Grade: " + res["grade"])
            else: print("Student not found.")
        elif selection == "5":
            print("\n--- CLASS ANALYTICS ---")
            print(generate_class_report())
        elif selection == "6":
            keep_running = False

if __name__ == "__main__":
    app_active = True
    while app_active:
        print("\n--- STUDENT RECORD ENGINE V1 ---")
        print("Choose: a) Register Teacher  b) Teacher Sign In  c) Turn Off System")
        user_intent = input("Command input: ").strip().lower()
        if user_intent == "a":
            usr = input("Enter New Username: ")
            pwd = input("Enter Password: ")
            state = register_admin(usr, pwd)
            if state == "ok_reg": print("Registered successfully.")
            else: print("Username taken.")
        elif user_intent == "b":
            usr = input("Username: ")
            pwd = input("Password: ")
            granted = login_admin(usr, pwd)
            if granted == "auth_yes":
                print("Access Approved.")
                teacher_dashboard_loop()
            else: print("Access Denied.")
        elif user_intent == "c":
            print("Shutting down system.")
            app_active = False
