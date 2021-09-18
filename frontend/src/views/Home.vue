<template>
    <div id=home-container>
        <NavBar/>
        <div>
            <h1>About us</h1>
            <p>Project made to learn two great frameworks that are very used, vue, which was used for the project's
                frontend, and django, used in the project's backend along with its database, dbsqlite3. 
                The project idea is a web page to view and send feedback on league of legends champions.</p>
                <button>Feedback</button>
        </div>
        <div id="home-background-gradient"/>     
        <div id="image-home"/>
        <div id="image-effect-right"/>
        <div id="image-effect-left"/>
    </div>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
    name: 'app',
    components: {
        NavBar
    },
}
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather+Sans:wght@300&display=swap%27');

    h1 {
        font-family: 'Merriweather Sans', sans-serif;
        position: absolute;
        width: 20%;
        right: 20%;
        top: 22%;
        font-size: 10vh;
        text-align: left;
        color: #95b8e5;
    }
    p {
        font-family: 'Merriweather Sans', sans-serif;
        position: absolute;
        width: 20%;
        right: 20%;
        top: 32%;
        font-size: 120%;
        text-align: left;
        padding-top: 3vh;
        color: #599df7;
    }
    #home-background-gradient{
        height: 100vh;
        background-image: linear-gradient(to right top, #181037, #18153e, #181b45, #18204c, #162653, #152a59, #142d5f, #123165, #11346c, #103873, #0e3b7a, #0c3f81);
        position: absolute;
        height: 100%;
        width: 100%;
        z-index: -5;
    }
    #home-container{
        overflow: hidden;
    }
    #image-home{
        background-image: url('C:/Users/arthu/OneDrive/Documents/Arthur/Projects/champ-feedback/frontend/src/assets/project-ashe-home-image.png');
        background-repeat: no-repeat;
        background-position: 100% 103%;
        background-size: 135vh;
        height: 100%;
        width: 100%;
        position: absolute;
        z-index: 0;
        opacity: 60%;
        transform: scaleX(-1)
    }
    #image-effect-right{
        position: absolute;
        background-image: url('C:/Users/arthu/OneDrive/Documents/Arthur/Projects/champ-feedback/frontend/src/assets/oct-right.png');
        z-index: -1;
        right: 0%;
        top: 0%;
        height: 100%;
        width: 100%;
        background-size: 135vh;
        background-position: 100% 85%;
        background-repeat: no-repeat;
        opacity: 12%;

    }
    #image-effect-left{
        position: absolute;
        background-image: url('C:/Users/arthu/OneDrive/Documents/Arthur/Projects/champ-feedback/frontend/src/assets/oct-left.png');
        z-index: -1;
        left: 0%;
        bottom: 0%;
        height: 100%;
        width: 100%;
        background-size: 135vh;
        background-position: -3% 85%;
        background-repeat: no-repeat;
        opacity: 9%;
    }
    button {
    font-family: 'Merriweather Sans', sans-serif;
    position: absolute;
    border: 0;
    color: #bddaff;
    background-image: linear-gradient(to right top, #44258b, #403294, #3c3e9c, #3949a4, #3653ab, #3355a9, #3156a8, #2f58a6, #2a519d, #254b93, #20448a, #1a3e81);
    font-weight: bold;
    font-size: 16px;
    border-radius: 4vh;
    margin-top: 20px;
    transition: 0.3s;
    height: 7%;
    width: 35vh;
    right: 24%;
    top: 55%;
    }

    button:hover {
        opacity: 0.8;
        color: #ffffff;
    }
</style>