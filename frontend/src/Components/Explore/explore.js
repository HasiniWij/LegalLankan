import React from 'react'; 
import './explore.css';
import {BrowserRouter as Router, NavLink, Route} from 'react-router-dom';

export const Explore = () => { 
    return (
        <div class="catDiv">
            <div className="categorylist">
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/family", 
                    state: { urlfull: "http://127.0.0.1:5000/legislationlist/family", title:"FAMILY" }}}>FAMILY
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/rights",
                    state: { urlfull: "http://127.0.0.1:5000/legislationlist/rights", title:"RIGHTS" }}}>RIGHTS
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/crime",
                    state: { urlfull: "http://127.0.0.1:5000/legislationlist/crime", title:"CRIME" }}}>CRIME
                    </NavLink>
                </div>
                <div className="catitems">
                    <NavLink activeClassName="activee" className="catlink" to={{pathname:"/explore/employment",
                    state: { urlfull: "http://127.0.0.1:5000/legislationlist/employment", title:"EMPLOYMENT" }}}>EMPLOYMENT
                    </NavLink>
                </div>
            </div>
        {/* <MenuAnswer></MenuAnswer> */}
        </div>
    );
  }
