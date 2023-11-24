import React from 'react'
import Login from '../src/components/login/Login'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Signup from '../src/components/signup/Signup'

function App() {
  return (
    <BrowserRouter>
    <Routes>
    <Route path = '/' element = {<Login />}> </Route>
    <Route path = '/signup' element = {<Signup />}></Route>
    </Routes>
    </BrowserRouter>
  )
}

export default App
