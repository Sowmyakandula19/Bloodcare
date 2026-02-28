🩸 Blood Donation Management System

📖 Description:

Blood Donation Management System is a web-based platform that allows users to register as blood donors, search for donors by blood group and location, submit blood requests, and manage blood inventory efficiently. It provides a user-friendly interface for donors, hospitals, and administrators.

✨ Features:
🧑‍🤝‍🧑 Donor registration with personal details and blood group
🔍 Search for donors by blood group, state, and city
🏥 Submit blood requests and track inventory
📊 Admin panel for managing donors, requests, and stock
🎨 Responsive and user-friendly design
🔗 JSON API for frontend integration

🛠️ Technologies Used:
🐍 Python (Flask)
💾 MySQL
🌐 HTML, CSS, JavaScript
🧩 Flask-CORS
🚀 Railway Deployment

🌐 Deployment Link:bloodcare-production.up.railway.app



👩‍💻 Created By

Kandula Sowmya
G.V. Sindhu
M.Rena

📂 Database Structure

Donors Table: id, name, email, age, gender, blood_group, password, contact, country, state, city

Requests Table: request_id, patient_name, blood_group, units_needed, hospital, contact, request_date

Blood Inventory Table: blood_group, units_available

🛣️ How It Works (Workflow)

1️⃣ Donor Registration: User fills form → Backend validates → Data stored in MySQL → Success message

2️⃣ Search Donors: User inputs blood, state, city → Backend queries donors table → Returns matching donors

3️⃣ Blood Requests & Inventory: Hospital submits request → Stored in requests table → Update blood_inventory table
