<template>
  <div id="app">
    <NavBar/>
    <GetFeedback/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import GetFeedback from './components/GetFeedback.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    GetFeedback,
  },
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
