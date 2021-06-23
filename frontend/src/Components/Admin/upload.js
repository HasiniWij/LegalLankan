import React, {useState} from 'react'; 
import './admin.css';
import { useHistory } from 'react-router-dom';
import {BrowserRouter as Router, Link, NavLink, Route} from 'react-router-dom';

function Upload() {
  const [test, setTest]=useState('');
  const [textFile, setTextFile]=useState('');
  const [fileError, setFileError]=useState('');
  const [type, setType]=useState('');
  const [title, setTitle]=useState('');
  const history = useHistory();
  
  const fileType=['text/plain'];
  const handleFileChange=(e)=>{
    let selectedFile=e.target.files[0];
    if (selectedFile){
      if (selectedFile&&fileType.includes(selectedFile.type)){
        let filereader =new FileReader();
        
        filereader.readAsText(selectedFile);
        console.log(selectedFile.name);
        setTitle(selectedFile.name);
        filereader.onloadend=(e)=>{
          
          setTextFile(e.target.result);
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
  function onChangeValue(e) {
    setType(e.target.value)
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (textFile!==""){
      setTest("submit working");
      history.push({pathname:'/admin/confirm',state: {data:{ text: textFile, title:title, type:type}, textFile:textFile }})
      console.log(type)
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
        <div onChange={onChangeValue}>
          <div  className="radiobtns"><input type="radio" value="act" name="type" checked /> Act</div>
          <div  className="radiobtns"><input type="radio" value="core" name="type" /> Core</div>
        </div>
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