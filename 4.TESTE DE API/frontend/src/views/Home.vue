<template>
    <div>
      <h1>Buscar Operadoras</h1>
      <SearchBar @search="fetchResults" />
      <ResultsList :results="results" />
    </div>
  </template>
  
  <script>
  import SearchBar from "@/components/SearchBar.vue";
  import ResultsList from "@/components/ResultsList.vue";
  import api from "@/api.js";
  
  export default {
    components: { SearchBar, ResultsList },
    data() {
      return {
        results: []
      };
    },
    methods: {
      async fetchResults(query) {
        if (query.length > 2) {
          try {
            const response = await api.get(`/buscar?query=${query}`);
            this.results = response.data;
          } catch (error) {
            console.error("Erro ao buscar operadoras:", error);
          }
        } else {
          this.results = [];
        }
      }
    }
  };
  </script>
  