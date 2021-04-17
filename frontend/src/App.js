import React from 'react'; 
import './App.css';
import {BrowserRouter as Router, NavLink, Route, Redirect, Switch} from 'react-router-dom';

import Logo from './images/logo.png';
import IG from './images/ig.png';
import TW from './images/tw.png';
import FB from './images/fb.png';

import { Answer } from './Components/Answer/answer';
import { Search } from './Components/Search/search';
import { Explore } from './Components/Explore/explore';
import { Home } from './Components/Home/home';
import { Display } from './Components/Display/display';
import { MenuAnswer } from './Components/Answer/menuAnswer';
import { Simplify } from './Components/Simplify/simplify';

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
      <Route path='/home' component={Home}/>
      <Route path='/search' component={ Search }/>
      <Route path='/explore' component={ Explore }/>
      <Route path='/answer' component={ Answer }/>
      <Route path='/explore/family' component={ MenuAnswer }/>
      <Route path='/explore/rights' component={ MenuAnswer }/>
      <Route path='/explore/crime' component={ MenuAnswer }/>
      <Route path='/explore/employment' component={ MenuAnswer }/>
      <Route path='/legislation' component={ Display }/>
      <Switch>
      <Route path='/simplify/:Id' component={ Simplify }/>
      </Switch>
      </div>
    </Router>
    </div>
  );
}
export default App;
