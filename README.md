# Sobre
O projeto restapi-flask é uma iniciativa que visa aplicar e consolidar os conhecimentos adquiridos ao longo de estudos prévios. Buscamos não apenas praticar os conceitos aprendidos, mas também desenvolver habilidades práticas na construção e implantação de uma API REST utilizando Flask.

Este projeto representa uma oportunidade para colocar em prática os aprendizados acumulados ao longo do tempo dedicado aos estudos, visando não só a compreensão teórica, mas também a aplicação prática dos conceitos em um contexto real de desenvolvimento de software.

# Projeto-1 restapi-flask
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


# Projeto-2 restapi-flask


Seguindo a evolução natural do nosso projeto, vamos adaptar o projeto como um todo, desde o código, pipeline e deploy para rodar dentro do Kubernetes.

Cursos requisitos:

    Kubernetes: Do Básico ao Avançado (mínimo até o módulo 13).
    Terraform para AWS

Ferramentas requisitos:

    Helm
    Terraform
    Vagrant
    Ansible

PS: O projeto completo estará em anexo nesta aula quando finalizar as gravações... Ainda está em fase de gravação 🙂

Neste segundo módulo eu proponho o seguinte:

    Melhorar a API adicionando mais 2 rotas (endpoints)
        /user/<cpf> (DELETE) para deletar um usuário do banco de dados.
        /user (PATCH) para atualizar um usuário existente.
    Criar um endpoint para health check que teste efetivamente a conexão com o banco de dados. O objetivo é que o nosso pod não receba tráfego enquanto o banco não estiver respondendo.
    Adicionar novas estratégias para garantir a qualidade de código e também da perspectiva de segurança.
    Construir um cluster local (na sua própria máquina) utilizando ferramentas como Kind, Minikube, K3s.
    Criar manifestos Kubernetes para fazer o deploy da aplicação.
    Adaptar o Makefile para deployar no cluster de desenvolvimento criado no passo 2.
    Evoluir os manifestos de forma empacotada usando um Helm Chart.
    Construir um cluster EKS na AWS utilizando Terraform.
    Adaptar o Makefile para deployar no EKS.
    Criar uma estratégia de deployment com o mínimo possível de erros.
    Evoluir a pipeline no GitHub Actions adicionando os novos testes e deployando no EKS.