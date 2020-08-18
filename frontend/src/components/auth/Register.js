import React from 'react'
import { faEnvelope, faUser, faLock } from '@fortawesome/free-solid-svg-icons'
import { useHistory } from 'react-router-dom'

import { registerUser } from '../../lib/api'
import useForm from '../../utils/useForm'
import PageContainer from '../common/PageContainer'
import Form from '../common/form/Form'
import FormInput from '../common/form/FormInput'
import FormErrorMessage from '../common/form/FormErrorMessage'
import FormLink from '../common/form/FormLink'
import FormButton from '../common/form/FormButton'
import FormTextarea from '../common/form/FormTextarea'
import FormImageUpload from '../common/form/FormImageUpload'

function Register() {
  const history = useHistory()

  const onSubmitSuccess = () => {
    history.push('/login')
  }

  const { formData, handleChange, formErrors, handleSubmit } = useForm({
    username: '',
    email: '',
    password: '',
    password_confirmation: '',
    first_name: '',
    last_name: '',
    bio: '',
    profile_pic: ''

  }, registerUser, null, onSubmitSuccess)

  return (
    <>
      <PageContainer>
        <Form onSubmit={handleSubmit}>
          <FormInput
            name="username"
            label="Username"
            placeholder="Username"
            icon={faUser}
            value={formData.username}
            error={formErrors.username}
            onChange={handleChange}
          />
          {formErrors.username && <FormErrorMessage error={formErrors.username} />}

          <FormInput
            name="email"
            label="Email"
            placeholder="Email"
            icon={faEnvelope}
            value={formData.email}
            error={formErrors.email}
            onChange={handleChange}
          />
          {formErrors.email && <FormErrorMessage error={formErrors.email} />}
          <FormInput
            name="password"
            label="Password"
            placeholder="Password"
            icon={faLock}
            value={formData.password}
            error={formErrors.password}
            onChange={handleChange}
            type="password"
          />
          {formErrors.password && <FormErrorMessage error={formErrors.password} />}
          <FormInput
            name="password_confirmation"
            label="Password Confirmation"
            placeholder="Password Confirmation"
            icon={faLock}
            value={formData.password_confirmation}
            error={formErrors.password_confirmation}
            onChange={handleChange}
            type="password"
          />
          {formErrors.passwordConfirmation && <FormErrorMessage error={formErrors.passwordConfirmation} />}
          <FormInput
            name="first_name"
            label="First Name"
            placeholder="First Name"
            icon={faUser}
            value={formData.first_name}
            error={formErrors.first_name}
            onChange={handleChange}
          />
          {formErrors.first_name && <FormErrorMessage error={formErrors.first_name} />}
          <FormInput
            name="last_name"
            label="Last Name"
            placeholder="Last Name"
            icon={faUser}
            value={formData.last_name}
            error={formErrors.last_name}
            onChange={handleChange}
          />
          {formErrors.last_name && <FormErrorMessage error={formErrors.last_name} />}
          <FormTextarea
            name="bio"
            label="About you"
            placeholder="Tell us about yourself..."
            onChange={handleChange}
            value={formData.bio}
            error={formErrors.bio}
          />
          {formErrors.bio && <FormErrorMessage error={formErrors.bio} />}
          <FormImageUpload
            label="Profile Pic"
            onChange={handleChange}
            name="profile_pic"
            value={formData.profile_pic}
            error={formErrors.profile_pic}
          />
          <FormButton buttonText="Sign me up" />
          <FormLink to="/login" text="Already have an account?" />
        </Form>
      </PageContainer>
    </>
  )
}

export default Register