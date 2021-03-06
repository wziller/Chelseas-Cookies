import React, { useState, useEffect } from "react";
import LoginForm from "./LoginForm"
import { Modal } from "../../../context/Modal";

function LoginModal() {
  useEffect(() => {

  }, [])
  const [showModal, setShowModal] = useState(false);

  return (
    <div>
      <button className='Nav_Button' onClick={() => setShowModal(true)}>Login</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <LoginForm setShowModal= {setShowModal}/>
        </Modal>
      )}

    </div>
  );
}

export default LoginModal;
