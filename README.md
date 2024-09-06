API Lacrei Saúde - Gerenciamento de Consultas Médicas

1. Introdução

Este projeto é uma API para gerenciar profissionais de saúde e consultas médicas. Ele foi desenvolvido em Python utilizando o framework Django e Django Rest Framework. A API permite o cadastro, edição, visualização e exclusão de profissionais de saúde e consultas, bem como a busca de consultas por profissional.

2. Tecnologias Utilizadas

    Python: Linguagem de programação utilizada no backend.
    Django: Framework web utilizado para gerenciar o backend e os modelos de dados.
    Django Rest Framework (DRF): Ferramenta usada para facilitar a criação de APIs RESTful.
    SQLite: Banco de dados padrão utilizado para desenvolvimento e testes.

3. Requisitos do Sistema

    Python 3.7 ou superior
    pip (gerenciador de pacotes do Python)
    Virtualenv (para isolamento do ambiente de desenvolvimento)

4. Configuração do Ambiente Virtual

Siga as etapas abaixo para configurar o ambiente virtual e rodar a aplicação:

4.1. Clonar o Repositório

Primeiro, clone o repositório do projeto para o seu ambiente local:
    git clone https://github.com/LhamCode/Lacrei_Saude.git
    cd Lacrei_Saude_Backend

4.2. Criar e Ativar o Ambiente Virtual
    Linux/macOS:
        python3 -m venv backend
        source backend/bin/activate
    
    Windows:
        python -m venv backend
        .\backend\Scripts\activate

4.3. Instalar as Dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

    pip install -r requirements.txt

4.4. Aplicar Migrações

Após instalar as dependências, aplique as migrações para criar as tabelas no banco de dados:

    python manage.py migrate

4.5. Rodar o Servidor de Desenvolvimento

Agora você pode rodar o servidor de desenvolvimento do Django:
    python manage.py runserver

5. Endpoints Principais da API
Profissionais

    GET /api/profissionais/: Lista todos os profissionais cadastrados.
    POST /api/profissionais/: Cadastra um novo profissional.
    GET /api/profissionais/{id}/: Retorna os detalhes de um profissional específico.
    PUT /api/profissionais/{id}/: Atualiza os dados de um profissional.
    DELETE /api/profissionais/{id}/: Deleta um profissional.

Consultas

    GET /api/consultas/: Lista todas as consultas cadastradas.
    POST /api/consultas/: Cadastra uma nova consulta.
    GET /api/consultas/{id}/: Retorna os detalhes de uma consulta específica.
    PUT /api/consultas/{id}/: Atualiza os dados de uma consulta.
    DELETE /api/consultas/{id}/: Deleta uma consulta.

Busca de Consultas por Profissional

    GET /api/consultas/?profissional_id={id}: Retorna todas as consultas vinculadas a um profissional específico.

6. Validações e Sanitização de Inputs
Sanitização

Para garantir a segurança da API e evitar ataques de injeção de código, os inputs dos usuários são sanitizados. Por exemplo, o campo de contato é validado para garantir que ele contenha apenas números.

No serializers.py:

    class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

    def validate_contato(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("O campo contato deve conter apenas números.")
        if len(value) != 11:  # Verifica se o contato tem o formato correto
            raise serializers.ValidationError("O campo contato deve conter 11 dígitos.")
        return value
Validações de Segurança

Para melhorar a segurança da aplicação, foram implementadas as seguintes medidas:

    Validação de formatos de dados: Todos os campos recebem validações para garantir que os dados inseridos estejam no formato correto (por exemplo, número de telefone).
    Proteção contra XSS e injeção de código: Os dados de entrada são sanitizados para evitar injeções maliciosas. Bibliotecas como bleach podem ser usadas para garantir que o input HTML seja seguro.
    Uso de permissões de acesso: A API foi configurada para restringir acesso apenas a usuários autenticados, garantindo que operações sensíveis como criação, edição e exclusão de dados estejam protegidas.

7. Testes Unitários

Os testes foram implementados para garantir o bom funcionamento da API. Para rodar os testes, execute o seguinte comando:

python manage.py test

8. Escolhas de Arquitetura
Django e Django Rest Framework

Escolhi o Django como framework para este projeto por ser robusto, escalável e já possuir um sistema de administração pronto, o que facilita o gerenciamento dos dados. O Django Rest Framework foi utilizado para facilitar a criação das APIs RESTful, permitindo um desenvolvimento mais rápido e estruturado.
Modelos de Dados

    Profissional: Armazena os dados dos profissionais de saúde, como nome, nome social, profissão, endereço e contato.
    Consulta: Relaciona uma consulta a um profissional e armazena a data da consulta.

A API foi projetada para ser escalável e modular, permitindo fácil expansão e manutenção futura.