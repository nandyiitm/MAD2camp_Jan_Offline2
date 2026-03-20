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

        <button type="submit" :disabled="creating">
          {{ creating ? 'Creating...' : '➕ Create Mobile' }}
        </button>
      </form>
    </div>

    <!-- MOBILE LIST -->
    <div class="card">
      <h2>📱 Mobiles List</h2>

      <!-- 🔄 LOADING UI -->
      <div v-if="loading" class="loading-container">
        <div class="spinner"></div>
        <p>Fetching mobiles...</p>
      </div>

      <!-- 📭 EMPTY -->
      <div v-else-if="mobiles.length === 0" class="empty">
        <p>No mobiles found 😕</p>
      </div>

      <!-- ✅ DATA -->
      <div v-else class="mobile-grid">
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
</template>

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
      mobiles: [],
      loading: false,
      creating: false
    }
  },

  methods: {
    async createMobile() {
      this.creating = true;

      try {
        const response = await fetch('http://localhost:5000/mobiles', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify(this.FormData)
        });

        if (response.status === 401) {
          alert('Unauthorized! Please log in again.');
          localStorage.clear();
          window.location.href = '/login';
          return;
        }

        const data = await response.json();

        this.mobiles = [...this.mobiles, data.mobile];

        // 🔄 reset form
        this.FormData = {
          name: '',
          color: '',
          ram: '',
          price: ''
        };

      } catch (error) {
        console.error(error);
      } finally {
        this.creating = false;
      }
    },

    async loadMobiles() {
      this.loading = true;

      try {
        const response = await fetch('http://localhost:5000/mobiles', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`
          }
        });

        if (response.status === 401) {
          alert('Unauthorized! Please log in again.');
          localStorage.clear();
          window.location.href = '/login';
          return;
        }

        const data = await response.json();
        this.mobiles = data.mobiles;

      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    }
  },

  mounted() {
    const user = JSON.parse(localStorage.getItem('user'));

    if (!user) {
      alert('You must be logged in');
      window.location.href = '/login';
      return;
    }

    if (user.role !== 'admin') {
      alert('Access denied');
      window.location.href = '/user';
      return;
    }

    this.loadMobiles();
  }
}
</script>

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

.form-card button:disabled {
  background: #999;
  cursor: not-allowed;
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

/* LOADING */
.loading-container {
  text-align: center;
  padding: 30px;
}

.spinner {
  margin: 0 auto 10px;
  width: 30px;
  height: 30px;
  border: 4px solid #ccc;
  border-top: 4px solid #1976d2;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

/* EMPTY */
.empty {
  text-align: center;
  padding: 20px;
  color: gray;
}

/* ANIMATION */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>