from flask import Flask, render_template, request, redirect, session
from db import get_connection
app = Flask(__name__)
app.secret_key = "secret"
@app.route('/')
def home():
    return render_template('login.html')
# Register
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s,%s)", (username, password))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/')
    return render_template('register.html')
# Login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        session['user'] = username
        return redirect('/dashboard')
    else:
        return "Invalid Login"
# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
# Search
@app.route('/search', methods=['POST'])
def search():
    category = request.form['category']
    search = request.form['search']
    conn = get_connection()
    cur = conn.cursor()
    if search:
        cur.execute("SELECT * FROM plants WHERE name ILIKE %s", ('%' + search + '%',))
    else:
        cur.execute("SELECT * FROM plants WHERE category=%s", (category,))
    plants = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('result.html', plants=plants)
# Plant Detail
@app.route('/plant/<int:id>')
def plant_detail(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM plants WHERE id=%s", (id,))
    plant = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('detail.html', plant=plant)
if __name__ == "__main__":
    app.run(debug=True)


