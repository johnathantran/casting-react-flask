import React, { Component } from 'react';
import $ from 'jquery';
import Movie from './Movie';

class MovieForm extends Component {

    constructor(){
        super();
        this.state = {
          movies: []
        }
    }
    
    componentDidMount(){
       this.getMovies()
    }
    
    getMovies= () => {
        $.ajax({
            url: `/movies`, //TODO: update request URL
            type: "GET",
            success: (result) => {
                this.setState({
                    movies: result.movies,
                })
                return;
            },
            error: (error) => {
                alert('Unable to load movies. Please try your request again')
                return;
            }
        })
    }

    editMovie = (event) => {

      try {
        event.preventDefault();

        let id = document.getElementById("select_id").value;
        let title = document.getElementById("editTitle").value;
        let releasedate = document.getElementById("editReleaseDate").value;

        console.log(releasedate);
    
        $.ajax({
          url: '/movies/' + id,
          type: "PATCH",
          dataType: 'json',
          contentType: 'application/json',
          data: JSON.stringify({
            title: title,
            releasedate: releasedate,
          }),
          headers: { Authorization: "Bearer " + localStorage.getItem('accessToken') },
          xhrFields: {
            withCredentials: true
          },
          crossDomain: true,
          success: (result) => {
            this.getMovies()
            return 'success';
          },
          error: (error) => {
            alert('Unable to edit movie. Please try your request again')
            return;
          }
        })
      } catch(e) {
        console.log(e);
      }
    }

    submitMovie = (event) => {

      try {
        event.preventDefault();
        const { title, releasedate } = event.target.elements

        $.ajax({
          url: '/movies',
          type: "POST",
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
            this.getMovies()
            return 'success';
          },
          error: (error) => {
            alert('Unable to post movie. Please try your request again')
            return;
          }
        })
      } catch(e) {
        console.log(e);
      }
    }

    render() {

        let movies = this.state.movies
        if (typeof movies === "undefined" || movies === null) {
          movies = []
        }

        return (
            <div>
            <div>  
                <div className="forms">
                    <h2> List a New Movie: </h2>
                    <form onSubmit={this.submitMovie}>
                        <div><label>Movie: <input type="text" name="title"/></label></div>
                        <div><label>Released on: <input type="text" name="releasedate"/></label></div>
                        <input type="submit" value="Submit"/>
                    </form>
                </div>
                <div className='forms'>
                    <h2> Edit an Existing Movie: </h2>
                    <form onSubmit={this.editMovie}>
                        <select id="select_id" name="id">
                            {movies.map((movie) => (
                                <option value={movie.id}>{movie.id} : {movie.title}</option>
                            ))}
                        </select>
                        <div><label>Movie Title: <input id="editTitle" type="text" name="title"/></label></div>
                        <div><label>Release Date: <input id="editReleaseDate" type="text" name="releasedate"/></label></div>
                        <input type="submit" value="Submit"/>
                    </form>
                </div>
                <h2>All Movies: </h2>

                <div className="itemContainer">
                    {movies.map((movie) => (
                        <Movie id={movie.id} title={movie.title} releasedate={movie.releasedate} />
                    ))}
                </div>

               
            </div>
            </div>
        );
    }
}

export default MovieForm;
