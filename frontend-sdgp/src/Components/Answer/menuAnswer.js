import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';
import './answer.css';

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
        //axios.get(this.props.location.state.url+this.props.location.state.q)
        //axios.get(this.props.location.state.url)
        //axios.get("https://jsonplaceholder.typicode.com/posts")
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
             { title? <div className="menutitle">{title}</div> : null}
             { errormsg? <div className="menutitle">{errormsg}</div> : null}
             {
                 posts.length ?
                 posts.map(post => <div class="leglist" key={post.legislationIndex}>
                     <Link className="menulinks" to ={{pathname:"/legislation", 
                     state:{urlfull: "http://localhost:5000/legislation/"+post.legislationIndex, 
                     in:post.legislationIndex, name:post.legislationName}}}>
                     - {post.legislationName} 
                     </Link>
                     </div>) :
                 null
             }
        </div>
    )
    }
}
export default MenuAnswer
