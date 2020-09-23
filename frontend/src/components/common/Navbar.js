import React from 'react'
import { Link, withRouter, useHistory } from 'react-router-dom'

import { logout, isAuthenticated } from '../../lib/auth'

function Navbar() {
  const history = useHistory()

  const [burgerIsOpen, setBurgerIsOpen] = React.useState(false)

  const handleBurgerClose = () => {
    setBurgerIsOpen(false)
  }
  
  const handleBurger = () => {
    setBurgerIsOpen(!burgerIsOpen)
  }

  const handleLogout = () => {
    logout()
    history.push('/')
  }

  return (
    <nav className="navbar is-dark">
      <div className="navbar-brand">
        <Link onClick={handleBurgerClose} className="navbar-item" to="/">
          Home
        </Link>

        <a
          onClick={handleBurger}
          role="button"
          className={`navbar-burger ${burgerIsOpen ? 'is-active' : ''}`}
          aria-label="menu"
          aria-expanded="false"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div className={`navbar-menu ${burgerIsOpen ? 'is-active' : ''}`}>
        <div className="navbar-end">
          {!isAuthenticated() && (
            <Link onClick={handleBurgerClose} className="navbar-item" to="/login">
              Log In
            </Link>
          )}

          {!isAuthenticated() && (
            <Link onClick={handleBurgerClose} className="navbar-item" to="/register">
              Register
            </Link>
          )}

          {isAuthenticated() && (
            <a onClick={handleBurgerClose, handleLogout} className="navbar-item" href="/" >
              Logout
            </a>
          )}
        </div>
      </div>
    </nav>
  )
}

export default withRouter(Navbar)
