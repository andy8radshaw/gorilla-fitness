import React from 'react'

function FormButton({ buttonText = 'submit' }){
  return (
    <div className="field">
      <button type="submit" className="button is-fullwidth is-dark">
        {buttonText}
      </button>
    </div>
  )
}

export default FormButton
