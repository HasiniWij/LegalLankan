import React from 'react'; 
import './search.css';
import Searchimg from './search.png';
import { Answer } from '../Answer/answer'

export const Search = () => {
    return (
        <div class="container">
            <form action="http://localhost:5000/search">
                <div class="searchbox">
                    <input type="text" class="searchtext" name="query" placeholder="Enter Keyword or Query.."></input>
                    <img class="searchimg" src={Searchimg} alt="Search"/>
                </div>
                 <div class="searchdiv"><button class="searchbutton" onClick= { Answer } >Search</button></div>
            </form>
        </div>
      );
}