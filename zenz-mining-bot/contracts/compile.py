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

# Save compiled contract to a file (optional)  
with open("compiled_contract.json", "w") as file:  
    json.dump(compiled_sol, file)  

# Print the ABI and bytecode  
print("ABI:", compiled_sol['contracts']['YourContract.sol']['YourContract']['abi'])  
print("Bytecode:", compiled_sol['contracts']['YourContract.sol']['YourContract']['evm']['bytecode']['object'])