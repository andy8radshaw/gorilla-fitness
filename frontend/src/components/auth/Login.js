import React, { useState } from 'react'
import { faEnvelope, faLock } from '@fortawesome/free-solid-svg-icons'
import { useHistory } from 'react-router-dom'
import { loginUser } from '../../lib/api'
import { setToken } from '../../lib/auth'
import useForm from '../../utils/useForm'

import PageContainer from '../common/PageContainer'
import Form from '../common/form/Form'
import FormInput from '../common/form/FormInput'
import FormButton from '../common/form/FormButton'
import FormErrorMesssage from '../common/form/FormErrorMessage'
import FormLink from '../common/form/FormLink'


function Login() {
  const [error, setError] = useState(null)
  const history = useHistory()

  const { formData, handleChange } = useForm({
    email: '',
    password: ''
  })

  const handleSubmit = async event => {
    event.preventDefault()

    try {
      const res = await loginUser(formData)
      setToken(res.data.token)
      history.push('/')
    } catch (err) {
      setError('Invalid Credentials')
    }
  }

  return (
    <>
      <PageContainer>
        <Form onSubmit={handleSubmit}>
          <FormInput
            name="email"
            label="Email"
            value={formData.email}
            onChange={handleChange}
            error={error}
            placeholder="Email"
            icon={faEnvelope}
          />
          <FormInput
            name="password"
            label="Password"
            value={formData.password}
            onChange={handleChange}
            error={error}
            placeholder="Password"
            icon={faLock}
            type="password"
          />
          {error && <FormErrorMesssage error="Invalid Credentials"/>}
          <FormButton buttonText="Log Me In!"/>
          <FormLink to="/register" text="Don't have an account?"/>
        </Form>
      </PageContainer>
    </>
  )
}

export default Login