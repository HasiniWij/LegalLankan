import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';
import './display.css';
import { Button, Popover, PopoverHeader, PopoverBody } from 'reactstrap';

export class Display extends Component {
    constructor(props){
        super(props)
        this.state={
            posts:[],
            block:[],
            complex:[],
            errormsg:"",
            urfull:"",
            legno:"",
            name:"",
            isModalOpen: false,
            simpleWord:""
            
        }
        this.toggleModal = this.toggleModal.bind(this);
        this.hello=this.hello.bind(this);
    }
    toggleModal() {
        this.setState({
          isModalOpen: !this.state.isModalOpen
        });
      }

    componentDidMount(){
        axios.get(this.props.location.state.urlfull)
        .then(response =>{
            console.log(response)
            console.log(response.data.block)
            console.log("sbb"+response.data.complexWords)
            this.setState({posts: response.data})
            this.setState({block: response.data.block})
            this.setState({complex: response.data.complexWords})
            this.setState({name:this.props.location.state.name})
        
        })
        .catch(error =>{
            console.log(error)
            this.setState({errormsg:"Invalid Request"})
        })
    }

    hello(word,content){
        
        
        this.setState({ simpleWord:"loading..."})

        var splitContent=content
        var chosenSent=""

        splitContent.split(".").map(sentence => {
            if (sentence.includes(word)) {
                chosenSent = sentence
            }
        })


        axios.get('http://localhost:5000/simplifiedWord/'+word+"/"+chosenSent)
      .then(response => {
          console.log(response)
          this.setState({ simpleWord:response.data})
        
         
          // this.setState({simpleWords: })
        //  console.log("sim "+this.state.simpleWords)
      })
      .catch(error => {
          console.log(error)
      })
  
    }


    render(){
        const {errormsg,posts,legno,name,block,complex} = this.state
        return (
             <div className="legcon">
             { errormsg? <div className="legtitle">{errormsg}</div> : null}
             { name? <div className="legtitle">{name}</div> : null} 
            {
                 block.length ?
                 block.map(block => 


                 <div className="legpiece" key={block.content}>
                      { 
                       console.log(block.title.split(" ")),
                       block.title.split(" ").map(text => {
                        // return text.toUpperCase() === "ACCOUNT" ? 
                        return complex.includes(text) ?
                        <span>
                        <Link id="titleComplexWord" onClick={() => this.hello(text,block.title)}>{text} </Link>

                        <Popover isOpen={this.state.isModalOpen} toggle={this.toggleModal} 
                        placement="top"  target="titleComplexWord">
                            
                            
                            {this.state.simpleWord}
                        
                        
                        </Popover>
                      

                        </span>
                         : 
                        <span style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{text} </span>;
    
                     })}
                     <br/>

{ 
                       console.log(block.content.split(" ")),
                       block.content.split(" ").map(text => {
                        // return text.toUpperCase() === "SECTION" ? 
                        return complex.includes(text) ?
                        <span>
                        <Link id="TooltipExample" onClick={() => this.hello(text,block.content)}>{text} </Link>

                        <Popover isOpen={this.state.isModalOpen} toggle={this.toggleModal} 
                        placement="top"  target="TooltipExample">
                            
                            
                            {this.state.simpleWord}
                        
                        
                        </Popover>
                      

                        </span>
                         : 
                        <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{text} </span>;
    
                     })}
                     

                     {/* <div className="menutext">
                        <span style={{fontSize: "16px", color:"rgba(182,166,139,1)", }}>{block.title} </span><br/>

                        <span style={{fontSize: "15px", color:"white", marginTop:"4px"}}>{block.content} </span>
                     </div> */}

                    

                        {/* <NavLink className="menulink" to={{pathname:`/simplify/${post.pieceIndex}`, state:{urlfull:"http://127.0.0.1:5000/simplifiedpiece/"+post.pieceIndex,
                        pindex:post.pieceIndex, content:post.content, title:post.pieceTitle, legno:legno,name:name}}}>
                         SIMPLIFY</NavLink> */}
                     
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
