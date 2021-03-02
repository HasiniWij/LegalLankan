import React, {useState, useEffect} from 'react';
import { Explore } from '../Components/Explore/explore';

export const ExplorePage = ()=> {

    useEffect(()=> {
        fetch('/api', ).then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => console.log(data))
    },[])

    return(
        <>
            <Explore/>
        </>
    )
}