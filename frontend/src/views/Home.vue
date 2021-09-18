<template>
    <div id=home-container>
        <NavBar/>
        <div>
            <h1>About us</h1>
            <p>Project made to learn two great frameworks that are very used, vue, which was used for the project's
                frontend, and django, used in the project's backend along with its database, dbsqlite3. 
                The project idea is a web page to view and send feedback on league of legends champions.</p>
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
    h1 {
        position: absolute;
        width: 25%;
        right: 20%;
        top: 22%;
        font-size: 10vh;
        text-align: left;
        color: #95b8e5;
    }
    p {
        position: absolute;
        width: 25%;
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
</style>