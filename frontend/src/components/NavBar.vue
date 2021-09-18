<template>
    <div class="navbar-container">
        <div class="move-navbar">
            <a href="/home">Home</a>
            <i class="menu-icon"><font-awesome-icon :icon="['fas','align-justify']"/></i>
        </div>
        <div class="send-navbar">
            <a class="send-feedback" href="#">Send</a>
            <i class="menu-icon fix"><font-awesome-icon :icon="['fas','edit']"/></i>
        </div>
        <div class="get-navbar">
            <a class="send-feedback" href="#">View</a>
            <i class="menu-icon fix"><font-awesome-icon :icon="['fas','list-alt']"/></i>
        </div>  
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

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap');

.navbar-container {
    position: absolute;
    z-index: 1;
    transition: 0.3s;
    left: -13vh;
    padding: 15px;
    width: 18vh;
    height: 100%;
    text-decoration: none;
    font-size: 20px;
    color: white;
    background-color:  rgba(37, 37, 37, 0.829);
}

.navbar-container:hover{
    left: -4vh;
    background-color: #1b1b1bb9;
}

a{
    font-family:'Quicksand', sans-serif;
    font-size: 20px;
    padding-left: 4vh;
    text-align: center;
    line-height: 1.7;
	color: #ffffff;
    margin: 0px;
	transition: all 0.4s;
	-webkit-transition: all 0.4s;
    -o-transition: all 0.4s;
    -moz-transition: all 0.4s;
    text-decoration: none;
}

a:hover{
    opacity: 40%;
}

.menu-icon{
    margin-left: 16%;
}

.move-navbar{
    transform: translate(0vh, 30px);
}

.send-navbar{
    transform: translate(0vh, 60px);
}

.get-navbar{
    transform: translate(0vh, 90px);
}

.fix {
    margin-left: 23%;
}
</style>