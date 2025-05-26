-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 26/05/2025 às 20:19
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sistemanutri`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cad_consultas`
--

CREATE TABLE `cad_consultas` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `data_consulta` date DEFAULT NULL,
  `hora` varchar(100) DEFAULT NULL,
  `anot` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cad_consultas`
--

INSERT INTO `cad_consultas` (`id`, `nome`, `data_consulta`, `hora`, `anot`) VALUES
(2, 'Daniel', '0000-00-00', '10:00', 'Nada');

-- --------------------------------------------------------

--
-- Estrutura para tabela `cad_pacientes`
--

CREATE TABLE `cad_pacientes` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) DEFAULT NULL,
  `idade` int(11) DEFAULT NULL,
  `sexo` varchar(255) DEFAULT NULL,
  `peso` float DEFAULT NULL,
  `altura` float DEFAULT NULL,
  `histmedi` varchar(255) DEFAULT NULL,
  `alergias` varchar(255) DEFAULT NULL,
  `imc` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cad_pacientes`
--

INSERT INTO `cad_pacientes` (`id`, `nome`, `idade`, `sexo`, `peso`, `altura`, `histmedi`, `alergias`, `imc`) VALUES
(7, 'Daniel', 16, 'masc', 50, 0, 'nada', 'nada', 0),
(8, 'Daniel Próspero de Figueiredo', 16, 'Masculino', 50, 170, 'nada', 'nada', 123);

-- --------------------------------------------------------

--
-- Estrutura para tabela `contr_dietas`
--

CREATE TABLE `contr_dietas` (
  `id` int(11) NOT NULL,
  `paciente` varchar(255) DEFAULT NULL,
  `planoAlimen` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `contr_dietas`
--

INSERT INTO `contr_dietas` (`id`, `paciente`, `planoAlimen`) VALUES
(1, 'Daniel', 'Nada'),
(2, 'Daniel', 'Nada');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cad_consultas`
--
ALTER TABLE `cad_consultas`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `cad_pacientes`
--
ALTER TABLE `cad_pacientes`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `contr_dietas`
--
ALTER TABLE `contr_dietas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cad_consultas`
--
ALTER TABLE `cad_consultas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `cad_pacientes`
--
ALTER TABLE `cad_pacientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `contr_dietas`
--
ALTER TABLE `contr_dietas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
