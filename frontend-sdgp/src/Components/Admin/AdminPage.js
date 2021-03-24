import React, {useState, useEffect} from 'react';
import { Admin } from '../Components/Admin/admin';

export const AdminPage = ()=> {

    useEffect(()=> {
        fetch('/api', ).then(response => {
            if(response.ok){
                return response.json()
            }
        }).then(data => console.log(data))
    },[])

    return(
        <>
            <Admin/>
        </>
    )
}