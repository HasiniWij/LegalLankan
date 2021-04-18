import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';
import './display.css';

export class Display extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
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
            this.setState({posts: response.data})
            this.setState({legno:this.props.location.state.in})
            this.setState({name:this.props.location.state.name})
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {errormsg,posts,legno,name} = this.state
        return (
             <div className="legcon">
             { errormsg? <div className="legtitle">{errormsg}</div> : null}
             { name? <div className="legtitle">{name}</div> : null} 
            {
                 posts.length ?
                 posts.map(post => 
                 <div className="legpiece" key={post.legislationIndex}>
                     <div className="menutext">
                        <span style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{post.pieceTitle} </span><br/>
                        <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{post.content} </span>
                     </div>
                        <NavLink className="menulink" to={{pathname:`/simplify/${post.pieceIndex}`, state:{urlfull:"https://legallankanbackend.azurewebsites.net/simplifiedpiece/"+post.pieceIndex, 
                        pindex:post.pieceIndex, content:post.content, title:post.pieceTitle, legno:legno,name:name}}}>
                         SIMPLIFY</NavLink>
                     
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
