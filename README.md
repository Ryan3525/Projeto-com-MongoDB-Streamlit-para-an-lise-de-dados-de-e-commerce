# Projeto com MongoDB Streamlit para analise de dados de e-commerce

## 1. Introdução

A **E-Shop Brasil** é uma das maiores plataformas de comércio eletrônico do país, com mais de 5 milhões de clientes ativos e cerca de 100 mil pedidos processados diariamente. Com o crescimento acelerado, a empresa enfrenta desafios nas áreas de **gestão de dados**, **personalização da experiência do cliente** e **otimização logística**.

Este projeto tem como objetivo apresentar uma solução prática e escalável utilizando **tecnologias modernas de banco de dados** (SQL, NoSQL) e **Big Data**, simulando uma aplicação real por meio de um ambiente Docker e interface visual com Streamlit.

---

## 2. Objetivos

- Garantir a **segurança e a privacidade dos dados** dos clientes, atendendo à LGPD.
- Melhorar a **experiência do usuário** com **recomendações personalizadas**.
- Otimizar a **logística de entrega e controle de estoque** com dados integrados.
- Propor uma solução **escalável e de fácil integração** com outras tecnologias.

---

## 3. Descrição do Problema

A E-Shop Brasil precisa resolver dois grandes desafios:

### ➤ Gestão de Dados

- **Segurança e privacidade:** Necessidade de proteger dados sensíveis contra ataques e cumprir a LGPD.
- **Análise e personalização:** Necessita tratar grandes volumes de dados para criar experiências personalizadas.

### ➤ Otimização Logística

- **Eficiência nas entregas:** Dificuldade para gerenciar estoques e entregas, principalmente em regiões remotas.
- **Integração Omnichannel:** Falta de integração entre canais físicos e digitais, impactando a disponibilidade e agilidade.

---

## 4. Teoria na Prática

### Conceitos Aplicados:

- **Banco de Dados Relacional (SQL):** organização estruturada dos dados.
- **Banco de Dados NoSQL (MongoDB):** armazenamento de dados não estruturados de forma escalável.
- **Big Data:** uso de ferramentas como Spark e Hadoop (teoricamente neste projeto).
- **Streamlit:** framework para visualização de dados e interfaces de usuário.
- **Docker:** ambiente isolado e padronizado para fácil execução.

  ## 5. Hipóteses Levantadas

1. A ausência de um sistema de dados unificado dificulta a análise de comportamento dos clientes.
2. O uso apenas de SQL torna o sistema rígido e lento com grandes volumes de dados.
3. A falta de automação e integração entre os canais limita a capacidade de resposta logística.

---

## 6. Solução Proposta

A melhor solução foi:

### Utilizar um banco NoSQL (MongoDB) integrado a uma aplicação em Streamlit via Docker

**Por que essa solução?**

- MongoDB permite **flexibilidade e escalabilidade** com dados não estruturados.
- Streamlit permite **interface simples para manipulação dos dados**.
- Docker facilita o **ambiente isolado, portátil e pronto para produção**.

Outras soluções avaliadas:

| Solução | Prós | Contras |
|--------|------|---------|
| ERP completo | Integra tudo | Alto custo |
| SQL puro | Segurança e robustez | Baixa escalabilidade |
| Big Data puro | Alta performance | Complexidade e custo |

---

## 7. Plano de Ação

### Etapas:

1. **Montar ambiente com Docker + MongoDB**
2. **Desenvolver aplicação com Streamlit**
3. **Implementar inserção, leitura, edição, exclusão e concatenação de dados**
4. **Simular fluxo com dados reais ou sintéticos**
5. **Documentar e disponibilizar no GitHub**

---

## 8. Tecnologias Utilizadas

- Docker
- MongoDB
- Python 3.10+
- Streamlit
- Pandas
