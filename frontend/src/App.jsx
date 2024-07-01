import {useEffect, useState} from 'react'
import './App.css'
import ContactList from "./ContactList.jsx";
import ContactForm from "./ContactForm.jsx";

function App() {
  const [contacts, setContacts] = useState([])
  const [isModalOpen, setisModalOpen] = useState(false)

  useEffect(() => {
    fetchContacts()
  }, [])
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }

  const closeModal = () => {
    setisModalOpen(false)
  }

  const modalCreateOpen = () => {
    if (!isModalOpen) {
      setisModalOpen(true)
    }
  }

  return <>
    <ContactList contacts={contacts}/>
    <button onClick={modalCreateOpen}>Create New Contact</button>
    {isModalOpen && <div className="modal">
      <div className={"modal-content"}>
        <span className="close" onClick={closeModal}><button>X</button></span>
        <ContactForm />
      </div>
    </div>
    }

  </>
}

export default App
