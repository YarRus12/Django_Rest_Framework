import React from 'react'
import {Link} from 'react-router-dom'

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={'user/${user.first_name}'}>{user.first_name}</Link>
            </td>
            <td>
                {user.last_name}
            </td>
            <td>
                {user.birthday_year}
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
                Birthday year
            </th>
            {users.map((user) => <UserItem user={user} />)}
        </table>
    )
}

export default UserList