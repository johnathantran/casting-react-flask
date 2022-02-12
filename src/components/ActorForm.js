import React, { Component } from 'react';
import $ from 'jquery';
import Actor from './Actor';

class ActorForm extends Component {

    constructor(){
        super();
        this.state = {
          actors: []
        }
    }
    
    componentDidMount(){
        this.getActors()
    }
    
    getActors= () => {

        $.ajax({
            url: `/actors`, //TODO: update request URL
            type: "GET",
            success: (result) => {
                this.setState({
                    actors: result.actors,
                })
                return;
            },
            error: (error) => {
                alert('Unable to load actors. Please try your request again')
                return;
            }
        })
    }

    submitActor = (event) => {

        try {
          event.preventDefault();
          const { name, age, gender } = event.target.elements
          $.ajax({
            url: '/actors',
            type: "POST",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({
              name: name.value,
              age: age.value,
              gender: gender.value
            }),
            headers: { Authorization: "Bearer " + localStorage.getItem('accessToken') },
            xhrFields: {
              withCredentials: true
            },
            crossDomain: true,
            success: (result) => {
              this.getActors()
              return 'success';
            },
            error: (error) => {
              alert('Unable to post actor. Please try your request again')
              return;
            }
          })
        } catch(e) {
          console.log(e);
        } 
    }

    editActor = (event) => {

      try {
        event.preventDefault();

        let id = document.getElementById("select_id").value;
        let name = document.getElementById("editName").value;
        let age = document.getElementById("editAge").value;
        let gender = document.getElementById("editGender").value;
    
        $.ajax({
          url: '/actors/' + id,
          type: "PATCH",
          dataType: 'json',
          contentType: 'application/json',
          data: JSON.stringify({
            name: name,
            age: age,
            gender: gender
          }),
          headers: { Authorization: "Bearer " + localStorage.getItem('accessToken') },
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          success: (result) => {
            this.getActors()
            return 'success';
          },
          error: (error) => {
            alert('Unable to edit actor. Please try your request again')
            return;
          }
        })
      } catch(e) {
        console.log(e);
      }
    }

    render() {

        let actors = this.state.actors
        if (typeof actors === "undefined" || actors === null) {
          actors = []
        }

        return (
            <div>
              <h1>Actor Form </h1>
              <div>
                  <div className='forms'>
                      <h2> List a New Actor: </h2>
                      <form onSubmit={this.submitActor}>
                          <div><label>Actor Name: <input type="text" name="name"/></label></div>
                          <div><label>Age: <input type="text" name="age"/></label></div>
                          <div><label>Gender: <input type="text" name="gender"/></label></div>
                          <input type="submit" value="Submit"/>
                      </form>
                  </div>

                  <hr/>

                  <div className='forms'>
                      <h2> Edit an Existing Actor: </h2>
                      <form onSubmit={this.editActor}>
                          <select id="select_id" name="id">
                              {this.state.actors.map((actor) => (
                                  <option value={actor.id}>{actor.id} : {actor.name}</option>
                              ))}
                          </select>
                          <div><label>Actor Name: <input id="editName" type="text" name="name"/></label></div>
                          <div><label>Age: <input id="editAge" type="text" name="age"/></label></div>
                          <div><label>Gender: <input id="editGender" type="text" name="gender"/></label></div>
                          <input type="submit" value="Submit"/>
                      </form>
                  </div>
                  <hr/>
                  <h2>All Actors: </h2>
                  <div className="itemContainer">
                      {actors.map((actor) => (
                          <Actor id={actor.id} name={actor.name} age={actor.age} gender={actor.gender} />
                      ))}
                  </div>
              </div>
            </div>
        );
    }
}

export default ActorForm;
