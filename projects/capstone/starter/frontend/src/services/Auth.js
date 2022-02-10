import { env } from "./env";
import auth0 from 'auth0-js';

export default class Auth {
    constructor(){

      this.auth0 = new auth0.WebAuth({
        domain: env.auth0.url,
        clientID: env.auth0.clientId,
        redirectUri: env.auth0.callbackURL,
      })
  }

  handleAuth = () => {
    this.auth0.parseHash((err, authResult) => {
      if(authResult && authResult.accessToken && authResult.idToken) {
        this.setSession(authResult);
        this.history.push("/");
      } else if (err) {
        alert(`Error: ${err.error}`)
        console.log(err);  
      }
    })
  }

  getAccessToken = () => {
    const accessToken = localStorage.getItem("access_token")
    if(!accessToken){
      throw new Error("No access token found")
    }
    return accessToken
  }
}