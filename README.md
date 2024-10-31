# Gerenciador de Tarefas / Task Manager

Este é um aplicativo simples de gerenciamento de tarefas desenvolvido com Flask. Ele permite que os usuários criem, leiam, atualizem e excluam tarefas.

## Funcionalidades

- **Listar Tarefas**: Retorna uma lista de todas as tarefas.
- **Criar Tarefa**: Permite a criação de uma nova tarefa.
- **Atualizar Tarefa**: Permite a atualização de uma tarefa existente.
- **Excluir Tarefa**: Permite a exclusão de uma tarefa existente.

## Endpoints

### `GET /tasks`

Retorna a lista de todas as tarefas.

**Retorno**: Uma lista de tarefas em formato JSON.

### `POST /tasks`

Cria uma nova tarefa a partir dos dados enviados no corpo da requisição.

**Requisição**: JSON contendo os dados da tarefa.

**Retorno**: A tarefa criada em formato JSON.

**Status Code**: 201 se a tarefa for criada com sucesso.

### `PUT /tasks/<task_id>`

Atualiza uma tarefa existente com base no ID fornecido.

**Parâmetros**:
- `task_id` (int): O ID da tarefa a ser atualizada.

**Retorno**: A tarefa atualizada em formato JSON, ou um erro se a tarefa não for encontrada.

**Status Code**: 404 se a tarefa não for encontrada.

### `DELETE /tasks/<task_id>`

Remove uma tarefa com base no ID fornecido.

**Parâmetros**:
- `task_id` (int): O ID da tarefa a ser removida.

**Retorno**: A tarefa removida em formato JSON, ou um erro se a tarefa não for encontrada.

**Status Code**: 404 se a tarefa não for encontrada.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu_usuario/gerenciador-de-tarefas.git
   cd gerenciador-de-tarefas

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/dann17dev/task_manager.git
   cd task_manager