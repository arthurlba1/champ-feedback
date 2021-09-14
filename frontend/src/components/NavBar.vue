<template>
    <div class="navbar-container">
        <h1>{{msg}}</h1>
    </div>
</template>

<script>
export default {
    name: 'NavBar',
    props: {
        msg: String
    }
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
    width: 12vh;
    text-decoration: none;
    font-size: 20px;
    color: white;
    background-color:#111111;
}

.navbar-container:hover {
    left: 0;
}


</style>