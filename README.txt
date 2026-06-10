Smart City Connect
==================
Graduation Project - CSE 493
Galala University
Supervisor: Dr. Safa Elaskary
Students: Oday Ashraf - Youssef Wael

Technologies Used:
------------------
- Python 3.x
- Flask (Backend Framework)
- MySQL (Database)
- HTML / CSS / JavaScript (Frontend)
- bcrypt (Password Encryption)
- scikit-learn (ML Model - Traffic Prediction)
- IoT Simulation (Python)

Requirements:
-------------
flask
flask-mysqldb
bcrypt
requests
scikit-learn
numpy

How to Run:
-----------
1. Install Python 3.x from python.org
2. Install XAMPP and start MySQL
3. Open phpMyAdmin: http://localhost/phpmyadmin
4. Create database named: smart_city
5. Import file: smart_city.sql
6. Open cmd in project folder
7. Run: py -m pip install -r requirements.txt
8. Run: py app.py
9. Open browser: http://127.0.0.1:5000
10. Login with: admin / admin123

To run IoT Simulator:
---------------------
Open another cmd and run: py iot_simulator.py

Pages:
------
/ - Main Dashboard
/transport - Transportation
/energy - Energy
/waste - Waste Management
/safety - Public Safety
/api/data - Live sensor data (JSON)
/api/history - Last 20 records
/api/predict - ML traffic prediction