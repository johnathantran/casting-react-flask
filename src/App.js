import './App.css';
import Container from './components/Container';
import { useAuth0 } from '@auth0/auth0-react';
import React, { useState, useEffect } from 'react';


function App() {
  const [token, setToken] = useState();
  const {
    isLoading,
    isAuthenticated,
    error,
    user,
    loginWithRedirect,
    logout,
    getAccessTokenSilently
  } = useAuth0();

  useEffect(() => {
    (async () => {
      const accessToken = await getAccessTokenSilently({
        audience: 'casting'
      });
      setToken(accessToken);
      localStorage.setItem('accessToken', accessToken);
    })();
  });

  if (isLoading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>Oops... {error.message}</div>;
  }

  if (isAuthenticated) {
    return (
      <div>
        Hello {user.name}{' '}
        <button onClick={() => logout({ returnTo: window.location.origin })}>
          Log out
        </button>
        <h1>Casting Agency Portal</h1>
        <Container />
      </div>
      
    );
  } else {
    return <button onClick={loginWithRedirect}>Log in</button>;
  }
}

export default App;
