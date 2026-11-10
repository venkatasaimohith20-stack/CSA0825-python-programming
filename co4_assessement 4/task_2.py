import pathlib

def process_monthly_attendance(folder_path, summary_file, error_file, low_attendance_file):
    attendance_counts = {}
    error_log = []    
    folder = pathlib.Path(folder_path)
    for file_path in folder.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                clean_line = line.strip()
                if not clean_line:
                    continue                
                parts = [p.strip() for p in clean_line.split(",")]
                if len(parts) != 3:
                    error_log.append(f"{file_path.name},{line_no},Incorrect number of fields")
                    continue               
                reg_no, date_str, status = parts
                if status not in ("P", "A"):
                    error_log.append(f"{file_path.name},{line_no},Invalid status '{status}'")
                    continue               
                if reg_no not in attendance_counts:
                    attendance_counts[reg_no] = {"present": 0, "absent": 0}
                if status == "P":
                    attendance_counts[reg_no]["present"] += 1
                else:
                    attendance_counts[reg_no]["absent"] += 1
    summary_lines = ["RegisterNumber,Present,Absent,TotalClasses,Percentage"]
    low_lines = ["RegisterNumber,Percentage"]
    for reg_no, counts in attendance_counts.items():
        present = counts["present"]
        absent = counts["absent"]
        total = present + absent        
        percentage = (present / total * 100) if total > 0 else 0.0       
        summary_lines.append(f"{reg_no},{present},{absent},{total},{percentage:.2f}%")       
        if percentage < 75.0:
            low_lines.append(f"{reg_no},{percentage:.2f}%")
    # Write files
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))    
    with open(low_attendance_file, "w", encoding="utf-8") as f:
        f.write("\n".join(low_lines))    
    with open(error_file, "w", encoding="utf-8") as f:
        f.write("FileName,LineNumber,Message\n" + "\n".join(error_log))
    print("Task 2 processing complete successfully!")
