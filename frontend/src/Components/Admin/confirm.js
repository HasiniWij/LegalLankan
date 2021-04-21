import React, { Component} from 'react'; 
import axios from 'axios';
import './admin.css';
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';

export class Confirm extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:"",
            data:"",
            textFile:"",
            success:""
        }
    }
    componentDidMount(){
        axios.post('http://127.0.0.1:5000/uploadLeg', this.props.location.state.data)
        .then(response =>{
            console.log(response)
            this.setState({posts: response.data})
            this.setState({success:'FILE SUCCESSFULLY UPLOADED'})
        })
            .catch(error =>{
                this.setState({success:'FILE UPLOAD FAILED'})
            })
       
    }
    

    render(){
        const {success} = this.state
            return (
                <div className="confirmcon">
                  {success?
                  <div>
                      <div className="confirmtext">{success}</div>
                      <div><Link className="uplink" to ={{pathname:"/admin/upload"}}>UPLOAD AGAIN</Link></div>
                  </div>:
                  <div>
                  <div className="loader"></div>
                  <div className="loadermsg">PLEASE WAIT..</div>
                 </div>}
               </div>

           )
        }
}
export default Confirm