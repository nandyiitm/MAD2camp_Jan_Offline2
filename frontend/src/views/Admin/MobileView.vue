<template>
  <div class="container">
    <h1 class="title">📱 Mobile Details</h1>

    <!-- VIEW MODE -->
    <div class="card" v-if="mobile && !isEditing">
      <h2 class="name">{{ mobile.name }}</h2>

      <div class="details">
        <p><strong>ID:</strong> {{ mobile.id }}</p>

        <p>
          <strong>Color:</strong>
          <span class="badge">{{ mobile.color }}</span>
        </p>

        <p><strong>RAM:</strong> {{ mobile.ram }} GB</p>

        <p class="price">₹{{ mobile.price.toLocaleString() }}</p>
      </div>

      <div class="actions">
        <button class="edit" @click="startEdit">Edit</button>
        <button class="delete" @click="deleteMobile">Delete</button>
      </div>
    </div>

    <!-- EDIT MODE -->
    <div v-else-if="mobile && isEditing" class="edit-form">
      <h3>Edit Mobile</h3>

      <input v-model="mobile.name" placeholder="Name" />
      <input v-model="mobile.color" placeholder="Color" />
      <input v-model.number="mobile.ram" type="number" placeholder="RAM" />
      <input v-model.number="mobile.price" type="number" placeholder="Price" />

      <div class="actions">
        <button class="edit" @click="updateMobile">Save</button>
        <button @click="cancelEdit">Cancel</button>
      </div>
    </div>

    <!-- LOADING -->
    <p v-else class="loading">Loading mobile details...</p>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();

const mobile = ref(null);
const isEditing = ref(false);
const originalMobile = ref(null); // for cancel edit

onMounted(() => {
  loadMobile();
});

// 🔄 Handle route change
watch(() => route.params.id, () => {
  loadMobile();
});

// 📡 Load mobile
async function loadMobile() {
  try {
    const response = await fetch(`http://localhost:5000/mobiles/${route.params.id}`, {
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
    mobile.value = data.mobile;

  } catch (error) {
    console.error('Error loading mobile:', error);
  }
}

// ✏️ Start editing
function startEdit() {
  originalMobile.value = { ...mobile.value }; // clone
  isEditing.value = true;
}

// ❌ Cancel edit
function cancelEdit() {
  mobile.value = { ...originalMobile.value };
  isEditing.value = false;
}

// ✅ Update mobile
async function updateMobile() {
  try {
    const response = await fetch(`http://localhost:5000/mobiles/${mobile.value.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      body: JSON.stringify(mobile.value)
    });

    const data = await response.json();

    if (response.status === 200) {
      alert('Mobile updated successfully!');
      mobile.value = data.mobile;
      isEditing.value = false;
    } else {
      alert(data.message || 'Update failed');
    }

  } catch (error) {
    console.error('Update error:', error);
  }
}

// 🗑 Delete mobile
async function deleteMobile() {
  const confirmDelete = confirm('Are you sure you want to delete this mobile?');
  if (!confirmDelete) return;

  try {
    const response = await fetch(`http://localhost:5000/mobiles/${mobile.value.id}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    });

    const data = await response.json();

    if (response.status === 200) {
      alert('Mobile deleted successfully!');
    //   window.location.href = '/admin/mobiles';
        window.location.href = '/admin/';
    } else {
      alert(data.message || 'Delete failed');
    }

  } catch (error) {
    console.error('Delete error:', error);
  }
}
</script>

<style>
.container {
  max-width: 500px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}

.title {
  text-align: center;
  margin-bottom: 20px;
}

.card {
  background: #f9f9f9;
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.name {
  margin-bottom: 15px;
  color: #333;
}

.details p {
  margin: 8px 0;
  font-size: 16px;
}

.price {
  margin-top: 15px;
  font-size: 20px;
  font-weight: bold;
  color: #2e7d32;
}

.badge {
  background: #e0e0e0;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 14px;
}

.actions {
  margin-top: 15px;
  display: flex;
  gap: 10px;
}

button {
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.edit {
  background: #1976d2;
  color: white;
}

.delete {
  background: #d32f2f;
  color: white;
}

.edit-form {
  background: #fff3e0;
  padding: 20px;
  border-radius: 12px;
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.edit-form input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 6px;
}

.loading {
  text-align: center;
  color: gray;
}
</style>