<template>

    <h1>Login to your account to continue</h1>

    <form @submit.prevent="login">
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" v-model="formData.email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="formData.password" required>
        </div>
        <button type="submit">Login</button>
    </form>

    <p :class="status ? 'success' : 'error'">{{ message }}</p>

    <p>Don't have an account? <router-link to="/register">Register here</router-link></p>

</template>
<script setup>
import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'

const formData = reactive({
    email: '',
    password: ''
})
const message = ref('')
const status = ref(false)

async function login() {
    console.log('Login form submitted with data:', formData)

    const response = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })

    console.log('Response from server:', response)
    
    let data = await response.json()

    if (!response.ok) {
        message.value = 'Login failed: ' + data.message
        return
    } else {
        console.log('Login successful, data from server:', data)
        message.value = 'Login successful! Redirecting...'
        status.value = true

        // Store the token and user info in localStorage
        localStorage.setItem('token', data.access_token)
        localStorage.setItem('user', JSON.stringify(data.user))

        setTimeout(() => {
            if (data.user.role === 'admin') {
                window.location.href = '/admin'
            } else {
                window.location.href = '/user'
            }
        }, 3000)



    }

    

    console.log('Data from server:', data)

}

</script>


<style>
/* Page styling */
body {
    font-family: Arial, sans-serif;
    background: #f4f6f8;
}

/* Center container */
form {
    max-width: 400px;
    margin: 40px auto;
    padding: 25px;
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

/* Heading */
h1 {
    text-align: center;
    margin-top: 30px;
    color: #333;
}

/* Form groups */
form div {
    margin-bottom: 15px;
}

/* Labels */
label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
    color: #555;
}

/* Inputs */
input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 14px;
    transition: border 0.2s ease;
}

input:focus {
    border-color: #007bff;
    outline: none;
}

/* Button */
button {
    width: 100%;
    padding: 12px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 6px;
    font-size: 16px;
    cursor: pointer;
    transition: background 0.3s ease;
}

button:hover {
    background: #0056b3;
}

/* Message text */
p {
    text-align: center;
    margin-top: 15px;
    color: #444;
}
p.error {
    color: red;
}
p.success {
    color: green;
}

/* Link */
a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>