import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';
import axios from 'axios';
import SearchSimplify from '../Simplify/searchSimplify';

export class SearchDis extends Component {
    constructor(props){
        super(props)
        this.state={
            index:"",
            content:"",
            name:"",
            title:""
        }
    }
    componentDidMount(){
            this.setState({index:this.props.location.state.index}) 
            this.setState({content:this.props.location.state.content}) 
            this.setState({name:this.props.location.state.name}) 
            this.setState({title:this.props.location.state.title}) 
    }
    render(){
        const {index, content, name, title} = this.state
        return (
         <div className="searchcon">
             <Link to ={{pathname:"/piece/simplify", state:{urlfull:"http://localhost:5000/simplifiedpiece/"+index,in:index}}}>Simplify</Link>
            { index? <div>{index}</div> : null} 
            { content? <div>{content}</div> : null} 
            { name? <div>{name}</div> : null} 
            { title? <div>{title}</div> : null} 
        </div>
    )
    }
}
export default SearchDis
