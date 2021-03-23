import React from 'react';
import './admin.css';
import User from '../../images/user.png';
import Username from '../../images/username.png';
import Password from '../../images/password.png';
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

export const Admin = ()=> {
    return (
        <Router>
            <div>
                <form class ="adminForm" method="post" autocomplete ="off">

                    <div id = "centerLogo"><img src={User} alt="User"/></div>

                    <div class="input-container">
                        <img src={Username} alt="Username"/>
                        <input id="userName" class="formInput" name="userName" type="text" placeholder="Username" required />
                    </div>

                    <div class="input-container">
                        <img src={Password} alt="Password"/>
                        <input id="password" class="formInput" name="password" type="password" placeholder="Password" required />
                    </div>

                    <button class="formButton" type="submit">SUBMIT</button>
                    <button class="formButton" type="reset">RESET</button>

                </form>
            </div>
        </Router>
    );
}