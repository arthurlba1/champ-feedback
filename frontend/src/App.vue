<template>
  <div id="app">
    
    <form action="">
      <div class="row g-3">
        <div class="col">
          <input type="text" class="form-control" placeholder="Name">
        </div>
        <div class="col">
          <input type="text" class="form-control" placeholder="Rating">
        </div>
        <div class="col">
          <input type="text" class="form-control col-3 mx-0" placeholder="Comment">
        </div>
        <div class="col">
          <button class="btn btn-success">Submit</button>
        </div>
      </div>
    </form>
    
    <table class="table">
        <thead>
           <th>Name</th>
           <th>Rating</th>
           <th>Comment</th>
        </thead>
        <tbody>
          <tr v-for="champ in champs" :key="champ.id">
            <th>{{ champ.name }}</th>
            <th>{{ champ.rating }}</th>
            <th>{{ champ.comment }}</th>
          </tr>
        </tbody>
    </table>

  </div>
</template>

<script>


export default {
  name: 'App',
    data(){
      return {
        champs: []
      }
    },
    async created(){
      var response = await fetch('http://127.0.0.1:8000/api/feedbackChamp/');
      this.champs = await response.json();
    }
  }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
