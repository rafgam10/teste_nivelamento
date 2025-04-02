<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <SearchBar @search="fetchResults" />
    <ResultsList :results="results" />
  </div>
</template>

<script>
import { ref } from "vue";
import SearchBar from "./components/SearchBar.vue";
import ResultsList from "./components/ResultsList.vue";
import axios from "axios";

export default {
  components: { SearchBar, ResultsList },
  setup() {
    const results = ref([]);
    const fetchResults = async (query) => {
      try { //buscar?q=419761 == //search?query
        const response = await axios.get(`http://127.0.0.1:5000/buscar?q=${query}`);
        console.log("Dados recebidos:", response.data);  // Verifica os dados recebidos
        results.value = response.data;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    };

    return { results, fetchResults };
  }
};
</script>
