import React, {useState, useEffect} from 'react';
import { Home } from '../Components/Home/home';

export const HomePage = ()=> {

    const [todo, setTodo] = useState([])
    
    useEffect(()=> {
        fetch('/api').then(response => {
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