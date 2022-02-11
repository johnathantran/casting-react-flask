import React, { Component } from 'react';
import $ from 'jquery';

class Movie extends Component {

  constructor(props){
    super(props);
    this.state = {
      id: this.props.id,
      title: this.props.title,
      releasedate: this.props.releasedate
    }
  }

  editMovie(event, movie_id) {
    try {
      event.preventDefault();
      const { title, releasedate } = event.target.elements

      $.ajax({
        url: '/movies/' + movie_id,
        type: "PATCH",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify({
          title: title.value,
          releasedate: releasedate.value,
        }),
        headers: { Authorization: "Bearer " + localStorage.getItem('accessToken') },
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
    } catch(e) {
      console.log(e);
    }
  }


  deleteMovie(movie_id) {
    try {
      $.ajax({
        url: `/movies/` + movie_id,
        type: "DELETE",
        headers: { Authorization: "Bearer " + localStorage.getItem('accessToken') },
        success: (result) => {
          alert('Movie has been deleted!')
          window.location.reload();
          return;
        },
        error: (error) => {
          alert('Unable to delete movie. Please try your request again')
          return;
        }
      })
    } catch(e) {
      console.log(e);
    }
  }

  render() {
    const { title, releasedate } = this.props;
    return (
      <div>
        <div className='items'>
            <h1>{title}</h1>
            <p>Released on: {releasedate}</p>
            <button onClick={() => {this.deleteMovie(this.state.id)}}>Delete</button>
        </div>
      </div>
    );
  }
}

export default Movie;
