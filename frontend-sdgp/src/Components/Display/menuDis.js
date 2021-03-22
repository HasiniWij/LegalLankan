import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
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
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({legno:this.props.location.state.in})
            this.setState({urfull:this.props.location.state.urlfull}) //test
        })
        .catch(error =>{
            console.log(error)
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {urfull,posts,legno} = this.state
        return (
        <div>
         <div class="menuCon">
             { urfull? <div>{urfull}</div> : null} 
             { legno? <div>{legno}</div> : null} 
             <Link to ={{pathname:"/legislation/simplify", state:{urlfull:"http://localhost:5000/simplifiedleg/"+legno,in:legno}}}>Simplify</Link>
            {
                 posts.length ?
                 posts.map(post => <div key={post.legislationIndex}>
                     {post.pieceTitle} 
                     {post.content}
                     </div>) :
                 null
             }
        </div>
        </div>
    )
    }
}
export default MenuDis
