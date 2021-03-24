import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';
import './simplify.css';

export class MenuSimplify extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            errormsg:"",
            pindex:"",
            urfull:"",
            content:"",
            title:"",
            legno:"",
            name:"",
        }
    }
    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({pindex:this.props.location.state.pindex})
            this.setState({urfull:this.props.location.state.urlfull})
            this.setState({content:this.props.location.state.content})
            this.setState({title:this.props.location.state.title})
            this.setState({name:this.props.location.state.name})
            this.setState({legno:this.props.location.state.legno})
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"NOTHING TO SHOW HERE"})
        })
    }
    
    render(){
        const {pindex,posts,urfull,errormsg,content,title,legno,name} = this.state
        return (
         <div className="menusim">
              { pindex? <div>{pindex}</div> : null} 
             { urfull? <div>{urfull}</div> : null} 
             { errormsg? <div>{errormsg}</div> : null}
             { title? <div>{title}</div> : null}
             { content? <div>{content}</div> : null}
             { posts? <div>
                 <div>{posts.content}</div>
             <div>{posts.pieceTitle}</div>
             </div> : null}  
             <Link to ={{pathname:"/legislation", 
                     state:{urlfull: "http://localhost:5000/legislation/"+legno, 
                     in:legno, name:name}}}>Go back to legislation</Link>
             
        </div>
    )
    }
}
export default MenuSimplify
