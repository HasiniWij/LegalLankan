import React, { useState}  from 'react';
import './home.css';
import {BrowserRouter as Router, Link} from 'react-router-dom';
import Searchimg from './search.png';
import { useHistory } from 'react-router-dom';
import {Row,Col} from 'reactstrap';
export const Home = ()=> {
    const [data,setData]=useState(null);
    function getData(val){
        setData(val.target.value)
        console.log(val.target.value)
    }
    const history = useHistory();
    return (
        <div className="container">
            
            <div id="bigTopic">
                <h1 id="topic1"> Unlimited movies, TV shows, and more.</h1>
                <h3>Watch anywhere. Cancel anytime.</h3>
        {/* <div class="widthDiv"> */}

        

        <form>
        <Row>

        <Col  md={{ size: 5, offset: 3}}>

        <div className="searchbox">
               <input type="text" className="searchtext" onChange={getData} name="query" placeholder="Ask a Question...">
               </input></div>
        </Col>
        <Col md={{ size: 1 }}>

        <div className="searchdiv">
                <button className="searchbutton searchdiv" 
            onClick={() => {history.push({pathname:'/answer',state: { urlfull: "http://127.0.0.1:5000/search/"+data, query:data }}) }}>
            Search</button>
          </div>
        </Col>
           

           {/* <div className="searchbox">
               <input type="text" className="searchtext" onChange={getData} name="query" placeholder="Ask a Question...">
               </input>
               <div className="searchdiv">
                <button className="searchbutton searchdiv" 
            onClick={() => {history.push({pathname:'/answer',state: { urlfull: "http://127.0.0.1:5000/search/"+data, query:data }}) }}>
            Search</button>
          </div> */}
           
         
        </Row>
       </form>



       
        
          
            </div>
        </div>
        // </div>
      );
}
export default Home