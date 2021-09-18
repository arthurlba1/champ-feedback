<template>
    <table class="table">
        <thead>
            <th>Name</th>
            <th>Rating</th>
            <th>Comment</th>
        </thead>
        <tbody>
        <tr v-for="feedback in feedbacks" :key="feedback.id">
            <th>{{ feedback.name }}</th>
            <th>{{ feedback.rating }}</th>
            <th>{{ feedback.comment }}</th>
        </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    name: 'GetFeedback',
    data(){
        return{
            feedbacks: []
        }
    },
    async created(){
        var response = await fetch('http://127.0.0.1:8000/api/feedbackChamp/');
        this.feedbacks = await response.json();
    },
}
</script>

<style>

</style>