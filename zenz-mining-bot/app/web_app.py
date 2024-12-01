# app/web_app.py  
from flask import Blueprint, render_template  
from mining_logic import get_mining_info  

main = Blueprint('web_app', __name__)  

@main.route('/')  
def index():  
    mining_info = get_mining_info()  
    return render_template('index.html', mining_info=mining_info)
  
from flask import jsonify  

@main.route('/refresh-data')  
def refresh_data():  
    mining_info = get_mining_info()  
    return jsonify({  
        'latest_block': mining_info['latest_block'],  
        'gas_price': mining_info['gas_price'],  
        'wallet_address': mining_info['wallet_address']  # Assuming you add wallet address handling  
    })

# app/web_app.py  
from flask import Blueprint, render_template  
from .mining_logic import get_mining_info  

main = Blueprint('main', __name__)  

@main.route('/')  
def index():  
    mining_info = get_mining_info()  # This function fetches current mining data  
    return render_template('index.html', latest_block=mining_info['latest_block'], gas_price=mining_info['gas_price'])
