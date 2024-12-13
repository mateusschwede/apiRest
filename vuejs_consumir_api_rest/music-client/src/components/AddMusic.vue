<template>
    <div>
        <h2>Adicionar Música</h2>
        <form @submit.prevent="addMusic">
            <input v-model="title" placeholder="Título" required />
            <input v-model="artist" placeholder="Artista" required />
            <button type="submit">Adicionar</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            title: '',
            artist: '',
        };
    },
    methods: {
        async addMusic() {
            await this.$axios.post('http://localhost:8000/api/musics/', {
                title: this.title,
                artist: this.artist,
            });
            this.$emit('music-added');
            this.title = '';
            this.artist = '';
        },
    },
};
</script>