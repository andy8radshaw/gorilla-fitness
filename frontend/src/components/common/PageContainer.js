import React from 'react'

function PageContainer({ children }) {
  return (
    <section className="section">
      <div className="container">
        {children}
      </div>
    </section>
  )
}

export default PageContainer