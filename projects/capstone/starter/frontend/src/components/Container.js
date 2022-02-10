import React, { Component } from 'react';
import MovieForm from './MovieForm';
import ActorForm from './ActorForm';

class Container extends Component {
  constructor(){
    super();
    this.state = {
        toggleMovieView: true
    }
    this.toggleForm =this.toggleForm.bind(this);
  }

  toggleForm() {
    this.setState(prevState => ({
        toggleMovieView: !prevState.toggleMovieView
      }));
  }

  render(){
    if (this.state.toggleMovieView) {  
        return (
            <div>
                <button onClick={this.toggleForm}> Toggle Movie/Actor Lists</button>
                <h1> Movie View </h1>
                <MovieForm />
            </div>
        );
    }
    else {
        return (
            <div>
                <button onClick={this.toggleForm}> Toggle Movie/Actor Lists</button>
                <h1> Actor View </h1>
                <ActorForm />
            </div>
        )
    }
  }
}

export default Container;
