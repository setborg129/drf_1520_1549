import React from 'react';

const TodoItem = ({todo}) => {

    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.todo_text}
            </td>
            <td>
                {todo.creator}
            </td>

        </tr>
    )
}

const TodoList = ({todos}) => {

    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Author
            </th>
             {todos.map((todo) => <TodoItem todo={todo} />)}
        </table>
    )
}

export default TodoList
