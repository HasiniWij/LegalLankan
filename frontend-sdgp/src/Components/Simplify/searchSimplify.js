import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';

export class SearchSimplify extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            errormsg:"",
            urfull:"",
            index3:"",
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({index3:this.props.location.state.in});
        })
        .catch(error =>{
            console.log(error)
            this.setState({urfull:this.props.location.state.urlfull}) //test
            this.setState({errormsg:"Invalid Request"})
        })
    }
    render(){
        const {index3,posts,urfull} = this.state
        return (
         <div>
             { index3? <div>{index3}</div> : null} 
             { urfull? <div>{urfull}</div> : null} 
             {
                 posts.length ?
                 posts.map(post => <div key={post.pieceIndex}>
                    {post.pieceTitle}
                    {post.content}
                     </div>) :
                 null
             }
            SearchSimplify
        </div>
    )
    }
}
export default SearchSimplify
