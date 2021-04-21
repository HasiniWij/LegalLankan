import React, { useState} from 'react'; 
import './search.css';
import Searchimg from './search.png';
import { useHistory } from 'react-router-dom';


export const Search = () => {
    const [data,setData]=useState(null);
    function getData(val){
        setData(val.target.value)
        console.log(val.target.value)
    }
    const history = useHistory();
    return (
        <div className="container">
            <form>
                <div className="searchbox">
                    <input type="text" className="searchtext" onChange={getData}
                    name="query" placeholder="Ask a Question..."></input>
                    <div className="searchimgdiv"><img className="searchimg" src={Searchimg} alt="Search"/></div>
                </div>
                 <div className="searchdiv"><button className="searchbutton" 
                 onClick={() => {history.push({pathname:'/answer',state: { urlfull: "http://127.0.0.1:5000/search/"+data, query:data }}) }}>
                 Search</button></div>
            </form>
        </div>
      );
}
export default Search