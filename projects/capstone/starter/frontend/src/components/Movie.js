import React, { Component } from 'react';
import '../stylesheets/Question.css';

class Movie extends Component {
  constructor(){
    super();
    this.state = {
      title: this.props.title,
      releasedate: this.props.releasedate
    }
  }

  render() {
    const { title, releasedate } = this.props;
    return (
      <div>
        <div>
            <h1>{title}</h1>
            <p>Released on: {releasedate}</p>
            <button>Edit Movie Info</button>
            <button>Delete Movie</button>
        </div>
      </div>
    );
  }
}

export default Movie;
