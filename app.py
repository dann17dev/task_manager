from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para armazenar as tarefas
tasks = []

# Rota para obter todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Rota para adicionar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

# Rota para atualizar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id < len(tasks):
        tasks[task_id] = request.json
        return jsonify(tasks[task_id]), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

# Rota para deletar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id < len(tasks):
        tasks.pop(task_id)
        return jsonify({'mensagem': 'Tarefa deletada'}), 200
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
