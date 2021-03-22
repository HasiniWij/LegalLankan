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
            tit:"",
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
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({title:this.props.location.state.title})
        })
        .catch(error =>{
            console.log(error)
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {posts, errormsg,urfull,title} = this.state
        return (
         <div>
             { title? <div>{title}</div> : null}
             { urfull? <div>{urfull}</div> : null} 
             {
                 posts.length ?
                 posts.map(post => <div class="leglist" key={post.legislationIndex}>
                     <Link to ={{pathname:"/legislation", 
                     state:{urlfull: "http://localhost:5000/legislation/"+post.legislationIndex, in:post.legislationIndex}}}>
                     {post.legislationName} 
                     {post.legislationIndex}
                     </Link>
                     </div>) :
                 null
             }
             { errormsg? <div>{errormsg}</div> : null}
        </div>
    )
    }
}
export default MenuAnswer
