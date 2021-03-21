import React from 'react'; 
import { logo } from "./logo.svg";
import './App.css';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

import { Answer2 } from './Components/Answer/answer2';
import { Answer } from './Components/Answer/answer';
import { Search } from './Components/Search/search';
import { Explore } from './Components/Explore/explore';
import { Home } from './Components/Home/home';

function App() {
  return (
    <Router>
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
          <li>
            <Link to="/explore" className="links">EXPLORE</Link>
          </li>
        </ul>
      </nav>
      </div> 
      </header>
      <div className="routerdiv">
      <Route path='/' exact  component={Home}/>
      <Route path='/search' component={ Search }/>
      <Route path='/explore' component={ Explore }/>
      <Route path='/answer2' component={ Answer2 }/>
      <Route path='/answer' component={ Answer }/>
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
