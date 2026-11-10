import re
contacts_source_1 = [
    {"name": "Dr. Ravi", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
    {"name": "Anita Kumar", "phone": "9840098400", "email": "anita@yahoo.com"}
]
contacts_source_2 = [
    {"name": "ravi kumar", "phone": "9840012345", "email": "ravi.work@office.com"},
    {"name": "Anita K.", "phone": "+91-98400-98400", "email": "anita@yahoo.com"}
]
def normalize_phone(phone):
    digits = re.sub(r'\D', '', phone)
    return digits[-10:] # Keep last 10 digits as key
def normalize_name(name):
    clean = re.sub(r'\b(dr|mr|mrs|ms)\b\.?', '', name, flags=re.IGNORECASE)
    return " ".join(clean.strip().lower().split())
def merge_contacts(sources):
    merged = {}
    for source in sources:
        for c in source:
            norm_phone = normalize_phone(c["phone"])
            norm_name = normalize_name(c["name"])
            
            if norm_phone not in merged:
                merged[norm_phone] = {
                    "names": {norm_name},
                    "phones": {c["phone"]},
                    "emails": {c["email"]} if c.get("email") else set()
                }
            else:
                merged[norm_phone]["names"].add(norm_name)
                merged[norm_phone]["phones"].add(c["phone"])
                if c.get("email"):
                    merged[norm_phone]["emails"].add(c["email"])
    return merged
unified_contacts = merge_contacts([contacts_source_1, contacts_source_2])
for phone, info in unified_contacts.items():
    print(f"Primary Key Phone: {phone}")
    print(f"  Names  : {info['names']}")
    print(f"  Phones : {info['phones']}")
    print(f"  Emails : {info['emails']}")
    print("-" * 35)