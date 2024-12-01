from web3 import Web3  
from solcx import compile_standard, install_solc  

# Install the desired version of Solidity if not already installed  
install_solc('0.8.0')  

# Read the Solidity contract  
with open("contracts/YourContract.sol", "r") as file:  
    contract_source_code = file.read()  

# Compile the contract  
compiled_sol = compile_standard(  
    {  
        "language": "Solidity",  
        "sources": {  
            "YourContract.sol": {  
                "content": contract_source_code  
            }  
        },  
        "settings":  
            {  
                "outputSelection": {  
                    "*": {  
                        "*": [  
                            "*"  
                        ]  
                    }  
                }  
            }  
    },  
    solc_version='0.8.0',  
)  

# Extract the contract interface (ABI and bytecode)  
contract_id = compiled_sol['contracts']['YourContract.sol']['YourContract']['evm']['bytecode']['object']  
contract_abi = compiled_sol['contracts']['YourContract.sol']['YourContract']['abi']  

# Connect to an Ethereum node (e.g., Infura or a local node)  
w3 = Web3(Web3.HTTPProvider('YOUR_INFURA_URL'))  

# Set the default account for transactions  
w3.eth.default_account = w3.eth.accounts[0]  

# Deploy the contract  
YourContract = w3.eth.contract(abi=contract_abi, bytecode=contract_id)  

# Create a transaction to deploy the contract  
transaction = YourContract.constructor("MyContract", 0).buildTransaction({  
    'from': w3.eth.default_account,  
    'nonce': w3.eth.getTransactionCount(w3.eth.default_account),  
    'gas': 3000000,  
    'gasPrice': w3.toWei('50', 'gwei')  
})  

# Sign and send the transaction  
signed_txn = w3.eth.account.signTransaction(transaction, private_key='YOUR_PRIVATE_KEY')  
txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)  

# Wait for the transaction to be mined  
txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)  

print(f"Contract deployed at address: {txn_receipt.contractAddress}")