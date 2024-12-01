# app/mining_logic.py  
from web3 import Web3  
import config  

infura_url = f"https://mainnet.infura.io/v3/{config.INFURA_PROJECT_ID}"  
web3 = Web3(Web3.HTTPProvider(infura_url))  

def get_mining_info():  
    if not web3.isConnected():  
        return "Error connecting to the Ethereum network."  
    latest_block = web3.eth.block_number  
    gas_price = web3.eth.gas_price  
    return f"Latest Block: {latest_block}\nGas Price: {web3.fromWei(gas_price, 'gwei')} Gwei"


# app/mining_logic.py  
from web3 import Web3  
from .config import INFURA_PROJECT_ID  

# Function to connect to Ethereum and fetch mining data  
def get_mining_info():  
    w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}"))  
    latest_block = w3.eth.block_number  
    gas_price = w3.eth.gas_price  

    return {  
        'latest_block': latest_block,  
        'gas_price': gas_price,  
    }