import os  
import json  
from flask import Flask, render_template, request, jsonify  
from dotenv import load_dotenv  
from web3 import Web3  

# Load environment variables  
load_dotenv()  
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  
INFURA_PROJECT_ID = os.getenv('INFURA_PROJECT_ID')  

# Initialize Web3  
web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))  

# File to store admin users  
ADMIN_FILE = 'admins.json'  

# Load admin users from JSON file  
def load_admins():  
    if os.path.exists(ADMIN_FILE):  
        with open(ADMIN_FILE, 'r') as file:  
            return json.load(file)  
    return []  

# Save admin users to JSON file  
def save_admins(admins):  
    with open(ADMIN_FILE, 'w') as file:  
        json.dump(admins, file)  

# Initialize Flask app  
app = Flask(__name__)  
admins_list = load_admins()  
is_mining = False  # Flag to track mining status  

# Home route  
@app.route('/')  
def index():  
    return render_template('index.html')  

# Status route  
@app.route('/status')  
def status():  
    return 'Mining is currently ' + ('running.' if is_mining else 'stopped.')  

# Start mining route  
@app.route('/mine', methods=['POST'])  
def start_mining():  
    global is_mining  
    is_mining = True  
    return 'Mining started!'  

# Stop mining route  
@app.route('/stop', methods=['POST'])  
def stop_mining():  
    global is_mining  
    is_mining = False  
    return 'Mining stopped.'  

# Add admin route  
@app.route('/addadmin', methods=['POST'])  
def add_admin():  
    data = request.get_json()  
    user_id = data['user_id']  
    if user_id.isdigit() and int(user_id) not in admins_list:  
        admins_list.append(int(user_id))  
        save_admins(admins_list)  
        return 'Admin added successfully.'  
    return 'Invalid admin ID or already an admin.'  

# Remove admin route  
@app.route('/removeadmin', methods=['POST'])  
def remove_admin():  
    data = request.get_json()  
    user_id = data['user_id']  
    if user_id.isdigit() and int(user_id) in admins_list:  
        admins_list.remove(int(user_id))  
        save_admins(admins_list)  
        return 'Admin removed successfully.'  
    return 'Invalid admin ID or not an admin.'  

# List admins route  
@app.route('/admins')  
def list_admins():  
    return jsonify(admins_list)  

if __name__ == '__main__':  
    app.run(debug=True)

    # Admin management route  
@app.route('/admin')  
def admin():  
    return render_template('admin.html')
from flask import session, redirect, url_for  

# Sample hardcoded credentials (replace with a secure method for real applications)  
valid_username = "admin"  
valid_password = "password123"  

@app.route('/login', methods=['POST'])  
def login():  
    data = request.get_json()  
    username = data.get('username')  
    password = data.get('password')  

    if username == valid_username and password == valid_password:  
        session['logged_in'] = True  
        return jsonify(success=True, message='Login successful!')  
    else:  
        return jsonify(success=False, message='Invalid credentials. Please try again.')  

@app.route('/logout')  
def logout():  
    session.pop('logged_in', None)  
    return redirect(url_for('login'))  # Redirect to login page after logout