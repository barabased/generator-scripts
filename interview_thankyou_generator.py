# Prompt the user to input values for the fields
company_name = input("Enter company name: ")
position_name = input("Enter position name: ")
hiring_manager_name = input("Enter hiring manager's name: ")
your_name = input("Enter your name: ")

# Create the email message using string formatting
email_message = f"Subject: Thank You for Interviewing Me for the {position_name} Role at {company_name}\n\nDear {hiring_manager_name},\n\nI hope this email finds you well. I am writing to express my gratitude for the opportunity to interview for the {position_name} role at {company_name}. It was a pleasure meeting you and discussing the job responsibilities and the company culture.\n\nI appreciate the time you took out of your busy schedule to interview me and answer my questions regarding the position. Your insights and expertise have made me more excited about the prospect of joining {company_name}. I am confident that my skills, experience, and enthusiasm will be an asset to the team.\n\nI would like to reiterate my strong interest in the {position_name} role and my eagerness to contribute to the growth of {company_name}. If there is any additional information you need from me, please do not hesitate to contact me. I look forward to hearing from you soon about the next steps in the hiring process.\n\nThank you again for your time and consideration.\n\nBest regards,\n\n{your_name}"

# Print the email message
print(email_message)
