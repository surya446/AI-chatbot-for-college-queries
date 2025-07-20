import re
from difflib import get_close_matches

# Department HOD data
hods = {
    "cse": "Dr. U.M. Fernandes Dimlo",
    "ds": "Mr. M.V. Nagesh",
    "aiml": "Dr. A. Swathi",
    "ece": "Mr. S.V. Maruthi Rao Chinnam",
    "h&s": "Mr. Md. Naseeruddin"
}

def get_closest_department(dept):
    all_keys = list(hods.keys())
    match = get_close_matches(dept.lower(), all_keys, n=1, cutoff=0.6)
    return match[0] if match else None

def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["exit", "quit", "bye"]:
        return "Take care! Bye 👋"

    elif re.search(r"(college name|your name)", user_input):
        return "I'm SreyasBot from Sreyas Institute of Engineering and Technology."

    elif re.search(r"(location|where.*college)", user_input):
        return "The college is located in Hyderabad, near Nagole."

    elif re.search(r"(timings|working hours|time)", user_input):
        return "College runs from 9:00 AM to 4:00 PM, Monday to Saturday."

    elif re.search(r"(lunch|break|lunch break)", user_input):
        return "Lunch break is from 12:10 PM."

    elif re.search(r"(principal|head of college)", user_input):
        return "The principal is Dr. K. Sagar."

    elif re.search(r"(chairman)", user_input):
        return "The Chairman is Sri Anantula Vinay Kumar Reddy."

    elif re.search(r"(vice chairman|vice-chairman|vc)", user_input):
        return "The Vice Chairman is Sri Anantula Hriday Reddy."

    elif re.search(r"(hod|head of department)", user_input):
        # Try to detect specific department
        for dept in hods:
            if dept in user_input:
                return f"The HOD of {dept.upper()} is {hods[dept]}"
        # Try fuzzy match
        words = user_input.split()
        for word in words:
            closest = get_closest_department(word)
            if closest:
                return f"The HOD of {closest.upper()} is {hods[closest]}"
        # If no department found, return all
        return ("HODs:\n"
                "- CSE: Dr. U.M. Fernandes Dimlo\n"
                "- DS: Mr. M.V. Nagesh\n"
                "- AIML: Dr. A. Swathi\n"
                "- ECE: Mr. S.V. Maruthi Rao Chinnam\n"
                "- H&S: Mr. Md. Naseeruddin")

    elif re.search(r"(departments|branches|courses)", user_input):
        return "Departments: CSE, DS, AIML, ECE, and H&S."

    elif re.search(r"(exam|semester|test)", user_input):
        return "Exams are held in May–June and Dec–Jan."

    elif re.search(r"(result|marks)", user_input):
        return "Check results at https://exams.sreyas.ac.in/"

    elif re.search(r"(internal|cie|marks policy)", user_input):
        return ("CIE: 40 marks, SEE: 60 marks. "
                "Need 14 in CIE and 21 in SEE to pass.")

    elif re.search(r"(wifi|internet)", user_input):
        return "Yes, campus has good Wi-Fi access for students."

    elif re.search(r"(library)", user_input):
        return "Library is available; first years have a dedicated period."

    elif re.search(r"(lab|coding club)", user_input):
        return "Yes, the college has excellent computer labs and coding clubs."

    elif re.search(r"(hostel)", user_input):
        return "Hostel is available only for girls."

    elif re.search(r"(bus|transport)", user_input):
        return "College buses cover almost all of Hyderabad."

    elif re.search(r"(official website|site)", user_input):
        return "Visit: https://sreyas.ac.in/"

    elif re.search(r"(contact|apply|admission)", user_input):
        return "Contact college via Phn.no - 9246323444 or visit https://sreyas.ac.in/contact-us-4/"

    elif re.search(r"(fee|fees)", user_input):
        return "Please contact the college for fee structure."

    elif re.search(r"(event|fest)", user_input):
        return ("Annual Day, Traditional Day, and Tech Fest are held yearly. "
                "Other events happen throughout the year.")

    elif re.search(r"(placement)", user_input):
        return "Placement Head: A.V.L. Vara Prasad."

    elif re.search(r"(id card|id)", user_input):
        return "Go to the Admin Office for ID card issues."

    elif re.search(r"(portal|login|password)", user_input):
        return "Contact the student branch for login issues."
    

    else:
        return "Sorry, I didn't understand. Try asking about timings, HODs, or exams."

