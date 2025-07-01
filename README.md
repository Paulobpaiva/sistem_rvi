# Sistema de Gerenciamento de Estacionamento

Sistema web para gerenciamento de veículos, motoristas e solicitações de uso de veículos.

## Requisitos

- Python 3.8+
- PostgreSQL
- pip

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   ```bash
   venv\Scripts\activate
   ```
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure o banco de dados PostgreSQL:
   - Crie um novo banco de dados
   - Atualize as credenciais no arquivo `sistema_estacionamento/settings.py`
6. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
7. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
8. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Funcionalidades

- Autenticação de usuários
- Cadastro e gestão de motoristas
- Cadastro e gestão de veículos
- Gestão de horários disponíveis
- Sistema de solicitações de veículos
- Dashboard administrativo
- Relatórios e estatísticas

## Estrutura do Projeto

- `motoristas/`: Aplicação para gestão de motoristas
- `veiculos/`: Aplicação para gestão de veículos
- `solicitacoes/`: Aplicação para gestão de solicitações e horários
- `sistema_estacionamento/`: Configurações do projeto

## API Endpoints

- `/api/horarios-disponiveis/`: Lista e criação de horários disponíveis
- `/api/solicitacoes/`: Lista e criação de solicitações

## Configuração do Banco de Dados

O sistema utiliza PostgreSQL como banco de dados. Certifique-se de criar um banco de dados PostgreSQL antes de executar as migrações.

## Segurança

- Autenticação obrigatória para todas as operações
- Permissões baseadas em grupos de usuários
- Validações de dados em nível de modelo
- Proteção contra CSRF e XSS
