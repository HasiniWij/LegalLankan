import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Admin from './Components/Admin/admin'
import Process from './Components/Admin/process';
import Upload from './Components/Admin/upload';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter as Router, NavLink, Route, Redirect, Switch} from 'react-router-dom';


ReactDOM.render(
  <React.StrictMode>
    <Router>
    <Route exact path="/"
                render={() => {
                    return (<Redirect to="/home" />)
                }}
              />
      <Route exact path='/home' component={App}/>
      <Route exact path='/admin' component={Admin}/>
      <Route path='/admin/process' component={Process}/>
      <Route path='/admin/upload' component={Upload}/>
    </Router>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
