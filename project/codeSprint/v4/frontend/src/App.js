// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
import React from 'react';
import SignUpForm from './components/signup/SignUpForm'; // Update the path based on your project structure
import SignInForm from './components/signin/SignInForm';
import Dashboard from './components/dashboard/dashboard';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';

function App() {
  return (
    // <div className="App">
    //   <h1>Welcome to EduLoyalty</h1>
    //   <SignUpForm /> Render the SignUpForm component here
    // </div>
    <Router>
            <Routes>
                <Route exact path="/" element={<SignInForm />} />
                <Route path="/signup" element={<SignUpForm />} />
                <Route path="/dashboard" element={<Dashboard />} />
                {/* Other routes or components */}
            </Routes>
    </Router>
  );
}

export default App;