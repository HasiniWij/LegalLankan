import React from 'react'; 
import { useHistory } from 'react-router-dom';
import { Home } from '../Home/home'

export const Answer = ( ) => {

    const history = useHistory()

    const getAnswer = () => {
        fetch(`/search`, {
            method:'POST',
            body: JSON.stringify({
                "name": "Hello World"
            })
        }).then(response => response.json())
          .then(data => {
              console.log(data)
              history.push('/')
          })
    }

    return(
        <>
            <Home/>
        </>
    )

}