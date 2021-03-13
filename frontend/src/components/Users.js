import React from 'react'


const UserItem = ({users}) => {
   return (
       <tr>
           <td>
               {users.first_name}
           </td>
           <td>
               {users.last_name}
           </td>
           <td>
               {users.email}
           </td>
       </tr>
   )
}

const UserList = ({users}) => {
   return (
       <table>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Email
           </th>
           {users.map((users) => <UserItem users={users} />)}
       </table>
   )
}

export default UserList