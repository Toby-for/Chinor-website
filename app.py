from flask import Flask, render_template, request, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-random-secret'

# In-memory user "database"
users = {}

# Sample SAT questions data
QUESTIONS = [
    {
        "id": 1,
        "section": "Math",
        "prompt": "What is the value of x in the equation 2x + 3 = 7?",
        "options": ["1", "2", "3", "4"],
        "answer": "B"  # Correct option index 1 (option "2")
    },
    {
        "id": 2,
        "section": "Reading",
        "prompt": "Which choice best describes the main idea of the passage?",
        "options": ["Choice A", "Choice B", "Choice C", "Choice D"],
        "answer": "A"
    }
]

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in users:
            error = 'User already exists.'
            return render_template('register.html', error=error)
        users[email] = password
        session['user'] = email
        return redirect(url_for('dashboard'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if users.get(email) == password:
            session['user'] = email
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials.'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/questions')
def get_questions():
    """Return a list of SAT questions in JSON format."""
    return jsonify(QUESTIONS)

if __name__ == '__main__':
    app.run(debug=True)
