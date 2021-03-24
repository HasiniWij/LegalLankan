import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';
import './display.css';

export class MenuDis extends Component {
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
            // this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {errormsg,posts,legno,name} = this.state
        return (
             <div className="piecelist">
             { errormsg? <div>{errormsg}</div> : null}
             { name? <div className="legtitle">{name}</div> : null} 
            {
                 posts.length ?
                 posts.map(post => 
                 <div className="pieces" key={post.legislationIndex}>
                     <div className="mentext">
                        <span>{post.pieceTitle} </span><br/>
                        <span>{post.content} </span>
                     </div>
                     <div className="mensib">
                        <NavLink to={{pathname:`/simplify/${post.pieceIndex}`, state:{urlfull:"http://localhost:5000/simplifiedpiece/"+post.pieceIndex, 
                        pindex:post.pieceIndex, content:post.content, title:post.pieceTitle, legno:legno,name:name}}}>
                         Simplify</NavLink>
                     </div>
                     
                        {/* <div style={{fontSize: "17px", color:"grey"}}>{post.pieceTitle} </div>
                        <div style={{fontSize: "15px", color:"white"}}>{post.content}</div> */}
    
                   
                </div>) :
                 null
             }
             </div>
    )
    }
}
