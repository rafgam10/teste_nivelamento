-- Consulta referente as 10 operadoras com maiores despesas no último ano
SELECT 
    REG_ANS AS operadora,
    DESCRICAO,
    DATA,
    SUM(CAST(REPLACE(VL_SALDO_FINAL, ',', '.') AS DECIMAL(18,2))) AS total_despesas -- Conversão dos valores para decimal
FROM demonstracoes_contabeis_2023
WHERE 
    DESCRICAO LIKE '%SINISTROS%' '%MEDICO HOSPITALAR%' -- Filtra pelas operadoras com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
    AND DATA >= (SELECT MAX(DATA) FROM demonstracoes_contabeis_2023) - INTERVAL 1 YEAR -- Aplica o intervalo de 1 ano
GROUP BY REG_ANS, DESCRICAO, DATA
ORDER BY total_despesas DESC
LIMIT 10;