import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Auth0Provider } from '@auth0/auth0-react';
import reportWebVitals from './reportWebVitals';
import { env } from './env';

console.log('env: ');
let envObj;

if (window.location.href === 'http://localhost:3000/') {
  envObj = env.prod;
}
else {
  envObj = env.prod;
} 

console.log(envObj.auth0.callbackURL);
ReactDOM.render(
  
  <Auth0Provider
    domain={envObj.auth0.url}
    clientId={envObj.auth0.clientId}
    redirectUri={window.location.href}
    //redirectUri={envObj.auth0.callbackURL}
  >
    <App />
  </Auth0Provider>,
  /*
  <React.StrictMode>
    <App />
  </React.StrictMode>,*/
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
