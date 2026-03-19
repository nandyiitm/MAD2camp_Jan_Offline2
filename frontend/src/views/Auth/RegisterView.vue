<template>

    <h1>Register for a new account</h1>

    <form method="POST" @submit.prevent="submitForm">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" v-model="formData.name" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" v-model="formData.email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" v-model="formData.password" required>
        </div>
        <button type="submit">Register</button>
    </form>

    <p>{{ message }}</p>

    <p>Already have an account? <router-link to="/login">Login here</router-link></p>

</template>
<script setup> // composition API style
import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'

const formData = reactive({
    name: '',
    email: '',
    password: ''
})

const message = ref('')

function submitForm() {
    // alert(`Form submitted with name: ${formData.name}, email: ${formData.email}, password: ${formData.password}`)
    console.log('Form submitted with data:', formData)

    fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        return response.json().then(data => {
            return { status: response.status, data };
        });
    })
    .then(({ status, data }) => {
        console.log('Response from server:', data);

        if (status === 201) {
            alert('Registration successful!');
            message.value = 'Registration successful! Redirecting to login page...';

            setTimeout(() => {
                window.location.href = '/login';
            }, 3000);
        } else if (status === 409) {
            message.value = 'User with this email already exists. Please try again with a different email.';
        } else {
            alert('Registration failed. Please try again.');
            message.value = data.message || 'Registration failed. Please try again.';
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Registration failed. Please try again.');
    });

    // Here you would typically send the form data to your backend API
    // For example, using fetch or axios to POST the data to your /register endpoint
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

/* Link */
a {
    color: #007bff;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}
</style>