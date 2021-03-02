import React, {useState, useEffect} from 'react';
import { Search } from '../Components/Search/search';

export const SearchPage = ()=> {

    
    useEffect(()=> {
        fetch('/api', ).then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => console.log(data))
    },[])

    return(
        <>
            <Search/>
        </>
    )
}