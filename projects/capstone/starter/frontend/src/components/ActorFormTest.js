// users.js
import { useAuth0 } from '@auth0/auth0-react';
import { useApi } from "../services/use-api";
import  Actor from '../components/Actor';

export const ActorFormTest = () => {

  const opts = {
    audience: 'casting',
    scope: 'post:actors',
  };
  const { user, login, getAccessTokenWithPopup, getAccessTokenSilently } = useAuth0();
  const { loading, error, refresh, data: users } = useApi(
    '/movies/',
    opts
  );
  const getTokenAndTryAgain = async () => {
    await getAccessTokenWithPopup(opts);
    refresh();
  };
  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    if (error.error === 'login_required') {
      return <button onClick={() => login(opts)}>Login</button>;
    }
    if (error.error === 'consent_required') {
      return (
        <button onClick={getTokenAndTryAgain}>Get access token again</button>
      );
    }
    return <div>Oops {error.message}</div>;
  }

  console.log(getAccessTokenSilently)

  let submitActor = (event) => {
    console.log('submitted');
  }

  return (
    <div>
            <div>
                <div className='forms'>
                    <h2> List a New Actor: </h2>
                    <form onSubmit={submitActor()}>
                        <div><label>Actor Name: <input type="text" name="name"/></label></div>
                        <div><label>Age: <input type="text" name="age"/></label></div>
                        <div><label>Gender: <input type="text" name="gender"/></label></div>
                        <input type="submit" value="Submit"/>
                    </form>
                </div>

                <hr/>


                <hr/>

            </div>
            </div>
  );
};