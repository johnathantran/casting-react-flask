import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Auth0Provider } from '@auth0/auth0-react';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router} from 'react-router-dom'
import { env } from './env';

console.log('env: ');
let envObj = env.test;

console.log(envObj.auth0.callbackURL);
ReactDOM.render(
  <Router>
    <Auth0Provider
      domain={envObj.auth0.url}
      clientId={envObj.auth0.clientId}
      redirectUri={envObj.auth0.callbackURL}
      //redirectUri={'https://casting-react.herokuapp.com/'}
    >
      <App />
    </Auth0Provider>
  </Router>,

  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
