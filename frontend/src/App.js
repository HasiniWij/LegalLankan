import React from 'react'; 
import './App.css';
import {BrowserRouter as Router, Link, NavLink, Route, Redirect, Switch} from 'react-router-dom';

import Logo from './images/logo.png';

import { Answer } from './Components/Answer/answer';
import { Explore } from './Components/Explore/explore';
import { Home } from './Components/Home/home';
import { Display } from './Components/Display/display';
import { MenuAnswer } from './Components/Answer/menuAnswer';
import { Simplify } from './Components/Simplify/simplify';

function App() {
  return (
    <body style={{ background: "black"}} id="main">
    <div >
    <Router>
    <div className="headerdiv"> 
      <div className="image">
        <Link to="/home"><img className="logoimg" src={Logo} alt="Logo"/></Link>
      </div>
          <div className="linkdiv">
            <NavLink activeClassName="active" to="/home" className="links">HOME</NavLink>
          </div>
          
          <div className="linkdiv">
            {/* <NavLink activeClassName="active" to="/explore" className="links">EXPLORE</NavLink > */}
            <NavLink activeClassName="activee" className="links" to={{pathname:"/explore/family", 
                    state: { urlfull: "http://127.0.0.1:5000/legislationlist/family", title:"FAMILY" }}}>EXPLORE
                    </NavLink>
          </div>
      </div> 
      <div className="routerdiv">
      <Route exact path="/"
                render={() => {
                    return (<Redirect to="/home" />)
                }}
              />
      <Route path='/home' component={Home}/>
      <Route path='/explore' component={ Explore } />
      <Route path='/answer' component={ Answer }/>
      <Route path='/explore/family' component={ MenuAnswer }/>
      <Route path='/explore/rights' component={ MenuAnswer }/>
      <Route path='/explore/crime' component={ MenuAnswer }/>
      <Route path='/explore/employment' component={ MenuAnswer }/>
      <Route path='/legislation' component={ Display }/>
    
      <Route path='/simplify/:Id' component={ Simplify }/>
    
      </div>
    </Router>
    </div>
    </body>
  );
}
export default App;
