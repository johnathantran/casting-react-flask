
//require('dotenv').config();

export const env = {

  prod: {
    production: true,
    apiServerUrl: 'https://casting-react.herokuapp.com/', // the running FLASK api server url
    auth0: {
      url: 'dev-rpk21ij6.us.auth0.com', // the auth0 domain prefix
      audience: 'casting', // the audience set for the auth0 app
      clientId: 'wjAEc39ZyB5gHEu5GYoaBH9KR7WFx6HB', // the client id generated for the auth0 app
      callbackURL: 'https://casting-react.herokuapp.com/', // the base url of the running ionic application. 
    }
  },
  test: {
    production: false,
    apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
    auth0: {
      url: 'dev-rpk21ij6.us.auth0.com', // the auth0 domain prefix
      audience: 'casting', // the audience set for the auth0 app
      clientId: 'wjAEc39ZyB5gHEu5GYoaBH9KR7WFx6HB', // the client id generated for the auth0 app
      callbackURL: 'http://localhost:3000/', // the base url of the running ionic application. 
    }
  }

  /*
    production: false,
    apiServerUrl: 'http://127.0.0.1:3000', // the running FLASK api server url
    auth0: {
      url: 'dev-rpk21ij6.us.auth0.com', // the auth0 domain prefix
      audience: 'casting', // the audience set for the auth0 app
      clientId: 'wjAEc39ZyB5gHEu5GYoaBH9KR7WFx6HB', // the client id generated for the auth0 app
      callbackURL: 'http://localhost:3000/', // the base url of the running ionic application. 
    }
  */
  };
    