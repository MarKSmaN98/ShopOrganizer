import {React, useState} from 'react';
import {Routes, Route, Navigate} from 'react-router-dom';
import '../App.css';
import Home from './Home'
import Nav from './Nav';
import Login from './Login';
import Option from './Option';



function App() {
  return (
    <div className="App" content='widthd-device-width, initial-scale=1.0'>
      <Routes>
        <Route
          element = {<Home />}
          path = '/'
        />

      </Routes>

    </div>
  );
}

export default App;
