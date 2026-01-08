import { useState, useEffect } from 'react'


function App() {
  


  return (
    <>
      <div className="login-box">
        <h2>LeetSquad</h2>
        <form action={"http://localhost:3000/api/signup"} method="POST">
          <div className="user-box">
            <input type="text" name="email" required="" />
            <label>Email</label>

             <input type="password" name="password" required="" />
            <label>Password</label>


              <input type="text" name="leetcodeusername" required="" />
              <label>LeetCode Username</label>
          </div>
         
         <button type="submit">Sign Up</button>
        </form>
      </div>

    </>
  )
}

export default App
