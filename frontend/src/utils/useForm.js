import React from 'react'

function useForm(intialFormState = {}, submitFn, submitParams = null, onSubmitSuccess = () => {}) {

  const [formData, setFormData] = React.useState(intialFormState)
  const [formErrors, setFormErrors] = React.useState({}) 

  const handleChange = ({ target: { name, value, type, checked } }) => {
    const newValue = type === 'checkbox' ? checked : value
    const updatedFormData = { ...formData, [name]: newValue }
    const updatedErrors = { ...formErrors, [name]: '' }
    setFormData(updatedFormData)
    setFormErrors(updatedErrors)
  }



  const handleSubmit = async event => {
    event.preventDefault()

    try {
      const response = await submitFn(formData, submitParams)
      onSubmitSuccess(response)
    } catch (err) {
      setFormErrors(err.response.data.errors)
    }
  }

  const handleAddImage = event => {
    event.preventDefault()
    const newFormData = { ...formData, images: [...formData.images, ''] }
    const newFormErrors = { ...formErrors, [event.target.name]: '' }
    setFormData({ newFormData })
    setFormErrors({ newFormErrors })
  }
  
  return { formData, handleChange, handleAddImage, setFormData, formErrors, setFormErrors, handleSubmit }
}

export default useForm