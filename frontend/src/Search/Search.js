import React from 'react'; 
import './Search.css';
import Searchimg from './search.png';

function Search() {
  return (
    <div class="container">
      <div class="searchbox">
        <input type="text" class="searchtext" name="" placeholder="Enter Keyword or Query.."></input>
        <img class="searchimg" src={Searchimg} alt="Search"/>
      </div>
      <div class="searchdiv"><button class="searchbutton">Search</button></div>
    
    </div>
  );
}

export default Search;
