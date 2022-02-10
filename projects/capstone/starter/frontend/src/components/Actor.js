import React, { Component } from 'react';

class Actor extends Component {
  constructor(props){
    super(props);
    this.state = {
      name: this.props.name,
      age: this.props.age,
      gender: this.props.gender
    }
  }

  render() {
    const { name, age, gender } = this.props;
    return (
      <div>
        <div>
            <h1>{name}</h1>
            <p>Age: {age}</p>
            <p>Gender: {gender}</p>
            <button>Edit Actor Info</button>
            <button>Delete Actor</button>
        </div>
      </div>
    );
  }
}

export default Actor;
