import React, { Component } from 'react';
import MovieForm from './MovieForm';
import ActorForm from './ActorForm';
import { Routes, Route, Link } from 'react-router-dom';
class Container extends Component {

  render(){
        return (
            <div>
              <ul>
                <li> <Link to="/movies">Movies</Link></li>
                <li><Link to="/actors">Actors</Link></li>
              </ul>
               <Routes>
                  <Route exact path='/movies' element={< MovieForm />}></Route>
                  <Route exact path='/actors' element={< ActorForm />}></Route>
                </Routes>
            </div>
        );
  }
}

export default Container;
