import { useState, useEffect } from 'react'


function App() {

  const [apiResult, setApiResult] = useState(''); 
  
  async function check() {
    let x = 'http://localhost:3000/';
    const response = await fetch(x);
    console.log(response, x);
    const data = await response.text();
    setApiResult(data);
  }
  useEffect(() => {
    check();
  }, []);


  return (
    <>
     <h1>HEY WELCOME</h1>
     <p> Result from api is - {apiResult}</p>
    </>
  )
}

export default App
