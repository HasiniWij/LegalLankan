import React from 'react'; 
import './Home.css';
import {BrowserRouter as Router, Link} from 'react-router-dom';

function Home() {
  return (
    <div class="homecont">
        <div class="leftdiv">
          <div class="topic"><Link class="homelinks" to="/search">SEARCH BY KEYWORDS</Link></div>
          <div class="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
            voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
          </div>
        </div>
        <div class="rightdiv">
          <div class="topic"><Link class="homelinks" to="/explore">SEARCH BY CATEGORY</Link></div>
          <div class="text">
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
            nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
            voluptate velit esse cillum dolore eu fugiat nulla pariatur.</p>
          </div>
        </div>
    </div>
  );
}

export default Home;
