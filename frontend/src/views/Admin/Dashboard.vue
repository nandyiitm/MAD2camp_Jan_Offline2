<template>
  <div class="container">
    <h1 class="title">📊 Admin Dashboard</h1>

    <!-- CREATE FORM -->
    <div class="card form-card">
      <h2>Add New Mobile</h2>

      <form @submit.prevent="createMobile">
        <input v-model="FormData.name" placeholder="Mobile Name" required />
        <input v-model="FormData.color" placeholder="Color" required />
        <input v-model.number="FormData.ram" type="number" placeholder="RAM (GB)" required />
        <input v-model.number="FormData.price" type="number" placeholder="Price (₹)" required />

        <button type="submit">➕ Create Mobile</button>
      </form>
    </div>

    <!-- MOBILE LIST -->
    <div class="card">
      <h2>📱 Mobiles List</h2>

      <div class="mobile-grid">
        <div class="mobile-card" v-for="mobile in mobiles" :key="mobile.id">
          <h3>{{ mobile.name }}</h3>

          <p><strong>Color:</strong> {{ mobile.color }}</p>
          <p><strong>RAM:</strong> {{ mobile.ram }} GB</p>
          <p class="price">₹{{ mobile.price.toLocaleString() }}</p>

          <RouterLink class="view-btn" :to="`/admin/mobiles/${mobile.id}`">
            View Details →
          </RouterLink>
        </div>
      </div>
    </div>
  </div>

  <!-- <pre>{{ mobiles }}</pre> -->

</template>

<style>
.container {
  max-width: 900px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}

.title {
  text-align: center;
  margin-bottom: 30px;
}

/* CARD */
.card {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 12px;
  margin-bottom: 25px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

/* FORM */
.form-card form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.form-card input {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
}

.form-card button {
  padding: 10px;
  background: #1976d2;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

/* GRID */
.mobile-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 15px;
}

/* MOBILE CARD */
.mobile-card {
  background: white;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
}

.mobile-card h3 {
  margin-bottom: 10px;
}

.price {
  font-weight: bold;
  color: #2e7d32;
  margin-top: 10px;
}

/* BUTTON */
.view-btn {
  display: inline-block;
  margin-top: 10px;
  text-decoration: none;
  color: white;
  background: #333;
  padding: 6px 10px;
  border-radius: 6px;
}
</style>

<script>
import { RouterLink } from 'vue-router';

export default {
    name: 'AdminDashboard',
    data() {
        return {
            FormData: {
                name: '',
                color: '',
                ram: '',
                price: ''
            },
            mobiles: []
            // You can add any data properties you need here
        }
    },
    methods: {
        // You can add any methods you need here
        async createMobile() {
            const response = await fetch('http://localhost:5000/mobiles', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                },
                body: JSON.stringify(this.FormData)
            });
            console.log(response);
            if (response.status === 401) {
                alert('Unauthorized! Please log in again.')
                localStorage.removeItem('token');
                localStorage.removeItem('user');
                window.location.href = '/login';
                return;
            }
            const data = await response.json();
            console.log(data);
            this.mobiles.push(data.mobile);
        },
        async loadMobiles(){
            const response = await fetch('http://localhost:5000/mobiles', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            });
            console.log(response);
            if (response.status === 401) {
                alert('Unauthorized! Please log in again.')
                localStorage.removeItem('token');
                localStorage.removeItem('user');
                window.location.href = '/login';
                return;
            }
            const data = await response.json();
            console.log(data);
            this.mobiles = data.mobiles;
        }

    },
    mounted() {
        // You can add any code you want to run when the component is mounted here
        console.log('Admin Dashboard mounted!')

        if (localStorage.getItem('user')) {
            const user = JSON.parse(localStorage.getItem('user'))
            if (user.role !== 'admin') {
                alert('Access denied! You are not an admin.')
                window.location.href = '/user'
            }
        } else {
            alert('You must be logged in to access this page.')
            window.location.href = '/login'
        }

        this.loadMobiles();
    
    }
}
</script>