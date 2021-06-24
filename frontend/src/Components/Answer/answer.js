import React, { Component} from 'react'; 
import './answer.css';
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';

export class Answer extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            errormsg:"",
            query:"",
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({query:this.props.location.state.query})
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"Invalid Request"})
        })
    }

    render(){
        const {posts, errormsg, query} = this.state
        return (
         <div className="searchans">
             { errormsg? <div className="seatitle">{errormsg}</div> : null}
             <h4><div className="seatitle">Results: {query}</div></h4>
             {
                 posts.length ?
                 posts.map(post => <div className="spieces" key={post.title}>
                     <h5><span style={{ color:"rgba(182,166,139,1)", }}>{post.title} </span><br/></h5>
                     <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{post.content}</span>
                    <div className="searchlinks">
                
                    <button className="searchbutton1 searchdiv1"  id="fullLegButton">

                        <Link className="menulinks"  to ={{pathname:"/legislation",
                            state:{urlfull: "http://127.0.0.1:5000/legislation/"+post.title,
                            in:post.title, name:post.title}}}>
                                SEE FULL LEGISLATION
                        </Link>

                    </button>




                    </div>
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
export default Answer
