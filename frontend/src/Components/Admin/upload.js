import React, {useState} from 'react'; 
import './admin.css';

function Upload() {
  const [pdfFile, setPdfFile]=useState(null);
  const [pdfFileError, setPdfFileError]=useState('');

  const [viewPdf, setViewPdf]=useState(null);
  const [test, setTest]=useState('');

  const fileType=['application/pdf'];
  const handlePdfFileChange=(e)=>{
    let selectedFile=e.target.files[0];
    if (selectedFile){
      if (selectedFile&&fileType.includes(selectedFile.type)){
        let reader =new FileReader();
        reader.readAsDataURL(selectedFile);
        reader.onloadend = (e) =>{
          setPdfFile(e.target.result);
          setPdfFileError('');
        }
      }
      else{
        setPdfFile(null);
        setPdfFileError('Please select valid pdf file');
      }
    }
    else{
      console.log('select your file');
    }
  }

  const handleSubmit=(e)=>{
    e.preventDefault();
    if (pdfFile!==null){
      setViewPdf(pdfFile);
      setTest("submit working");
    }
    else{
      setViewPdf(null);
    }
  }

    return (
      <div className="uploadcon">
        <form>
          <input type="file" required onChange={handlePdfFileChange}/>
          {pdfFileError&&<div>{pdfFileError}</div>}
          <div>
            <button onClick={handleSubmit}>UPLAOD PDF</button>
          </div>
        </form>
        <div>
          {test&&<div>{test}</div>}
        </div>
    </div>
    );
  }
  export default Upload;