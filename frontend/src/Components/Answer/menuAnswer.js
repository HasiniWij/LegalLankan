import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';
import './menuAnswer.css';
import 'bootstrap/dist/css/bootstrap.css';
import { Button } from 'reactstrap';

export class MenuAnswer extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            errormsg:"",
            title:"",
            urfull:"",
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({title:this.props.location.state.title})
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"NOTHING TO SHOW HERE"})
        })
    }
    render(){
        const {posts, errormsg,title} = this.state
        return (
         <div className="menuans">
             <h2>{ title? <div className="menutitle">{title}</div> : null}</h2>
             { errormsg? <div className="menutitle">{errormsg}</div> : null}
             {
                 posts.length ?
                 posts.map(post => <div class="leglist" key={post.title}>
                <button type="button" class="btn"  id="id">

                    <Link className="menulinks" to ={{pathname:"/legislation",
                        state:{urlfull: "http://127.0.0.1:5000/legislation/"+post.title,
                        in:post.title, name:post.title}}}>
                            {post.title}
                     </Link>

                 </button>
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
export default MenuAnswer
