import React from 'react';
import './home.css';
import {BrowserRouter as Router, Link} from 'react-router-dom';

export const Home = ()=> {
    return <div className="homecont">
        <div className="title">SEARCH BY</div>
        <div className="sbine"></div>
        <Link className="homelinks" to="/search"><div className="topic">KEYWORDS</div></Link>
        <Link className="homelinks" to="/explore"><div className="topic">CATEGORY</div></Link>
    </div>
}