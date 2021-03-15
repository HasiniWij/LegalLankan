import React from 'react'; 
import './explore.css';
import { Family } from '../Categories/family';
import { Crime } from '../Categories/crime';
import { Rights } from '../Categories/rights';
import { Employment } from '../Categories/employment';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

export const Explore = () => {
    return (
        <Router>
        <div>
            <div class="categorylist">
                <div class="catitems">
                    <Link class="catlink" activeClassName="activee" onlyActiveOnIndex to="/family">FAMILY</Link>
                </div>
                <div class="catitems">
                    <Link class="catlink"  to="/rights">RIGHTS</Link>
                </div>
                <div class="catitems"><Link class="catlink" to="/crime">CRIME</Link></div>
                <div class="catitems"><Link class="catlink" to="/employment">EMPLOYMENT</Link></div>
            </div>
            <div class="content">
                <Route path='/family' component={ Family }/>
                <Route path='/rights' component={ Rights }/>
                <Route path='/crime' component={ Crime }/>
                <Route path='/employment' component={ Employment }/>
            </div>
        </div>
        </Router>
    );
  }
