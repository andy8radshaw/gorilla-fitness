import axios from 'axios'
import { getToken } from './auth'

const baseUrl = '/api'

const withHeaders = () => {
  return {
    headers: { Authorization: `Bearer ${getToken()}` }
  }
}

//* USER REQUESTS

export const loginUser = data => {
  return axios.post(`${baseUrl}/auth/login/`, data)
}

export const registerUser = (data) => {
  return axios.post(`${baseUrl}/auth/register/`, data)
}


