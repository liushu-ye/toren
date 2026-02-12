<script setup lang='ts'>
    import { ref } from 'vue'

    import Avatar from '@/components/home/topnav/Avatar.vue'
    import SearchInput from '@/components/home/topnav/Searchinput.vue'
    import { useRouter } from 'vue-router'
    const router = useRouter()

    const keyword = ref('')
</script>

<template>
    <header class="flex items-center justify-between px-4 w-full">
        <div class="flex items-center justify-evenly gap-4">
            <Avatar src="https://picsum.photos/200" :size="'sm'" :is-online="true"></Avatar>
            <div>周口市</div>
            
        </div>
        <div class="flex items-center justify-evenly gap-4">
            <SearchInput v-model="keyword" />
            <div @click.stop="router.push('/setting')"><img src="@\assets\icons\assignment.svg" alt="设置"></div>
            <div @click.stop="router.push('/setting')"><img src="@\assets\icons\mail.svg" alt="设置"></div>
        </div>
    </header>
    
</template>

<style scoped>

</style>
