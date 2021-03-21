import React, { Component} from 'react'; 
import './answer.css';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';

export class Answer extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            errormsg:"",
            ur:"",
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
            this.setState({ur:this.props.location.state.url+this.props.location.state.q}) //test
            this.setState({urfull:this.props.location.state.urlfull}) //test
        })
        .catch(error =>{
            console.log(error)
            this.setState({ur:this.props.location.state.url+this.props.location.state.q}) //test
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({errormsg:"Invalid Request"})
        })
    }

    render(){
        const {posts, errormsg, ur,urfull} = this.state
        return (
         <div>
            {/*  test */}
             { ur? <div>{ur}</div> : null} 
             { urfull? <div>{urfull}</div> : null} 
             Results:
             {
                 posts.length ?
                 posts.map(post => <div key={post.pieceIndex}>
                     {post.content}
                     {post.legislationIndex}
                     {post.legislationName}
                     {post.pieceIndex}
                     {post.pieceTitle}
                    </div>) :
                 null
             }
             { errormsg? <div>{errormsg}</div> : null}
        </div>
    )
    }
}
export default Answer
