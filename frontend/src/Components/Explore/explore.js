import React from 'react'; 
import './explore.css';
import {BrowserRouter as Router, NavLink, Route} from 'react-router-dom';

export const Explore = () => { 
    return (
        <div>
            <div className="categorylist">
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/family", 
                    state: { urlfull: "https://legallankanbackend.azurewebsites.net/legislationlist/FA", title:"FAMILY" }}}>FAMILY
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/rights",
                    state: { urlfull: "https://legallankanbackend.azurewebsites.net/legislationlist/RI", title:"RIGHTS" }}}>RIGHTS
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/crime",
                    state: { urlfull: "https://legallankanbackend.azurewebsites.net/legislationlist/CR", title:"CRIME" }}}>CRIME
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/employment",
                    state: { urlfull: "https://legallankanbackend.azurewebsites.net/legislationlist/EM", title:"EMPLOYMENT" }}}>EMPLOYMENT
                    </NavLink>
                </div>
            </div>
        </div>
    );
  }
