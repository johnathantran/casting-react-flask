import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { Auth0Provider } from '@auth0/auth0-react';
import reportWebVitals from './reportWebVitals';
import { env } from './env';

ReactDOM.render(
  
  <Auth0Provider
    domain={env.auth0.url}
    clientId={env.auth0.clientId}
    redirectUri={env.auth0.callbackURL}
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
