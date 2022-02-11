
import $ from 'jquery';

export function deleteActor(actor_id) {
    
    if(window.confirm('are you sure you want to delete the actor?')) {
        $.ajax({
        url: `/actors/${id}`, //TODO: update request URL
        type: "DELETE",
        success: (result) => {
            return "success";
        },
        error: (error) => {
            alert('Unable to load questions. Please try your request again')
            return;
        }
        })
    }
    }
    
