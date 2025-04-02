<template>
    <div>
      <input v-model="query" type="text" placeholder="Digite o nome da operadora" />
      <button @click="emitSearch">Buscar</button>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    setup(_, { emit }) {
      const query = ref("");
  
      const emitSearch = () => {
        emit("search", query.value);
      };
  
      return { query, emitSearch };
    }
  };
  </script>
  