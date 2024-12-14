<template>
    <div>
        <h2>Editar Música</h2>
        <form @submit.prevent="updateMusic">
            <input v-model="editedMusic.title" placeholder="Título da música" required>
            <input v-model="editedMusic.artist" placeholder="Artista" required>
            <button type="submit">Salvar</button>
            <button type="button" @click="$emit('cancel')">Cancelar</button>
        </form>
    </div>
</template>

<script>
export default {
    props: {
        music: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            editedMusic: { ...this.music },
        };
    },
    methods: {
        async updateMusic() {
            try {
                await this.$axios.put(`http://localhost:8000/api/musics/${this.editedMusic.id}/`, {
                    title: this.editedMusic.title,
                    artist: this.editedMusic.artist,
                });
                this.$emit('updated');
            } catch (error) {
                console.error('Erro ao atualizar música:', error);
            }
        },
    },
};
</script>