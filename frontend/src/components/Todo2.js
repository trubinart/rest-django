import React from 'react'


const TodoItem = ({todo}) => {
   return (
       <tr>
           <td>
               {todo.name}
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

const TodoList = ({todo}) => {
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
           {todo.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}

export default TodoList