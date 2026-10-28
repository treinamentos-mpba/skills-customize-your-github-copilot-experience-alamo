# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST com FastAPI para gerenciar tarefas. Você praticará criação de endpoints, validação de dados com modelos Pydantic e uso de métodos HTTP e códigos de status.

## 📝 Tarefas

### 🛠️ Criar e Executar uma API FastAPI

#### Descrição
Complete o código inicial para criar uma aplicação FastAPI e disponibilizar um endpoint inicial. Execute a aplicação localmente e explore a documentação interativa gerada pelo framework.

#### Requisitos
O programa concluído deve:

- Criar uma instância da aplicação FastAPI chamada `app`.
- Implementar um endpoint `GET /` que retorne uma mensagem indicando que a API está funcionando.
- Permitir iniciar a aplicação com `uvicorn starter-code:app --reload`.
- Disponibilizar a documentação interativa em `/docs`.

Para instalar as dependências, execute:

```bash
python -m pip install fastapi uvicorn
```

### 🛠️ Criar e Consultar Tarefas

#### Descrição
Adicione endpoints para criar tarefas e consultar a lista completa ou uma tarefa específica. Use os modelos Pydantic fornecidos no código inicial para estruturar os dados.

#### Requisitos
O programa concluído deve:

- Implementar `POST /tasks` para criar uma tarefa com título, descrição e estado de conclusão.
- Atribuir um identificador único a cada tarefa criada e retornar a tarefa criada.
- Implementar `GET /tasks` para retornar todas as tarefas.
- Implementar `GET /tasks/{task_id}` para retornar a tarefa correspondente ao identificador.
- Retornar o código HTTP `404` quando o identificador consultado não existir.

### 🛠️ Completar as Operações CRUD

#### Descrição
Amplie a API para permitir atualizar e excluir tarefas, mantendo respostas consistentes quando um identificador não for encontrado.

#### Requisitos
O programa concluído deve:

- Implementar `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa existente.
- Implementar `DELETE /tasks/{task_id}` para excluir uma tarefa existente.
- Retornar o código HTTP `404` para atualizações ou exclusões de tarefas inexistentes.
- Retornar uma resposta que confirme a exclusão da tarefa.
- Verificar os endpoints e os códigos de resposta usando `/docs`.
