import axios from "axios";
import { env } from "./env";

class AuthService {
    url = env.auth0.url;
    audience = env.auth0.audience;
    clientId = env.auth0.clientId;
    callbackURL = env.auth0.callbackURL;

  
    build_login_link() {
      let link = 'https://';
      link += this.url + '.auth0.com';
      link += '/authorize?';
      link += 'audience=' + this.audience + '&';
      link += 'response_type=token&';
      link += 'client_id=' + this.clientId + '&';
      link += 'redirect_uri=' + this.callbackURL;
      console.log(link)
      return link;
    }
  
    login(username, password) {

        let link = this.build_login_link()

        return axios
          .post(link + "/login", {
            username,
            password
          })
          .then(response => {
            if (response.data.accessToken) {
              localStorage.setItem("user", JSON.stringify(response.data));
            }
    
            return response.data;
          });
    }
    
    logout() {
        localStorage.removeItem("user");
    }
}

export default new AuthService();