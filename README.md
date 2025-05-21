# Hostel Latecomer Monitoring System

A Python-based automation system to track and manage hostel latecomers using a three-strike rule. This project demonstrates automation, database management, and secure email handling.

---

## 🚀 Features

- 📬 Sends a **warning email** to students on first offense
- 📧 Notifies **parents** via email on second offense
- 💸 Applies a **₹3000 fine** automatically on third offense
- 🗂 Uses **SQLite** for student and offense tracking
- 🔐 Sends secure emails using **Gmail SMTP** and **App Passwords**

---

## 🧑‍💻 Technologies Used

- Python 3
- SQLite (`sqlite3` module)
- Email Automation (`smtplib`, `email.mime`)
- Environment variables for credential security
- VS Code & GitHub for development and version control

---

## 📁 Project Structure

```
HostelLatecomerSystem/
├── main.py                # Main execution logic
├── database.py            # Handles SQLite database operations
├── email_handler.py       # Sends different types of emails
├── students.db            # SQLite database file
├── .env                   # (Optional) for email credentials
└── README.md              # Project overview
```

---

## 🔑 3-Strike Logic Workflow

1. **First offense:**
   - Record offense
   - Send warning email to student

2. **Second offense:**
   - Update offense count
   - Notify parents via email

3. **Third offense:**
   - Update offense count
   - Flag student with ₹3000 fine

---

## 🛠 Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/aditya-bytecraft/HostelLatecomerSystem.git
cd HostelLatecomerSystem
```

2. **Install Python Dependencies**
```bash
pip install -r requirements.txt
```
(You only need built-in libraries like `sqlite3` and `smtplib`, so a `requirements.txt` may be optional.)

3. **Configure Email Credentials**
- Go to your [Google Account App Passwords](https://myaccount.google.com/apppasswords)
- Generate one for "Mail" and copy it
- Store credentials securely in environment variables or replace in code (not recommended)

4. **Run the Program**
```bash
python main.py
```

---

## 📌 Future Improvements

- Add QR code scanning for automatic late-entry logging
- Build a Flask-based admin dashboard
- Use MySQL or PostgreSQL for better scalability
- Deploy on Render/Heroku for online access

---

## 🧑 Author
**Aditya Mishra**  
[LinkedIn](https://www.linkedin.com/in/aditya-mishra-63aa70278)  
📧 adityamishra8852@gmail.com

---

## 🌟 Show Your Support
If you like this project, give it a ⭐ on GitHub and feel free to fork or contribute!
