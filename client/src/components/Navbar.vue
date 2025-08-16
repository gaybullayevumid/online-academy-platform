<script setup lang="ts">
import { RouterLink } from 'vue-router';

</script>

<template>
<nav>
    <ul>
        <li><RouterLink to="/">Home</RouterLink></li>
        <li><RouterLink to="/courses">Courses</RouterLink></li>
        <li><RouterLink to="/quiz">Quiz</RouterLink></li>
        <li><RouterLink to="/dashboard">Dashboard</RouterLink></li>
        <!-- <li><a href=""></a></li> -->
    </ul>
</nav>
</template>