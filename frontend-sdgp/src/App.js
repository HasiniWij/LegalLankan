import React from 'react'; 
import { logo } from "./logo.svg";
import './App.css';
import {BrowserRouter, BrowserRouter as Router, NavLink, Route, Redirect, Switch} from 'react-router-dom';

import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

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
    <div>
    <Router>
    <div className="headerdiv"> 
      <div className="image">
        <img className="logoimg" src={Logo} alt="Logo"/>
      </div>
          <div className="linkdiv">
            <NavLink activeClassName="active" to="/home" className="links">HOME</NavLink>
          </div>
          <div className="linkdiv">
            <NavLink activeClassName="active" to="/search" className="links">SEARCH</NavLink >
          </div>
          <div className="linkdiv">
            <NavLink activeClassName="active" to="/explore" className="links">EXPLORE</NavLink >
          </div>
      </div> 
      <div className="routerdiv">
      <Route exact path="/"
                render={() => {
                    return (<Redirect to="/home" />)
                }}
              />
      <Route exact path='/home' component={Home}/>
      <Route exact path='/search' component={ Search }/>
      <Route path='/explore' component={ Explore }/>
      <Route path='/answer' component={ Answer }/>
      <Route path='/piece' component={ SearchDis }/>
      <Route path='/explore/family' component={ MenuAnswer }/>
      <Route path='/explore/rights' component={ MenuAnswer }/>
      <Route path='/explore/crime' component={ MenuAnswer }/>
      <Route path='/explore/employment' component={ MenuAnswer }/>
      <Route path='/legislation' component={ MenuDis }/>
      <Route path='/piece/simplify' component={ SearchSimplify }/>
      <Switch>
      <Route path='/simplify/:Id' component={ MenuSimplify }/>
      </Switch>
      </div>
    </Router>
    </div>
  );
}
export default App;
