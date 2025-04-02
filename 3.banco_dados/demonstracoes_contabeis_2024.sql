use demonstracoes;

CREATE TABLE demonstracoes_contabeis_2024 (
    DATA DATE,
    REG_ANS VARCHAR(255),
    CD_CONTA_CONTABIL VARCHAR(255),
    DESCRICAO TEXT,
    VL_SALDO_INICIAL VARCHAR(100),
    VL_SALDO_FINAL VARCHAR(100)
);

SHOW VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = 1;

-- Importação dos dados dos arquivos .csv baixados para a tabela
LOAD DATA INFILE 'C:/Caminho/do/arquivo/1T2024.csv' -- Necessário alterar para o local em que se encontra o arquivo !
INTO TABLE demonstracoes_contabeis_2024
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;  -- Ignora o cabeçalho

LOAD DATA INFILE 'C:/Caminho/do/arquivo/2T2024.csv' -- Necessário alterar para o local em que se encontra o arquivo !
INTO TABLE demonstracoes_contabeis_2024
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Caminho/do/arquivo/3T2024.csv' -- Necessário alterar para o local em que se encontra o arquivo !
INTO TABLE demonstracoes_contabeis_2024
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'C:/Caminho/do/arquivo/4T2024.csv' -- Necessário alterar para o local em que se encontra o arquivo !
INTO TABLE demonstracoes_contabeis_2024
FIELDS TERMINATED BY ';' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Mostra todos os resultados dos arquivos de 2024
SELECT * FROM demonstracoes_contabeis_2024;