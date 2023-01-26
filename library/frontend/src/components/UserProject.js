import React from 'react'
import {useParams} from 'react-router-dom'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.link}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                {project.description}
            </td>
        </tr>
    )
}

const UserProjectList = ({projects}) => {
    let {name} = useParams()
    let filtered_projects = projects.filter((item)=>projects.author==name)
    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Link
            </th>
            <th>
                User
            </th>
            <th>
                Description
            </th>
            {filtered_projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default UserProjectList