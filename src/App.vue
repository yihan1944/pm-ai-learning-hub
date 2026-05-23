<script setup lang="ts">
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <main class="container" style="padding-top: calc(var(--nav-height) + 1.5rem); padding-bottom: 3rem;">
    <router-view />
  </main>
</template>
