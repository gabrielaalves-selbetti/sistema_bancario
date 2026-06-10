# Sistema Bancário Digital — DSA Mini-Projeto 2

Projeto desenvolvido durante o curso **Fundamentos de Python** da [Data Science Academy (DSA)](https://www.datascienceacademy.com.br), no módulo de **Programação Orientada a Objetos (POO)**.

## Sobre o projeto

Aplicação de terminal que simula um sistema bancário digital com cadastro de clientes, abertura de contas e operações financeiras. O objetivo principal é aplicar na prática os pilares da POO em Python.

## Conceitos de POO aplicados

| Conceito | Onde é usado |
|---|---|
| **Abstração** | Classe `Conta` (ABC) define o contrato sem implementar `sacar` |
| **Herança** | `ContaCorrente` e `ContaPoupanca` herdam de `Conta` |
| **Polimorfismo** | Método `sacar` tem comportamentos distintos em cada subclasse |
| **Encapsulamento** | Atributos protegidos (`_saldo`, `_numero`) com acesso via `@property` |
| **Composição** | `Banco` contém clientes e contas; `Cliente` contém contas |
| **Exceções customizadas** | `SaldoInsuficienteError` e `ContaInexistenteError` herdam de `Exception` |

## Estrutura do projeto

```
base/
├── dsa_mini_projeto2.py       # Ponto de entrada e menus da aplicação
├── dsaentidades/
│   ├── cliente.py             # Classe Cliente
│   └── conta.py               # Classes Conta (abstrata), ContaCorrente e ContaPoupanca
├── dsaoperacoes/
│   └── banco.py               # Classe Banco (gerencia clientes e contas)
└── dsautilitarios/
    └── exceptions.py          # Exceções personalizadas
```

## Como executar

```bash
cd base
python dsa_mini_projeto2.py
```

## Funcionalidades

- Cadastrar clientes (nome e CPF)
- Criar contas corrente ou poupança vinculadas a um cliente
- Depositar e sacar valores
- Consultar extrato com histórico de transações
