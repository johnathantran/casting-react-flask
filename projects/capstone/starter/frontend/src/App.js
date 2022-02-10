import logo from './logo.svg';
import './App.css';
import Actor from './components/Actor';
import ActorForm from './components/ActorForm';

function App() {
  return (
    <div className="App">
      <header className="App-header">

        <img src={logo} className="App-logo" alt="logo" />

        <ActorForm/>
        
      </header>
    </div>
  );
}

export default App;
