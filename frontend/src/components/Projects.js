import React from 'react'


const ProjectsItem = ({projects}) => {
   return (
       <tr>
           <td>
               {projects.name}
           </td>
           <td>
               {projects.text}
           </td>
           <td>
               {JSON.stringify(projects.users)}
           </td>
       </tr>
   )
}

const ProjectsList = ({projects}) => {
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
           {projects.map((projects) => <ProjectsItem projects={projects} />)}
       </table>
   )
}

export default ProjectsList