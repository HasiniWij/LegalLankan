import React from 'react'; 
import './Explore.css';
import Family from '../Categories/Family';
import Crime from '../Categories/Crime';
import Rights from '../Categories/Rights';
import Employment from '../Categories/Employment';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

function Explore() {
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
                <Route path='/family' component={Family}/>
                <Route path='/rights' component={Rights}/>
                <Route path='/crime' component={Crime}/>
                <Route path='/employment' component={Employment}/>
            </div>
        </div>
        </Router>
    );
  }
export default Explore;