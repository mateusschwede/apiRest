<template>
    <div class="confirm-dialog">
        <p>{{ message }}</p>
        <button @click="$emit('confirm')">Sim</button>
        <button @click="$emit('cancel')">Não</button>
    </div>
</template>

<script>
export default {
    props: ['message'],
};
</script>