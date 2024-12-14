<template>
    <div>
        <h1>Lista de Músicas</h1>

        <div v-if="activeForm === null">
            <button @click="showForm('add')">Adicionar Música</button>
        </div>

        <AddMusic v-if="activeForm === 'add'" @music-added="onMusicAdded" @close="closeForm" @cancel="closeForm" />

        <EditMusic v-if="activeForm === 'edit'" :music="editingMusic" @updated="onMusicUpdated" @cancel="closeForm" />

        <ul>
            <li v-for="music in musics" :key="music.id">
                {{ music.title }} - {{ music.artist }}
                <button @click="editMusic(music)">Editar</button>
                <button @click="confirmDelete(music.id)">Excluir</button>
            </li>
        </ul>

        <ConfirmDialog v-if="showConfirmDialog" :message="'Deseja realmente excluir esta música?'"
            @confirm="deleteMusic" @cancel="closeConfirmDialog" />
    </div>
</template>

<script>
import AddMusic from './AddMusic.vue';
import EditMusic from './EditMusic.vue';
import ConfirmDialog from './ConfirmDialog.vue';

export default {
    components: { AddMusic, EditMusic, ConfirmDialog },
    data() {
        return {
            musics: [],
            showConfirmDialog: false,
            musicToDelete: null,
            editingMusic: null,
            activeForm: null,
        };
    },
    methods: {
        async fetchMusics() {
            try {
                const response = await this.$axios.get('http://localhost:8000/api/musics/');
                this.musics = response.data;
            } catch (error) {
                console.error('Erro ao buscar músicas:', error);
            }
        },
        showForm(formType) {
            this.activeForm = formType;
            this.closeConfirmDialog();
        },
        closeForm() {
            this.activeForm = null;
            this.editingMusic = null;
        },
        editMusic(music) {
            this.editingMusic = { ...music };
            this.showForm('edit');
        },
        onMusicUpdated() {
            this.closeForm();
            this.fetchMusics();
        },
        onMusicAdded() {
            this.closeForm();
            this.fetchMusics();
        },
        confirmDelete(id) {
            this.closeForm();
            this.musicToDelete = id;
            this.showConfirmDialog = true;
        },
        async deleteMusic() {
            try {
                await this.$axios.delete(`http://localhost:8000/api/musics/${this.musicToDelete}/`);
                this.fetchMusics();
                this.closeConfirmDialog();
            } catch (error) {
                console.error('Erro ao excluir música:', error);
            }
        },
        closeConfirmDialog() {
            this.showConfirmDialog = false;
            this.musicToDelete = null;
        },
    },
    created() {
        this.fetchMusics();
    },
};
</script>