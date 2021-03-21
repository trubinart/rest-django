import React from 'react'
import {Link} from 'react-router-dom'
import { useParams } from 'react-router-dom'



const UserItem = ({users}) => {
   return (
       <tr>
          <td>
               <Link to={`users/${users.id}`}>{users.id}</Link>
           </td>
           <td>
               {users.firstName}
           </td>
           <td>
               {users.lastName}
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
               ID
           </th>
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

const UserList2 = ({users}) => {
    let { id } = useParams();
    let filtered_items = users.filter((item) => item.id == id)
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Email
           </th>
           {filtered_items.map((users) => <UserItem users={users} />)}
       </table>
   )
}


export {UserList, UserList2}