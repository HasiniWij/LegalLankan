import React, { Component, useState} from 'react'; 
import './search.css';
import Searchimg from './search.png';
import { BrowserRouter as Router, Route} from 'react-router-dom';
import { useHistory } from 'react-router-dom';


export const Search = () => {
    const [data,setData]=useState(null);
    function getData(val){
        setData(val.target.value)
        console.log(val.target.value)
    }
    const history = useHistory();
    // const handleHis=()=>{
    //     //history.push({pathname:'/answer',state: { url: "http://localhost:5000/search/", q:data }});
    //     //history.push({pathname:'/answer',state: { url: "https://jsonplaceholder.typicode.com/posts", q:data }});
    //     history.push({pathname:'/answer',state: { urlfull: "http://localhost:5000/search/"+data }});
    // };
    return (
        <div className="container">
            <form>
                <div className="searchbox">
                    <input type="text" className="searchtext" onChange={getData}
                    name="query" placeholder="Enter Keyword or Query.."></input>
                    <div className="searchimgdiv"><img className="searchimg" src={Searchimg} alt="Search"/></div>
                </div>
                 <div className="searchdiv"><button className="searchbutton" 
                 onClick={() => {history.push({pathname:'/answer',state: { urlfull: "https://legallankanapi.azurewebsites.net/search/"+data, query:data }}) }}>
                 Search</button></div>
            </form>
        </div>
      );
}
