<template>

    <div>
      <h2>Resultados</h2>
      <ul>
        <!-- <li v-for="result in results" :key="result.id">
          {{ result.nome }} - {{ result.regiao }}
        </li> -->
        <li v-for="operadora in results" :key="operadora.CNPJ">
        <strong>{{ operadora["Razao_Social"] }}</strong> ({{ operadora["UF"] }}) <br />
        <span>Cidade: {{ operadora["Cidade"] }}</span> <br />
        <span>Bairro: {{ operadora["Bairro"] }}</span> <br />
        <span>Telefone: {{ operadora["DDD"] }} - {{ operadora["Telefone"] }}</span> <br />
        <hr />
      </li>
      </ul>
    </div>
  </template>
  
  <script>
    export default {
        props: {
        results: Array
        }
  };
  </script>
  