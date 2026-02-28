from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error, IntegrityError
import re
import os

app = Flask(__name__)
CORS(app)

# Secret key (important for production)
app.secret_key = "supersecretkey"

# ===============================
# DATABASE CONNECTION
# ===============================

# ===============================
# DATABASE CONNECTION
# ===============================

# ===============================
# DATABASE CONNECTION (Railway)
# ===============================

try:
    db = mysql.connector.connect(
        host=os.environ.get("MYSQLHOST"),
        user=os.environ.get("MYSQLUSER"),
        password=os.environ.get("MYSQLPASSWORD"),
        database=os.environ.get("MYSQLDATABASE"),
        port=int(os.environ.get("MYSQLPORT",3306))
    )

    cursor = db.cursor(dictionary=True)

except Error as e:
    print("Database connection error:", e)

# ===============================
# PAGE ROUTES
# ===============================

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/donors-page")
def donors():
    return render_template("donors.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ===============================
# REGISTER DONOR API
# ===============================
# Temporary only once run cheyyi
# Temporary: Ensure donors table exists with all required columns
# Temporary snippet: run once in Flask app
# ===============================
# TEMPORARY TABLE CREATION (ONE-TIME)
# ===============================
# Temporary: Add missing 'contact' column if not exists
# Temporary: Add missing columns safely (one-time run)
columns_to_add = {
    
    "country": "VARCHAR(50)",
    "state": "VARCHAR(50)",
    "city": "VARCHAR(50)"
}

for col, col_type in columns_to_add.items():
    try:
        cursor.execute(f"ALTER TABLE donors ADD {col} {col_type}")
        db.commit()
        print(f"✅ Column '{col}' added successfully!")
    except Exception as e:
        print(f"⚠️ Column '{col}' may already exist or error:", e)

@app.route("/register_donor", methods=["POST"])
def register_donor():

    data = request.json

    # 🔎 Check email already exists
    cursor.execute("SELECT * FROM donors WHERE email=%s", (data["email"],))
    email_exists = cursor.fetchone()

    if email_exists:
        return jsonify({"message": "Email already existed"}), 400

    # 🔎 Check contact already exists
    cursor.execute("SELECT * FROM donors WHERE contact=%s", (data["contact"],))
    contact_exists = cursor.fetchone()

    if contact_exists:
        return jsonify({"message": "Contact already existed"}), 400

    # ✅ If no duplicates, insert data
    query = """
        INSERT INTO donors 
        (name, age, gender, blood_group, contact, email, country, state, city)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        data["name"],
        data["age"],
        data["gender"],
        data["blood_group"],
        data["contact"],
        data["email"],
        "India",
        data["state"],
        data["city"]
    )

    cursor.execute(query, values)
    db.commit()

    return jsonify({"message": "❤️You are now someone's hero!"}), 201
# ===============================
# SEARCH DONORS API
# ===============================

@app.route("/search_donors", methods=["POST"])
def search_donors():

    data = request.get_json()

    if not data:
        return jsonify([])

    blood = data.get("blood")
    state = data.get("state")
    city = data.get("city")

    if not blood or not state or not city:
        return jsonify([])

    try:
        query = """
            SELECT donor_id, name, age, gender, blood_group, contact, email, state, city
            FROM donors
            WHERE blood_group = %s
            AND state = %s
            AND city = %s
            ORDER BY donor_id DESC
        """

        values = (blood, state, city)

        cursor.execute(query, values)
        donors = cursor.fetchall()

        return jsonify(donors)

    except Error:
        return jsonify([])

# ===============================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway sets PORT automatically
    app.run(host="0.0.0.0", port=port, debug=False)
