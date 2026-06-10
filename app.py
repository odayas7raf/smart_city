from flask import Flask, jsonify, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import random
import bcrypt
import pickle
import numpy as np

with open('traffic_model.pkl', 'rb') as f:
    traffic_model = pickle.load(f)

app = Flask(__name__)
app.secret_key = 'smartcity2024'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'smart_city'

mysql = MySQL(app)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            session['username'] = username
            session['role'] = user[3]
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/api/data')
def get_data():
    if 'username' not in session:
        return jsonify({"error": "unauthorized"}), 401
    data = {
        "vehicles": random.randint(130, 165),
        "energy": round(random.uniform(3.1, 4.6), 1),
        "bins": random.randint(255, 315),
        "alerts": random.randint(1, 7),
        "transport": {
            "bus": random.randint(65, 98),
            "metro": random.randint(80, 99),
            "traffic": random.randint(35, 85),
            "parking": random.randint(25, 75)
        },
        "energy_grid": {
            "solar": random.randint(40, 80),
            "wind": random.randint(15, 45),
            "load": random.randint(60, 90)
        },
        "waste": {
            "zones": random.randint(7, 10),
            "trucks": random.randint(8, 15),
            "full_bins": random.randint(3, 12),
            "recycling": random.randint(30, 50)
        }
    }
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO city_data (vehicles, energy, bins, alerts) VALUES (%s, %s, %s, %s)',
                (data['vehicles'], data['energy'], data['bins'], data['alerts']))
    mysql.connection.commit()
    cur.close()
    return jsonify(data)

@app.route('/api/history')
def get_history():
    if 'username' not in session:
        return jsonify({"error": "unauthorized"}), 401
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM city_data ORDER BY timestamp DESC LIMIT 20')
    rows = cur.fetchall()
    cur.close()
    history = [{"id": r[0], "vehicles": r[1], "energy": r[2],
                "bins": r[3], "alerts": r[4], "timestamp": str(r[5])} for r in rows]
    return jsonify(history)
@app.route('/api/predict')
def predict():
    if 'username' not in session:
        return jsonify({"error": "unauthorized"}), 401
    vehicles = random.randint(10, 200)
    hour = 8
    day = 1
    prediction = traffic_model.predict([[vehicles, hour, day]])[0]
    labels_map = {0: 'Low', 1: 'Medium', 2: 'High'}
    return jsonify({
        "vehicles": vehicles,
        "predicted_congestion": labels_map[prediction],
        "hour": hour,
        "day": day
    })
@app.route('/transport')
def transport():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('transport.html')

@app.route('/energy')
def energy():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('energy.html')

@app.route('/waste')
def waste():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('waste.html')

@app.route('/safety')
def safety():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('safety.html')

if __name__ == '__main__':
    app.run(debug=True)