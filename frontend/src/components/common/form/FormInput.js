import React from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'

function FormInput({
  name,
  label,
  value,
  error,
  onChange,
  placeholder = null ,
  icon = null,
  type = 'text'
}) {
  return (
    <div className="field">
      <label className="label">{label}</label>
      <div className="control has-icons-left">
        <input
          className={`input ${error ? 'is-danger' : ''}`}
          placeholder={placeholder ? placeholder : ''}
          name={name}
          onChange={onChange}
          value={value}
          type={type}
        />
        {icon &&
          <span className="icon is-small is-left">
            <FontAwesomeIcon icon={icon} />
          </span>
        }
      </div>
    </div>
  )
}

export default FormInput
