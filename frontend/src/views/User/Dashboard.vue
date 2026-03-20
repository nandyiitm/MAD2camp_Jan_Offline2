<template>
    <h1>User Dashboard!</h1>
    <button @click="logout">Logout</button>
    <p>This is a protected route accessible only to authenticated users.</p>
</template>

<script setup>
import { onMounted } from 'vue'

function logout() {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
    window.location.href = '/login'
}

onMounted(() => {
    console.log('User Dashboard mounted!')

    if (!localStorage.getItem('user')) {
        alert('You must be logged in to access this page.')
        window.location.href = '/login'
    }
})

</script>