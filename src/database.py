import os

def pull_student_data():
    filename = "data/students.txt"
    rows = []
    if not os.path.exists(filename): return rows
    f = open(filename, "r")
    blob = f.read()
    f.close()
    lines = blob.split("\n")
    idx = 0
    while idx < len(lines):
        ln = lines[idx].strip()
        if len(ln) > 0:
            p = ln.split("|")
            if len(p) == 5:
                rows.append({"roll": p[0], "name": p[1], "math": float(p[2]), "sci": float(p[3]), "eng": float(p[4])})
        idx = idx + 1
    return rows

def push_student_data(big_list):
    filename = "data/students.txt"
    writer = open(filename, "w")
    idx = 0
    while idx < len(big_list):
        item = big_list[idx]
        writer.write(item['roll'] + "|" + item['name'] + "|" + str(item['math']) + "|" + str(item['sci']) + "|" + str(item['eng']) + "\n")
        idx = idx + 1
    writer.close()

def add_student_record(roll, name, m, s, e):
    history = pull_student_data()
    idx = 0
    while idx < len(history):
        if history[idx]["roll"] == roll: return "Roll number already exists!"
        idx = idx + 1
    item_structure = {"roll": roll, "name": name, "math": float(m), "sci": float(s), "eng": float(e)}
    history.append(item_structure)
    push_student_data(history)
    return "Student added successfully."

def remove_student_record(roll):
    old_records = pull_student_data()
    new_records = []
    idx = 0
    while idx < len(old_records):
        row = old_records[idx]
        if row["roll"] != roll: new_records.append(row)
        idx = idx + 1
    if len(old_records) == len(new_records): return "Student not found."
    push_student_data(new_records)
    return "Record removed successfully."
