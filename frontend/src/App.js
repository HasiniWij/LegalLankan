import React from 'react'; 
import './App.css';
import Home from './Home/Home';
import Search from './Search/Search';
import Explore from './Explore/Explore';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

function App() {
  return (
    <Router>
      <header>
      <div class="headerdiv"> 
       <img src={Logo} alt="Logo"/>
      <nav>
        <ul>
          <li>
            <Link to="/" class="links">HOME</Link>
          </li>
          <li>
            <Link to="/search" class="links">SEARCH</Link>
          </li>
          <li>
            <Link to="/explore" class="links">EXPLORE</Link>
          </li>
        </ul>
      </nav>
      </div> 
      </header>
      <div class="routerdiv">
      <Route path='/' exact  component={Home}/>
      <Route path='/search' component={Search}/>
      <Route path='/explore' component={Explore}/>
      </div>
      <footer>
        <div class="footerdiv">
          <div class="con">Contact us on: </div>
          <div class="sm"> <img class="im" src={FB} alt="fb"/></div>
          <div class="sm"><img class="im" src={IG} alt="ig"/></div>
          <div class="sm"> <img class="im" src={TW} alt="tw"/></div>
        </div>
      </footer>
    </Router>
  );
}
export default App;
