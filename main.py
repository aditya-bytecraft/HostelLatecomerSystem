from database import create_db, add_latecomer
from email_handler import send_email

def handle_latecomer(name, email, parent_email):
    strikes = add_latecomer(name, email, parent_email)

    if strikes == 1:
        send_email(email, "Hostel Latecoming Warning",
                   f"Dear {name},\n\nThis is your first warning for being late to the hostel.")
        print("Warning email sent to student.")
    elif strikes == 2:
        send_email(parent_email, "Your Ward was Late Again",
                   f"Dear Parent,\n\nYour ward {name} has been late to the hostel again. This is the second offense.")
        print("Email sent to parents.")
    elif strikes >= 3:
        print(f"{name} has now been fined ₹3000 for repeated latecoming.")

if __name__ == "__main__":
    create_db()
    while True:
        name = input("Enter student's name: ")
        email = input("Enter student's email: ")
        parent_email = input("Enter parent's email: ")
        handle_latecomer(name, email, parent_email)
        cont = input("Add another? (y/n): ").lower()
        if cont != 'y':
            break
