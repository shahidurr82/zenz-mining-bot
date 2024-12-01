// static/js/script.js  

// Add any necessary JavaScript functionality here.  
document.addEventListener('DOMContentLoaded', () => {  
    console.log("Web3 Mining Dashboard Loaded");  
    // Future functionalities like fetching data can be added here  
});

 
document.addEventListener('DOMContentLoaded', () => {  
    const refreshButton = document.getElementById('refresh-button');  

    refreshButton.addEventListener('click', () => {  
        // Example to simulate data refresh  
        fetch('/refresh-data')  // This would be a route in your Flask app to get new data  
            .then(response => response.json())  
            .then(data => {  
                const latestBlock = document.querySelector('.mining-data p:nth-child(1)');  
                const gasPrice = document.querySelector('.mining-data p:nth-child(2)');  
                
                latestBlock.textContent = `Latest Block: ${data.latest_block}`;  
                gasPrice.textContent = `Gas Price: ${data.gas_price} Gwei`;  
            })  
            .catch(error => console.error('Error fetching data:', error));  
    });  
});