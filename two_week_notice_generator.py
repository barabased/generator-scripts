company_name = input("Enter company name: ")
manager_name = input("Enter manager name: ")
position = input("Enter position: ")
date = input("Enter your last day of work: ")

notice = f"Dear {manager_name},\n\nI am writing to inform you that I have decided to resign from my position as {position} at {company_name}. My last day of work will be two weeks from today, on {date}.\n\nI want to express my gratitude for the opportunities and experiences that I have had during my time at {company_name}. I have learned a great deal and appreciate the support and guidance that you and the team have provided.\n\nPlease let me know if there is anything that I can do to help during this transition. I will do my best to ensure that my responsibilities are fully transitioned to another team member before my departure.\n\nThank you again for everything.\n\nSincerely,\n[Your Name]"

print(notice)
