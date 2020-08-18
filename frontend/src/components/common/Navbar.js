import React from 'react'
import { Link, withRouter, useHistory } from 'react-router-dom'

import { logout } from '../../lib/auth'

function Navbar() {
  const history = useHistory()


  const handleLogout = () => {
    logout()
    history.push('/')
  }


  return (
    <div>
      <Link to='/'>Home</Link>
      <Link to='/login'>Log In</Link>
      <Link to='/register'>Register</Link>
      <Link onClick={handleLogout}>Logout</Link>
    </div>
  )
}

export default withRouter(Navbar)