import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';
import './simplify.css';

export class Simplify extends Component {
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
        const {posts,errormsg,content,title,legno,name} = this.state
        return (
         <div className="simplifycon">
             { errormsg? <div className="simtitle">{errormsg}</div> : null}
             <div className="simtext">
             <div className="original">
                 <div className="simtitle">ORIGINAL</div>
                 <div style={{width: "90%", margin:"0 auto", }}>
                { title? <div style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{title}</div> : null}
                { content? <div style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{content}</div> : null}
                </div>
             </div>
             <div className="simplified">
             <div className="simtitle">SIMPLIFIED</div>
                { posts? <div style={{width: "90%", margin:"0 auto", }}>
                <div style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{posts.pieceTitle}</div>
                 <div style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{posts.content}</div>
                </div> : null} 
             </div>
             </div>
              
             <div className="goback">GO BACK TO - 
             <Link className="goblink" to ={{pathname:"/legislation", 
                     state:{urlfull: "https://legallankanbackend.azurewebsites.net/legislation/"+legno,
                     in:legno, name:name}}}> {name}</Link>
             </div>             
        </div>
    )
    }
}
export default Simplify
