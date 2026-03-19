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