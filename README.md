# restapi-flask
Objetivos do projeto:

1. Construir uma REST API com três rotas (endpoints):
    1. /users para retornar todos os usuários (GET)
    2. /user/<cpf> para retornar um usuário específico (GET)
    3. /user para registrar um novo usuário (POST)

2. Persistir dados em um Banco de Dados.

3. Configurar a aplicação para rodar dentro de um Docker container (Dockerfile).

4. Criar um docker-compose para compor a API juntamente com o banco de dados (ambiente de desenvolvimento).

5. Escrever testes unitários para as rotas.

6. Utilizar um Makefile para automatizar os passos mais comuns.

7. Fazer o deploy da aplicação em alguma plataforma de PaaS (Heroku).

8. Criar uma pipeline de CI/CD utilizando alguma ferramenta “as a service” (GitHub Actions, Azure DevOps, etc…).

Importante instalar:

- Docker
- Python