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
    z-index: 1;
    transition: 0.3s;
    left: -7.5vh;
    padding: 15px;
    width: 15vh;
    height: 100%;
    text-decoration: none;
    font-size: 20px;
    color: white;
    background-color:  rgba(37, 37, 37, 0.829);
    font-family: Helvetica;
}

.navbar-container:hover {
    left: 0vh;
    background-color: #1b1b1bb9;
}


</style>