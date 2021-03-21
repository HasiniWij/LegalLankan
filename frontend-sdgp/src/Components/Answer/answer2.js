import React from 'react'; 
import './answer.css';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

export const Answer2 = () => {
    return (
        <div class="allanswers">
            <div class="results">RESULTS:</div>

            <Link to="/doc" className="answers"><div class="ansdiv"><span class="anstitle">Answer 1</span><br/>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua.</div></Link>

            <Link to="/doc" className="answers"><div class="ansdiv"><span class="anstitle">Answer 2</span><br/>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua.</div></Link>

            <Link to="/doc" className="answers"><div class="ansdiv"><span class="anstitle">Answer 3</span><br/>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua.</div></Link>

            <Link to="/doc" className="answers"><div class="ansdiv"><span class="anstitle">Answer 4</span><br/>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua.</div></Link>

            <Link to="/doc" className="answers"><div class="ansdiv"><span class="anstitle">Answer 5</span><br/>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
            labore et dolore magna aliqua.</div></Link>
        </div>
    );
}
