import React from 'react';
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {

    return (
        <tr>
            <td>
                <Link to={`/projects/${project.id}`}>{project.name}</Link>
            </td>
            <td>
                {project.repo_link}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {

    return (
        <table>
            <th>
                Project name
            </th>
            <th>
                Repo link
            </th>
            <th>
                Allowed users
            </th>
             {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList
