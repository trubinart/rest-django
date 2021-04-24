import React from 'react'


const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                {todo.name}
            </td>
            <td>
                <button onClick={() => deleteTodo(todo.id)} type='button'>Delete</button>
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {JSON.stringify(todo.users)}
            </td>
        </tr>
    )
}

const TodoList = ({todo, deleteTodo}) => {
    return (
        <table>
            <th>
                ProjectName
            </th>
            <th>
                ProjectText
            </th>
            <th>
                ProjectUsers
            </th>
            {todo.map((todo) => <TodoItem todo={todo} deleteTodo={deleteTodo}/>)}
        </table>
    )
}

export default TodoList