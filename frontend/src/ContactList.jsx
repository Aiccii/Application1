import React from "react";

const ContactList = ({contacts, updateContact, updateCallBack }) => {

    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options)

            if (response.status === 200) {
                updateCallBack()
            }else {
                console.error("Couldn't delete contact")
            }

        }catch (err) {
            alert(err)
        }
    }

    return <div>
        <h2>Contacts</h2>
        <table>
            <thead>
                <tr>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map((contacts) => (
                    <tr key={contacts.id}>
                        <td>{contacts.firstName}</td>
                        <td>{contacts.lastName}</td>
                        <td>{contacts.email}</td>
                        <td>
                            <button onClick={() => updateContact(contacts)}>Update</button>
                            <button onClick={()=> onDelete(contacts.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>

    </div>

}

export default ContactList