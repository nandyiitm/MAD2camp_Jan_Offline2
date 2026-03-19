<script setup>
import router from '@/router';
import TheWelcome from '../components/TheWelcome.vue'

import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

  <h1>Mobile shop</h1>

  <p>Welcome to our mobile shop!</p>

  <p>Discover the latest smartphones at unbeatable prices.</p>

  <p>Shop now and save big!</p>

  <p>Login to your account <router-link to="/login">Login</router-link> or create a new account <router-link to="/register">Register</router-link> </p>

  <main>
    <!-- <TheWelcome /> -->
  </main>
</template>
