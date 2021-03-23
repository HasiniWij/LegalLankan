import React from 'react'; 
import './explore.css';
import { MenuAnswer } from '../Answer/menuAnswer';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

export const Explore = () => {
    return (
        <div>
            <div class="categorylist">
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/family", 
                    state: { urlfull: "http://localhost:5000/legistlationlist/FA", title:"Family" }}}>FAMILY
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/rights",
                    state: { urlfull: "http://localhost:5000/legistlationlist/RI", title:"Rights" }}}>RIGHTS
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/crime",
                    state: { urlfull: "http://localhost:5000/legistlationlist/CR", title:"Crime" }}}>CRIME
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/employment",
                    state: { urlfull: "http://localhost:5000/legistlationlist/EM", title:"Employment" }}}>EMPLOYMENT
                    </Link>
                </div>
            </div>
        </div>
    );
  }
