import React, { Component } from 'react';
import $ from 'jquery';

class Actor extends Component {
  constructor(props){
    super(props);
    this.state = {
      id: this.props.id,
      name: this.props.name,
      age: this.props.age,
      gender: this.props.gender
    }
  }

  editActor(event, actor_id) {

    event.preventDefault();
    const { name, age, gender } = event.target.elements

    $.ajax({
      url: '/actors/' + actor_id,
      type: "PATCH",
      dataType: 'json',
      contentType: 'application/json',
      data: JSON.stringify({
        name: name.value,
        age: age.value,
        gender: gender.value
      }),
      xhrFields: {
        withCredentials: true
      },
      crossDomain: true,
      success: (result) => {
        return 'success';
      },
      error: (error) => {
        alert('Unable to add question. Please try your request again')
        return;
      }
    })
  }


  deleteActor(actor_id) {
    $.ajax({
      url: `/actors/` + actor_id, //TODO: update request URL
      type: "DELETE",
      success: (result) => {  
        alert('Actor has been deleted!')
        window.location.reload();
        return;
      },
      error: (error) => {
        alert('Unable to delete actor. Please try your request again')
        return;
      }
    })
  }

  render() {
    const { name, age, gender } = this.props;
    return (
        <div className='items'>
            <h1>{name}</h1>
            <p>Age: {age}</p>
            <p>Gender: {gender}</p>
            <button onClick={() => {this.deleteActor(this.state.id)}}>Delete</button>
        </div>
    );
  }
}

export default Actor;
