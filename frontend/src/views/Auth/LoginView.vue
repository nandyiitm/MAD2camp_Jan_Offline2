<template>

    <h1>Login to your account to continue</h1>

    <form method="POST">
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <button type="submit">Login</button>
    </form>

    <p>Don't have an account? <router-link to="/register">Register here</router-link></p>

</template>
<script setup>
import { RouterLink } from 'vue-router'

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