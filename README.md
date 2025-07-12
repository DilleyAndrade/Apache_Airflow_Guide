
# 🌬️ Apache Airflow - Repositório de Estudos

Este repositório contém DAGs desenvolvidas durante meus estudos em Apache Airflow. A intenção é consolidar o aprendizado por meio da prática, servindo como material de revisão e consulta.

## 🧠 Tópicos Estudados

As DAGs abordam diversos recursos e funcionalidades do Airflow, incluindo:

- BashOperator
- Conceitos de paralelismo, precedência e upstream
- Trigger Rules (OneFailed, AllFailed)
- Task Groups
- Operators: EmailOperator, EmptyOperator, PythonOperator, BranchPythonOperator
- Variáveis, Pools e Providers
- Hooks e XComs
- Criação de plugins personalizados
- Processamento de dados com arquivos CSV
- Pipeline de consumo e produção

## 📁 Estrutura do Projeto

```
.
├── dags/
│   ├── 1-BashOperator.py
│   ├── 2-Paralelismo.py
│   ├── 3-Precedencia.py
│   └── ...
├── data/
│   └── Churn.csv
├── plugins/
│   └── big_data_operator.py
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

## ▶️ Como Executar o Projeto (via Docker)

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/airflow-curso.git
cd Apache_Airflow_Guide
```

2. Execute com Docker Compose:
```bash
docker-compose up -d
```

3. Acesse a interface web do Airflow:
```
http://localhost:8080
```
- **Usuário:** airflow  
- **Senha:** airflow

## 📌 Requisitos

- Docker e Docker Compose instalados
- Python 3.7+
- Requisitos adicionais estão no `requirements.txt`

## 📎 Referências

- [Documentação oficial do Apache Airflow](https://airflow.apache.org/)

## 📄 Licença

Este projeto está licenciado sob a licença MIT.


Dilley Andrade | Data engineer
(81) 98663-2609 | dilleyandrade@gmail.com | linkedin.com/in/dilleyandrade | github.com/DilleyAndrade


