# Personal Knowledge Wiki

Welcome to my Personal Knowledge Wiki! This wiki serves as a repository for the knowledge I have accumulated over time, covering a wide range of topics that interest me. It is a living document, continuously updated as I learn and discover new things.

## Table of Contents

- [Personal Knowledge Wiki](#personal-knowledge-wiki)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Structure](#structure)
    - [Courses](#courses)
    - [Artifacts](#artifacts)
    - [Questions](#questions)
  - [Environment](#environment)

## Introduction

This wiki is designed to be a comprehensive and organized collection of information that I have found valuable. It includes summaries, explanations, and insights on various subjects, providing a resource for quick reference and in-depth study.

## Purpose

The primary purposes of this wiki are:

- To consolidate and organize my personal knowledge in one place.
- To facilitate easy access and retrieval of information.
- To share knowledge with others who may find it useful.
- To document learning progress and milestones.

## Structure

The wiki is divided into several main categories, each containing related topics. Below is a summary of the main course topics and their subtopics:

### Courses

**Microsoft Power BI for Business Intelligence and Data Science** (`courses/microsoft_power_bi_for_business_intelligence_and_data_science/`)
  - Concepts, tools, and best practices for Power BI in business intelligence and data science.

**Data Engineering Fundamentals** (`courses/data_engineering_fundamentals/`)
  - Core principles and foundational knowledge for data engineering.

**Formação Engenheiro de Dados (Data Engineer Formation)** (`courses/data_engineer_formation/`)
  - **Infrastructure as Code** (`iac_terraform_aws_azure_databricks/`) — Terraform, AWS, Azure and Databricks notes.
  - **Data Warehouse Modeling, Implementation, and Governance** (`modeling_implementation_governance_data_warehouses/`) — migration strategies, backup & disaster recovery, reverse ETL.
  - **Data Engineering: Airbyte, DBT and SQL** (`data_engineering_airbyte_dbt_sql/`) — cursors, primary keys in incremental sync, and data movement best practices.
  - **SQL para Análise de Dados** (`sql_analise_dados/`) — SQL fundamentals and analysis techniques.
  - **Cursos de Aperfeiçoamento Profissional / Personal Improvement Bonus** (`personal_improvement_bonus/`) — soft skills, career transition, study strategies, web scraping (Selenium, Beautiful Soup), and other career-development notes.

Each subdirectory holds dated, sequentially numbered markdown notes (e.g. `NN_<prefix>_DDMMYYYY.md`), making it easy to follow the chronological progression of each course. See the `courses/` directory for detailed notes and the latest updates.

### Artifacts

The `artifacts/` directory holds supporting diagrams referenced from the notes: draw.io exports (`.drawio`, `.drawio.png`) and hand-authored SVG diagrams built to match a shared visual design system (consistent color palette, shadows, and typography) for topics like the ikigai framework, career-transition planning, logical levels of change, habit layers, and knowledge-source mapping.

### Questions

The `questions/` directory contains structured question banks (e.g. `bi_powerbi.json`) used for self-testing and reviewing course material.

## Environment

A `Dockerfile` and `docker-compose.yml` are provided to spin up a Python 3.11 container with the dependencies in `requirements.txt` (LangChain and related tooling) mounted against the repository, for running notebook-based or scripted work against the notes.
