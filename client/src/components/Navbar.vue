<script setup lang="ts">
import { RouterLink } from "vue-router";
</script>

<template>
  <!-- Top Bar Start -->
  <div class="top-bar">
    <div class="container">
      <div class="contact-info">
        <span>
          <font-awesome-icon icon="fa-solid fa-phone" class="nav-icon" />
          +998930850955
        </span>
        <span>
          <font-awesome-icon icon="fa-solid fa-envelope" class="nav-icon" />
          umidgaybullayev955@gmail.com
        </span>
      </div>

      <div class="location">
        <font-awesome-icon icon="fa-solid fa-location-dot" />
        Uzbekistan, Navai, Karmana
      </div>
    </div>
  </div>
  <!-- Top Bar End -->

  <!-- Navbar Start -->
  <nav>
    <ul>
      <li><RouterLink to="/">Home</RouterLink></li>
      <li><RouterLink to="/about">About</RouterLink></li>
      <li><RouterLink to="/quiz">Quiz</RouterLink></li>
      <li><RouterLink to="/dashboard">Dashboard</RouterLink></li>
    </ul>
  </nav>
  <!-- Navbar End -->
</template>

<style scoped>
.top-bar {
  background: #ee2c3c;
  padding: 0 40px;
}

.top-bar .container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  color: #fff;
}

.top-bar .container .contact-info {
  display: flex;
  align-items: center;
  gap: 30px;
}

.top-bar .container .contact-info span {
  display: flex;
  align-items: center;
  gap: 5px;
}

.top-bar .container .contact-info span .nav-icon {
  font-size: 18px;
}
</style>
