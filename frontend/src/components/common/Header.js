import React from 'react'

function Header({ heroTitle, heroSubtitle }) {
  return (
    <section className='hero is-medium is-primary'>
      <div className='hero-body'>
        <div className='container'>
          <img className='image' src='https://i.imgur.com/PVzq2iYb.png?2' />
          <h1 className='title'>{heroTitle}</h1>
          <h2 className='subtitle'>{heroSubtitle}</h2>
        </div>
      </div>
    </section>
  )
}

export default Header
