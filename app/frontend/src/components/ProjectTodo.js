import React from 'react';
import {useParams} from 'react-router-dom'

const ProjectTodoItem = ({todo}) => {

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

const ProjectTodoList = ({todos}) => {
    let {projectId} = useParams()
    let filteredTodos = todos.filter((todo) => todo.project === parseInt(projectId))
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
              {filteredTodos.map((todo) => <ProjectTodoItem todo={todo} />)}
        </table>
    )
}
export default ProjectTodoList
