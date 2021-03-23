import React from 'react';
import './home.css';
import {BrowserRouter as Router, Link} from 'react-router-dom';

export const Home = ()=> {
    return <div className="homecont">
        <div className="leftdiv">
          <div className="topic"><Link className="homelinks" to="/search">SEARCH BY KEYWORDS</Link></div>
          <div className="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
            voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
          </div>
        </div>
        <div className="rightdiv">
          <div className="topic"><Link className="homelinks" to="/explore">SEARCH BY CATEGORY</Link></div>
          <div className="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
            voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
          </div>
        </div>
    </div>
}