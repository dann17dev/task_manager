from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para armazenar as tarefas
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna a lista de todas as tarefas.

    Returns:
        JSON: Uma lista de tarefas em formato JSON.
    """
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Cria uma nova tarefa a partir dos dados enviados no corpo da requisição.

    Returns:
        JSON: A tarefa criada em formato JSON.
        status_code: 201 se a tarefa for criada com sucesso.
    """
    task = request.get_json()
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente com base no ID fornecido.

    Args:
        task_id (int): O ID da tarefa a ser atualizada.

    Returns:
        JSON: A tarefa atualizada em formato JSON, ou um erro se a tarefa não for encontrada.
        status_code: 404 se a tarefa não for encontrada.
    """
    if task_id < len(tasks):
        task = request.get_json()
        tasks[task_id] = task
        return jsonify(task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Remove uma tarefa com base no ID fornecido.

    Args:
        task_id (int): O ID da tarefa a ser removida.

    Returns:
        JSON: A tarefa removida em formato JSON, ou um erro se a tarefa não for encontrada.
        status_code: 404 se a tarefa não for encontrada.
    """
    if task_id < len(tasks):
        deleted_task = tasks.pop(task_id)
        return jsonify(deleted_task)
    return jsonify({'error': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)