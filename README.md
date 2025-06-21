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


