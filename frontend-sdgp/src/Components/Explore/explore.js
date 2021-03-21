import React from 'react'; 
import './explore.css';
import { MenuAnswer } from '../Categories/menuAnswer';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

export const Explore = () => {
    return (
        <Router>
        <div>
            <div class="categorylist">
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/family",
                    state: { urlfull: "https://jsonplaceholder.typicode.com/posts", title:"Family" }}}>FAMILY
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/rights",
                    state: { urlfull: "https://jsonplaceholder.typicode.com/posts", title:"Rights" }}}>RIGHTS
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/crime",
                    state: { urlfull: "https://jsonplaceholder.typicode.com/posts", title:"Crime" }}}>CRIME
                    </Link>
                </div>
                <div class="catitems">
                    <Link class="catlink" to={{pathname:"/explore/employment",
                    state: { urlfull: "https://jsonplaceholder.typicode.com/posts", title:"Employment" }}}>EMPLOYMENT
                    </Link>
                </div>
            </div>
            <div class="content">
                <Route path='/explore/family' component={ MenuAnswer }/>
                <Route path='/explore/rights' component={ MenuAnswer }/>
                <Route path='/explore/crime' component={ MenuAnswer }/>
                <Route path='/explore/employment' component={ MenuAnswer }/>
            </div>
        </div>
        </Router>
    );
  }
