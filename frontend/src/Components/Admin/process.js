import axios from 'axios';
import React, { Component, useState} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import './admin.css';

export class Process extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:"",
            userdata:"",
            user:""
        }
    }
    componentDidMount(){
        axios.post('http://127.0.0.1:5000/login', this.props.location.state.userdata)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({user:this.props.location.state.user})
        })
            .catch(error =>{
                console.log(error)
            })
       
    }
    

    render(){
        const {posts,user} = this.state
            return (
                <div >
                    <div>
                        {(() => {
                        if (posts==="Signing in...") {
                        return (
                            <div className="processcon">
                                { user? <div className="succmsg">{user} - Successfully Logged In!</div> : null}
                                   <div> <Link className="uplink" to ={{pathname:"/admin/upload"}}>UPLOAD DOCUMENT</Link></div>
                            </div>
                        )
                        } else if (posts==="") {
                            return (
                                <div className="processcon"> 
                                    <div className="loader"></div>
                                    <div className="loadermsg">PLEASE WAIT..</div>
                                </div>
                            )
                        }else {
                        return (
                            <div className="processcon">
                                <div className="succmsg">Invalid Details. Try Again</div>
                                <Link className="uplink" to ={{pathname:"/admin"}}>LOG IN</Link>
                            </div>
                        )
                        }
                        })()}
                    </div>
               </div>

           )
        }
}
export default Process

