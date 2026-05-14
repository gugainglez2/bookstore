# 📚 Bookstore API

[![Django](https://img.shields.io/badge/Django-6.0-092e20?style=for-the-badge&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.15-ff1709?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ed?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render)](https://render.com/)

API robusta para gerenciamento de livraria, desenvolvida durante o curso de Desenvolvimento Web Full Stack da EBAC. O projeto foca em boas práticas de desenvolvimento, conteinerização e entrega contínua (CI/CD).

## 🚀 Demonstração (Live)
A aplicação está hospedada no Render e pode ser acessada através do link abaixo:
- **URL Base:** [https://bookstore-ezhd.onrender.com](https://bookstore-ezhd.onrender.com)
- **Endpoints Principais:**
    - `GET /bookstore/v1/product/`
    - `GET /bookstore/v1/category/`
    - `GET /bookstore/v1/order/` (Requer Autenticação)

## 🛠️ Tecnologias Utilizadas
- **Backend:** Python 3.12 & Django 6.0
- **API:** Django REST Framework (DRF)
- **Banco de Dados:** PostgreSQL (Produção) / SQLite (Desenvolvimento)
- **Servidor de Produção:** Gunicorn & WhiteNoise (Arquivos estáticos)
- **Gerenciador de Dependências:** Poetry
- **Infraestrutura:** Docker & Docker Compose
- **Monitoramento:** Django Debug Toolbar (em modo Debug)

## 🏗️ Arquitetura e Decisões Técnicas
- **CI/CD:** Pipeline automatizada via GitHub Actions para garantir a integridade do código antes do deploy.
- **Ambiente Isolado:** Uso de Docker para garantir que o ambiente de desenvolvimento seja idêntico ao de produção.
- **Segurança:** Implementação de autenticação via **Token** para operações sensíveis.
- **Versionamento de API:** Suporte a múltiplas versões (v1/v2) via regex nas URLs.

## 📦 Como rodar o projeto localmente

### Pré-requisitos
- Docker e Docker Compose instalados.

### Passo a passo
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/gugainglez2/bookstore.git](https://github.com/gugainglez2/bookstore.git)
   cd bookstore

2. Suba os containers:
   ```bash
   docker-compose up --build

  A API estará disponível em `http://localhost:8000`.

3. **Executar Migrações (caso necessário):**
   ```bash
   docker-compose exec web python manage.py migrate

4. A API estará disponível em `http://localhost:8000`.
   ```bash
   docker-compose exec web python manage.py createsuperuser

## 📝 Documentação da API
A API segue o padrão REST. Para autenticar requisições que exigem token:
1. Obtenha seu token em `/api-token-auth/` enviando seu username e password.
2. Adicione o header: `Authorization: Token <seu_token>`.

---
Desenvolvido por **Gustavo Inglez** 🚀
