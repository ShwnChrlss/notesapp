from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Dummy data for demonstration
users = []  # List to store user data (replace with a database in production)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Logic to handle user login (authentication)
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user exists (add your authentication logic here)
        if any(user['username'] == username and user['password'] == password for user in users):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Logic to handle user registration
        username = request.form.get('username')
        password = request.form.get('password')

        # Add user to the list (replace with database logic)
        users.append({'username': username, 'password': password})
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Handle file upload logic here
        flash('File uploaded successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('upload.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/notes')
def notes():
    return render_template('notes.html')

@app.route('/logout')
def logout():
    # Logic for logging out (if applicable)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
