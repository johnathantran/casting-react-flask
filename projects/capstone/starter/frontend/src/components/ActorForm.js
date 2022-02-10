import React, { Component } from 'react';
import $ from 'jquery';
import Actor from './Actor';

class ActorForm extends Component {

    constructor(){
        super();
        this.state = {
          actors: [],
          inputName: '',
          inputAge: '',
          inputGender: ''
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
                alert('Unable to load questions. Please try your request again')
                return;
            }
        })
    }

    submitActor = (event) => {

        event.preventDefault();
        const { name, age, gender } = event.target.elements

        $.ajax({
          url: '/actors', //TODO: update request URL
          type: "POST",
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

    render() {
        console.log("rendering...")

        return (
            <div>
            <div>  
                <button onClick={() => {this.getActors()}}>Get Actors</button>
                <h2>All Actors: </h2>
             
                {this.state.actors.map((actor) => (
                    <Actor name={actor.name} age={actor.age} gender={actor.gender} />
                ))}

      
                <h2> List a New Actor: </h2>
                <form onSubmit={this.submitActor}>
                    <div><label>Actor: <input type="text" name="name"/></label></div>
                    <div><label>Age: <input type="text" name="age"/></label></div>
                    <div><label>Gender: <input type="text" name="gender"/></label></div>
                    <input type="submit" value="Submit"/>
                </form>
                <a href="/">Back to Home</a>
            </div>
            </div>
        );
    }
}

export default ActorForm;
