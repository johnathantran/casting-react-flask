// rename this file to env.js and populate the auth0 domain prefix and the clientid
export const env = {
    production: false,
    apiServerUrl: 'http://127.0.0.1:3000', // the running FLASK api server url
    auth0: {
      url: '', // the auth0 domain prefix
      audience: 'casting', // the audience set for the auth0 app
      clientId: '', // the client id generated for the auth0 app
      callbackURL: 'http://localhost:3000/', // the base url of the running ionic application. 
    }
  };
    