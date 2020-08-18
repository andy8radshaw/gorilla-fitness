import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons'

function FormErrorMessage({ error = 'Required Field' }){
  return (
    <small className="help is-danger">
      <span className="icon is-small">
        <FontAwesomeIcon icon={faExclamationTriangle} />
      </span>
      {error}
    </small>
  )
}

export default FormErrorMessage
