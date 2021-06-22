import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';
import './display.css';

export class Display extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            block:[],
            complex:[],
            errormsg:"",
            urfull:"",
            legno:"",
            name:"",
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            console.log(response.data.block)
            console.log("sbb"+response.data.complexWords)
            this.setState({posts: response.data})
            this.setState({block: response.data.block})
            this.setState({complex: response.data.complexWords})
            this.setState({name:this.props.location.state.name})
        
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {errormsg,posts,legno,name,block,complex} = this.state
        return (
             <div className="legcon">
             { errormsg? <div className="legtitle">{errormsg}</div> : null}
             { name? <div className="legtitle">{name}</div> : null} 
            {
                 block.length ?
                 block.map(block => 


                 <div className="legpiece" key={block.content}>
                      { 
                       console.log(block.title.split(" ")),
                       block.title.split(" ").map(text => {
                        // return text.toUpperCase() === "ACCOUNT" ? 
                        return complex.includes(text.toUpperCase()) ?
                         <Link >{text} </Link> : 
                        <span style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{text} </span>;
    
                     })}
                     <br/>

{ 
                       console.log(block.content.split(" ")),
                       block.content.split(" ").map(text => {
                        // return text.toUpperCase() === "SECTION" ? 
                        return complex.includes(text.toUpperCase()) ?
                        <Link >{text} </Link> : 
                        <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{text} </span>;
    
                     })}
                     

                     {/* <div className="menutext">
                        <span style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{block.title} </span><br/>

                        <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{block.content} </span>
                     </div> */}

                    

                        {/* <NavLink className="menulink" to={{pathname:`/simplify/${post.pieceIndex}`, state:{urlfull:"http://127.0.0.1:5000/simplifiedpiece/"+post.pieceIndex,
                        pindex:post.pieceIndex, content:post.content, title:post.pieceTitle, legno:legno,name:name}}}>
                         SIMPLIFY</NavLink> */}
                     
                </div>) :
                <div>
                    <div className="loader"></div>
                    <div className="loadermsg">PLEASE WAIT..</div>
                </div>
             }
             </div>
    )
    }
}
