import React, { Component} from 'react'; 
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';
import axios from 'axios';
import './display.css';
import {  UncontrolledPopover, PopoverBody } from 'reactstrap';

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
            isTitleOpen: false,
            simpleWord:"",
            simpleTitle:""
            
        }
        this.toggleModal = this.toggleModal.bind(this);
        this.toggleTitle = this.toggleTitle.bind(this);
        this.simplifyWords=this.simplifyWords.bind(this);
        this.simplifyTitle=this.simplifyTitle.bind(this);
    }
    toggleModal() {
        this.setState({
          isModalOpen: !this.state.isModalOpen
        });
      }
      toggleTitle() {
        this.setState({
            isTitleOpen: !this.state.isTitleOpen
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

    simplifyWords(word,content){
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
      })
      .catch(error => {
          console.log(error)
      })
  
    }

    simplifyTitle(word,content){
        this.setState({ simpleTitle:"loading..."})

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
          this.setState({ simpleTitle:response.data})
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
                    
                        return complex.includes(text) ?
                        <span>
                        <Link className="LinkStyleStyle"  id="titleComplexWord" onClick={() => this.simplifyTitle(text,block.title)}>{text} </Link>

                         <UncontrolledPopover placement="top"  target="titleComplexWord" trigger="focus">
                            <PopoverBody>
                                {this.state.simpleTitle}
                            </PopoverBody> 
                        </UncontrolledPopover>

                        </span>
                         : 
                        <span style={{fontSize: "16px", color:"rgba(169,121,46,1)", fontWeight: "bold" }}>{text} </span>;
    
                     })}
                     <br/>

{ 
                       console.log(block.content.split(" ")),
                       block.content.split(" ").map(text => {
                        return complex.includes(text) ?
                        <span>
                        <Link className="LinkStyle" id="TooltipExample" onClick={() => this.simplifyWords(text,block.content)}>{text} </Link>

                            <UncontrolledPopover placement="top"  target="TooltipExample" className="popoverStyle" trigger="focus">
                                <PopoverBody>
                                    {this.state.simpleWord}
                                </PopoverBody>
                            </UncontrolledPopover>
   
                        </span>
                         : 
                        <span style={{fontSize: "15px", color:"#cfcfca", marginTop:"4px"}}>{text} </span>;

                     })}
                     
                     
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
