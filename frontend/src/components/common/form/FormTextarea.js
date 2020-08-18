import React from 'react'

function FormTextarea({ name, label, value, error, onChange, placeholder = null }) {
  return (
    <div className="field">
      <label className="label">{label}</label>
      <div className="control">
        <textarea
          className={`textarea ${error ? 'is-danger' : ''}`}
          placeholder={placeholder ? placeholder : ''}
          name={name}
          onChange={onChange}
          value={value}
        />
      </div>
    </div>
  )
}

export default FormTextarea
