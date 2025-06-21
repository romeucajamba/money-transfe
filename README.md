# 💸 Plataforma de Pagamentos Simplificada

Este projeto é uma API RESTful desenvolvida com **Django**, **Python** e **Django Ninja**, que simula um sistema de transferência de dinheiro entre dois tipos de usuários: **usuários comuns** e **lojistas**. A aplicação permite cadastro, depósito e transferências entre usuários, com validações e notificações integradas.

## 🚀 Funcionalidades

- Cadastro de usuários com dados únicos (CPF/CNPJ, e-mail)
- Dois tipos de usuários:
  - **Usuário comum**: pode enviar e receber dinheiro
  - **Lojista**: **apenas recebe** dinheiro
- Transferência de dinheiro entre usuários, com validação de saldo
- Consulta a um serviço externo para autorização de transferências
- Envio de notificação de pagamento via serviço de terceiros
- Operações feitas em **transações atômicas**
- API RESTful para integração com clientes

## 🛠 Tecnologias Utilizadas

- Python 3.10+
- Django 4.x
- Django Ninja (FastAPI-like para Django)
- SQLite (ou qualquer outro banco suportado pelo Django)
- Requests (para chamadas HTTP externas)

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/romeucajamba/money-transfe.git
   cd money-transfe

2. Cria ambiente virtual
```bash
python -m venv env
source env/bin/activate  # No Windows: env\Scripts\activate
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Aplique as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```
📌 Endpoints Principais
A documentação da API é gerada automaticamente em:
http://localhost:8000/api/docs

Exemplos de rotas:
POST /api/users/ – Cadastro de usuário

POST /api/deposit/ – Depositar valores na conta do usuário

POST /api/transfer/ – Realizar transferência de dinheiro

GET /api/wallets/{user_id}/ – Ver saldo da carteira

✅ Regras de Negócio
CPF/CNPJ e e-mail devem ser únicos no sistema

Lojistas não podem transferir dinheiro

Toda transferência:

Valida se o remetente tem saldo

Consulta serviço de autorização externa:

https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc

Notifica o destinatário via serviço externo (simulado):

https://run.mocky.io/v3/54dc2cf1-3add-45b5-b5a9-6bf7e7f1f4a6

É feita dentro de uma transação atômica: falhas revertem a operação

📂 Estrutura do Projeto

.
├── core/                   # Lógica de negócio
├── users/                  # Cadastro e autenticação de usuários
├── transactions/           # Transferências e validações
├── manage.py
└── requirements.txt

⚠️ Tratamento de Erros
Retorno de erros padronizados para:

Saldo insuficiente

Tentativa de transferência por lojista

CPF/CNPJ ou e-mail duplicado

Falha no serviço autorizador externo

Falha no envio de notificação (sem afetar a transação)

🧑‍💻 Autor
Projeto desenvolvido por [Seu Nome] – contato: [seu-email@email.com]


Acessar http://localhost:8000/api/docs para visualizar e testar as rotas
