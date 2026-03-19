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

    <p>Already have an account? <router-link to="/login">Login here</router-link></p>

</template>
<script setup> // composition API style
import { RouterLink } from 'vue-router'
import {ref, reactive, onMounted} from 'vue'

const formData = reactive({
    name: 'user100',
    email: 'user100@gmail.com',
    password: '12345678'
})

function submitForm() {
    alert(`Form submitted with name: ${formData.name}, email: ${formData.email}, password: ${formData.password}`)
    console.log('Form submitted with data:', formData)

    fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })

    // Here you would typically send the form data to your backend API
    // For example, using fetch or axios to POST the data to your /register endpoint
}

</script>