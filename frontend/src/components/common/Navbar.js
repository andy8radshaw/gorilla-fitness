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
    <nav className="navbar is-info">
      <div className="navbar-brand">
        <Link className="navbar-item" to="/">
          Home
        </Link>
        <Link className="navbar-item" to="/login">
          Log In
        </Link>
        <Link className="navbar-item" to="/register">
          Register
        </Link>
        <a className="navbar-item" href="/" onClick={handleLogout}>
          Logout
        </a>
        <a
          role="button"
          className="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
    </nav>
  )
}

export default withRouter(Navbar)
