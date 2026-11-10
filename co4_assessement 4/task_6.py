import os
def process_department_file(file_path, master_records, error_log, event_participants):
    """
    Processes a single department's registration file, validates records,
    removes duplicates, and logs errors without crashing the program.
    """
    if not os.path.exists(file_path):
        error_log.append((file_path, 0, "Department file missing"))
        return
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                clean_line = line.strip()
                if not clean_line:
                    continue  # Skip empty lines               
                parts = [p.strip() for p in clean_line.split(",")]
                if len(parts) < 5:
                    error_log.append((os.path.basename(file_path), line_no, "Damaged line: insufficient fields"))
                    continue              
                reg_no, name, dept, email, events_str = parts[0], parts[1], parts[2], parts[3], parts[4]            
                # Simple string-based email validation
                if "@" not in email or "." not in email.split("@")[-1]:
                    error_log.append((os.path.basename(file_path), line_no, f"Invalid email format: {email}"))
                    continue
                # Duplicate registration check using a set of register numbers
                if reg_no in master_records:
                    error_log.append((os.path.basename(file_path), line_no, f"Duplicate registration for {reg_no}"))
                    continue     
                # Parse chosen events separated by semicolons
                events = [e.strip() for e in events_str.split(";") if e.strip()] 
                # Store valid record in master dictionary
                master_records[reg_no] = {
                    "name": name,
                    "department": dept,
                    "email": email,
                    "events": events
                }
                # Map participants to their respective event lists
                for event in events:
                    if event not in event_participants:
                        event_participants[event] = []
                    event_participants[event].append((reg_no, name, dept))                   
    except Exception as e:
        error_log.append((os.path.basename(file_path), 0, f"Unexpected error: {str(e)}"))
def run_fest_processing(dept_files):
    master_records = {}
    error_log = []
    event_participants = {}   
    # Process all department files
    for file_path in dept_files:
        process_department_file(file_path, master_records, error_log, event_participants)       
    # Generate Master List Report
    print(f"--- Master List ({len(master_records)} Unique Registrations) ---")
    for reg, info in master_records.items():
        print(f"{reg}: {info['name']} ({info['department']}) - Events: {', '.join(info['events'])}")       
    # Generate Error Log Report
    print(f"\n--- Error Log ({len(error_log)} Issues Encountered) ---")
    for err in error_log:
        print(f"File: {err[0]} | Line: {err[1]} | Reason: {err[2]}")