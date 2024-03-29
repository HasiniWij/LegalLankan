import React, {useState} from 'react'; 
import './admin.css';
import Logo from '../../images/logo.png';
import { useHistory } from 'react-router-dom';

function Admin() {
    const [user,setUser]=useState(null);
    const [pass,setPass]=useState(null);
    function getUser(val){
        setUser(val.target.value)
    }
    function getPass(val){
        setPass(val.target.value)
    }
    const history = useHistory();
    
    return (
      <div className="logincon">
        <form class ="adminForm" autocomplete ="off">
        <div className="formimgdiv">
            <img className="formimg" src={Logo} alt="Logo"/>
        </div>
        <div className="forminputs">
            <label className="labels"> USERNAME <span className="star">*</span></label>
            <input type="text" name="userName" onChange={getUser} className="input" placeholder="USERNAME" required/>
        </div>

        <div className="forminputs">
            <label className="labels"> PASSWORD <span className="star">*</span></label>
            <input type="password" name="password" onChange={getPass} className="input" placeholder="PASSWORD" required/>
        </div>
        <div className="loginbuttondiv">
            <button className="loginbutton" 
             onClick={() => {history.push({pathname:'/admin/process',state: { user:user,userdata:{ userName: user, password:pass } }}) }}>
                LOG IN</button>
        </div>

        </form>
    </div>
    );
  }
  export default Admin;