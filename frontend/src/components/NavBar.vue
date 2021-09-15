<template>
    <div class="navbar-container">
        <label>Feedback</label>
    </div>
</template>

<script>
export default {
    name: 'NavBar',
}
</script>

<style scoped>
/*
#D0A85C pastel
#0BC6E3  blue
#111111  black 
*/

.navbar-container {
    position: absolute;
    transition: 0.3s;
    left: -80px;
    padding: 15px;
    width: 15vh;
    height: 100%;
    text-decoration: none;
    font-size: 20px;
    color: white;
    background-color:#D0A85C;
    font-family: Helvetica;
}

.navbar-container:hover {
    left: 0;
}


</style>