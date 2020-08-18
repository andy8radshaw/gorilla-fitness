import React from 'react'
import { Link } from 'react-router-dom'

function FormLink({ to, text }) {
  return (
    <div className="column is-half is-offset-one-quarter">
      <p className="has-text-centered">
        <small>
          <Link to={to} className="form-link">{text}</Link>
        </small>
      </p>
    </div>
  )
}

export default FormLink
