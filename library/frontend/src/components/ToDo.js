import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.create_at}
            </td>
            <td>
                {todo.update_at}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.active}
            </td>

        </tr>
    )
}


const ToDoList = ({todo_tasks}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Created
            </th>
            <th>
                Updated
            </th>
            <th>
                User
            </th>
            <th>
                Active
            </th>
            {todo_tasks.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoList