import React from 'react'
import { Link, withRouter } from 'react-router-dom'

function Navbar() {
  return (
    <div>
      <Link to='/'>Home</Link>
      <Link to='/login'>Log In</Link>
      <Link to='/register'>Register</Link>
    </div>
  )
}

export default withRouter(Navbar)