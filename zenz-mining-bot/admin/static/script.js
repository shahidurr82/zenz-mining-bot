async function checkStatus() {  
    const response = await fetch('/status');  
    const data = await response.text();  
    document.getElementById('status').innerText = data;  
}  

async function startMining() {  
    const response = await fetch('/mine', { method: 'POST' });  
    const data = await response.text();  
    document.getElementById('message').innerText = data;  
}  

async function stopMining() {  
    const response = await fetch('/stop', { method: 'POST' });  
    const data = await response.text();  
    document.getElementById('message').innerText = data;  
}  

async function addAdmin() {  
    const adminId = document.getElementById('adminId').value;  
    const response = await fetch('/addadmin', {  
        method: 'POST',  
        headers: { 'Content-Type': 'application/json' },  
        body: JSON.stringify({ user_id: adminId })  
    });  
    const data = await response.text();  
    document.getElementById('message').innerText = data;  
}  

async function removeAdmin() {  
    const adminId = document.getElementById('adminId').value;  
    const response = await fetch('/removeadmin', {  
        method: 'POST',  
        headers: { 'Content-Type': 'application/json' },  
        body: JSON.stringify({ user_id: adminId })  
    });  
    const data = await response.text();  
    document.getElementById('message').innerText = data;  
}  

async function listAdmins() {  
    const response = await fetch('/admins');  
    const data = await response.json();  
    document.getElementById('adminList').innerText = `Admins: ${data.join(', ')}`;  
}
async function handleLogin(event) {  
    event.preventDefault(); // Prevent the default form submission  

    const username = document.getElementById('username').value;  
    const password = document.getElementById('password').value;  

    const response = await fetch('/login', {  
        method: 'POST',  
        headers: { 'Content-Type': 'application/json' },  
        body: JSON.stringify({ username: username, password: password })  
    });  

    const result = await response.json();  
    document.getElementById('message').innerText = result.message;  

    if (result.success) {  
        // Redirect to the main dashboard if login is successful  
        window.location.href = '/';  
    }  
}