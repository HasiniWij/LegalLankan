import React, {useState, useEffect} from 'react';
import { Home } from '../Components/Home/home';

export const HomePage = ()=> {

    
    useEffect(()=> {
        fetch('/api', ).then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => console.log(data))
    },[])

    return(
        <>
            <Home/>
        </>
    )
}