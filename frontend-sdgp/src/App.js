import React from 'react'; 
import { logo } from "./logo.svg";
import './App.css';
import {BrowserRouter, BrowserRouter as Router, Link, Route} from 'react-router-dom';

import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

import { Answer2 } from './Components/Answer/answer2';
import { Answer } from './Components/Answer/answer';
import { Search } from './Components/Search/search';
import { Explore } from './Components/Explore/explore';
import { Home } from './Components/Home/home';
import { SearchDis } from './Components/Display/searchDis';
import { MenuDis } from './Components/Display/menuDis';
import { MenuAnswer } from './Components/Answer/menuAnswer';
import { SearchSimplify } from './Components/Simplify/searchSimplify';
import { MenuSimplify } from './Components/Simplify/menuSimplify';

function App() {
  return (
    <BrowserRouter>
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
      <Route path='/piece' component={ SearchDis }/>
      <Route path='/explore/family' component={ MenuAnswer }/>
      <Route path='/explore/rights' component={ MenuAnswer }/>
      <Route path='/explore/crime' component={ MenuAnswer }/>
      <Route path='/explore/employment' component={ MenuAnswer }/>
      <Route path='/legislation' component={ MenuDis }/>
      <Route path='/piece/simplify' component={ SearchSimplify }/>
      <Route path='/legislation/simplify' component={ MenuSimplify }/>
      </div>
      <footer>
        <div className="footerdiv">
          <div className="con">Contact us on: </div>
          <div className="sm"> <img className="im" src={FB} alt="fb"/></div>
          <div className="sm"><img className="im" src={IG} alt="ig"/></div>
          <div className="sm"> <img className="im" src={TW} alt="tw"/></div>
        </div>
      </footer>
    </BrowserRouter>
  );
}
export default App;
