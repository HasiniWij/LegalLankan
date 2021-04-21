import React, {useState} from 'react'; 
import './admin.css';
import { useHistory } from 'react-router-dom';
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';

function Upload() {
  const [test, setTest]=useState('');
  const [textFile, setTextFile]=useState('');
  const [fileError, setFileError]=useState('');
  const history = useHistory();
  
  const fileType=['text/plain'];
  const handleFileChange=(e)=>{
    let selectedFile=e.target.files[0];
    if (selectedFile){
      if (selectedFile&&fileType.includes(selectedFile.type)){
        let filereader =new FileReader();
        filereader.readAsText(selectedFile);
        filereader.onloadend=(e)=>{
          setTextFile(e.target.result);
          console.log(e.target.result)
        }
        setFileError('');
      }
      else{
        setTextFile("");
        setFileError('INVALID FILE FORMAT');
      }
    }
    else{
      console.log('select your file');
    }
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (textFile!==""){
      setTest("submit working");
      history.push({pathname:'/admin/confirm',state: { data:{ text: textFile }, textFile:textFile }})
      setTest("")
    }
    else{
      setTest("PLEASE SELECT A TEXT FILE");
    }
  }
 

    return (
      <div className="uploadcon">
        <div className="uploadtitle">UPLOAD TEXT FILE</div>
        <form>
        <div class="upload-btn-wrapper">
          <input type="file"  className="fileinput" required onChange={handleFileChange} />
        </div>
        {fileError ?<div className="fileerror">{fileError}</div>:<div></div>}
          <div>
            <button className="uploadbtn" onClick={handleSubmit}>UPLOAD</button>
          </div>
        </form>
        <div>
          {test&&<div className="fileerror">{test}</div>}
        </div>
    </div>
    );
  }
  export default Upload;