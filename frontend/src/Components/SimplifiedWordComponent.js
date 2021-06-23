import { Button, Row, Col, Label , Modal, ModalHeader, ModalBody,} from 'reactstrap';
import React, { Component } from 'react';
import { Tooltip } from 'reactstrap';





class SimplifiedWord extends Component {

    constructor(props) {
        super(props);
        this.state = {
            isTooltipOpen: false    
        };
      }
    //   const [tooltipOpen, setTooltipOpen] = useState(false);

      toggleTootip() {
        this.setState({
          isTooltipOpen: !this.state.tooltip
        });
      }

      
      render(){
        return(
            console.log("text: "+this.props.text),
            
            <div>
               
               <p style={{color: "red"}} href='#' id="TooltipExample">{ this.props.text} test </p>
                {/* <p>Somewhere in here is a <span style={{textDecoration: "underline", color:"blue"}} href="#" id="TooltipExample">tooltip</span>.</p> */}
                <Tooltip isOpen={this.state.isModalOpen} toggle={this.toggleTootip} placement="right"  target="TooltipExample" >
                    Hello world!
                </Tooltip>
            </div>
                    
        );
    
    
    
    }

}
export default SimplifiedWord;