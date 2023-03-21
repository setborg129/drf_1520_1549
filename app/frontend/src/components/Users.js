import React from "react";


const AuthorItem = ({user}) => {
                return(
                    <tr>
                        <td>
                            {user.first_name}
                        </td>

                        <td>
                            {user.last_name}
                        </td>

                        <td>
                            {user.Birthday}
                        </td>
                        <td>
                            {user.email}
                        </td>
                    </tr>
                      )
}

const AuthorList = ({users}) => {
            return (
                    <table>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Birthday Year</th>
                        <th>E-mail</th>
                        </tr>
                            { users.map((user) => <AuthorItem user={ user }/> )}
                    </table>
            )
}

export default AuthorList
