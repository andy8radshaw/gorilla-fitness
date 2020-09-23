import React from 'react'
import { faEnvelope, faUser, faLock, faCameraRetro, faInfoCircle } from '@fortawesome/free-solid-svg-icons'
import { useHistory } from 'react-router-dom'

import { registerUser } from '../../lib/api'
import { setToken } from '../../lib/auth'
import useForm from '../../utils/useForm'
import PageContainer from '../common/PageContainer'
import Form from '../common/form/Form'
import FormInput from '../common/form/FormInput'
// import FormErrorMessage from '../common/form/FormErrorMessage'
import FormLink from '../common/form/FormLink'
import FormButton from '../common/form/FormButton'
// import FormTextarea from '../common/form/FormTextarea'

function Register() {
  const history = useHistory()

  const onSubmitSuccess = response => {
    setToken(response.data.token)
    history.push('/')
  }

  const { formData, handleChange, formErrors, handleSubmit } = useForm({
    username: '',
    email: '',
    password: '',
    password_confirmation: '',
    first_name: '',
    last_name: '',
    bio: '',
    profile_image: ''

  }, registerUser, null, onSubmitSuccess)


  return (
    <>
      <PageContainer>
        <Form onSubmit={handleSubmit}>
          <FormInput
            error={formErrors.username}
            name="username"
            label="Username"
            placeholder="Username"
            icon={faUser}
            value={formData.username || ''}
            onChange={handleChange}
          />
          {/* {formErrors.username && <FormErrorMessage error={formErrors.username} />} */}

          <FormInput
            name="email"
            label="Email"
            placeholder="Email"
            icon={faEnvelope}
            value={formData.email || ''}
            error={formErrors.email}
            onChange={handleChange}
          />
          {/* {formErrors.email && <FormErrorMessage error={formErrors.email} />} */}
          <FormInput
            name="password"
            label="Password"
            placeholder="Password"
            icon={faLock}
            value={formData.password || ''}
            error={formErrors.password}
            onChange={handleChange}
            type="password"
          />
          {/* {formErrors.password && <FormErrorMessage error={formErrors.password} />} */}
          <FormInput
            name="password_confirmation"
            label="Password Confirmation"
            placeholder="Password Confirmation"
            icon={faLock}
            value={formData.password_confirmation || ''}
            error={formErrors.password_confirmation}
            onChange={handleChange}
            type="password"
          />
          {/* {formErrors.passwordConfirmation && <FormErrorMessage error={formErrors.passwordConfirmation} />} */}
          <FormInput
            name="first_name"
            label="First Name"
            placeholder="First Name"
            icon={faInfoCircle}
            value={formData.first_name || ''}
            error={formErrors.first_name}
            onChange={handleChange}
          />
          {/* {formErrors.first_name && <FormErrorMessage error={formErrors.first_name} />} */}
          <FormInput
            name="last_name"
            label="Last Name"
            placeholder="Last Name"
            icon={faInfoCircle}
            value={formData.last_name || ''}
            error={formErrors.last_name}
            onChange={handleChange}
          />
          {/* {formErrors.last_name && <FormErrorMessage error={formErrors.last_name} />} */}
          {/* <FormTextarea
            name="bio"
            label="About you"
            placeholder="Tell us about yourself..."
            onChange={handleChange}
            value={formData.bio || ''}
            error={formErrors.bio}
          /> */}
          {/* {formErrors.bio && <FormErrorMessage error={formErrors.bio} />} */}
          <FormInput
            name="profile_image"
            label="Profile Pic"
            placeholder="URL for your profile picture"
            icon={faCameraRetro}
            value={formData.profile_image || ''}
            error={formErrors.profile_image}
            onChange={handleChange}
          />
          {/* {formErrors.profile_image && <FormErrorMessage error={formErrors.profile_image} />} */}
          <FormButton buttonText="Sign me up" />
          <FormLink to="/login" text="Already have an account?" />
        </Form>
      </PageContainer>
    </>
  )
}

export default Register