import React from 'react'; 
import './explore.css';
import { MenuAnswer } from '../Answer/menuAnswer';
import {BrowserRouter as Router, NavLink, Route} from 'react-router-dom';

export const Explore = () => { 
    return (
        <div>
            <div className="categorylist">
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/family", 
                    state: { urlfull: "http://localhost:5000/legistlationlist/FA", title:"FAMILY" }}}>FAMILY
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/rights",
                    state: { urlfull: "http://localhost:5000/legistlationlist/RI", title:"RIGHTS" }}}>RIGHTS
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/crime",
                    state: { urlfull: "http://localhost:5000/legistlationlist/CR", title:"CRIME" }}}>CRIME
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/employment",
                    state: { urlfull: "http://localhost:5000/legistlationlist/EM", title:"EMPLOYMENT" }}}>EMPLOYMENT
                    </NavLink>
                </div>
            </div>
        </div>
    );
  }
