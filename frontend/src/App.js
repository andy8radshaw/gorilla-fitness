import React from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'


import Navbar from './components/common/Navbar'
import Home from './components/common/Home'

import Login from './components/auth/Login'
import Register from './components/auth/Register'
import EventList from './components/events/EventList'
import GroupList from './components/groups/GroupList'



const App = () => {
  return (
    <BrowserRouter>
      <Navbar />
      <Switch>
        <Route exact path='/' component={Home} />
        <Route path='/login' component={Login} />
        <Route path='/register' component={Register} />
        <Route path='/events' component={EventList} />
        <Route path='/groups' component={GroupList} />

      </Switch>
    </BrowserRouter>
  )
}

export default App
