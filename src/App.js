import React from 'react'; 
import logo from './logo.svg';
import './App.css';
import { TodoPage } from './Pages/TodoPage';
import { HomePage } from './Pages/HomePage';

import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

function App() {
  return (
    <Router>
      <div className="App">
        <TodoPage/>
      </div>
      <header>
      <div className="headerdiv"> 
       <img src={Logo} alt="Logo"/>
      <nav>
        <ul>
          <li>
            <Link to="/" className="links">HOME</Link>
          </li>
          <li>
            <Link to="/search" className="links">SEARCH</Link>
          </li>
        </ul>
      </nav>
      </div> 
      </header>
      <div className="routerdiv">
      <Route path='/' exact  component={HomePage}/>
      <Route path='/search' component={TodoPage}/>
      </div>
      <footer>
        <div className="footerdiv">
          <div className="con">Contact us on: </div>
          <div className="sm"> <img className="im" src={FB} alt="fb"/></div>
          <div className="sm"><img className="im" src={IG} alt="ig"/></div>
          <div className="sm"> <img className="im" src={TW} alt="tw"/></div>
        </div>
      </footer>
    </Router>
  );
}
export default App;
