// import React, { useState } from 'react';
// import { Link } from 'react-router-dom';

// const SignInForm = () => {
//     const [name, setName] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState('');

//     const handleSubmit = async (e) => {
//         e.preventDefault();

//         try {
//             const response = await fetch('http://127.0.0.1:5000/', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ name, password })
//             });

//             if (!response.ok) {
//                 const data = await response.json();
//                 setError(data.error_message);
//             }else {
//                 // Redirect to Dashboard or Home page on successful signin
//                 // Navigate programmatically
//                 window.location.href = '/dashboard';
//             }
//         } catch (error) {
//             setError('An error occurred. Please try again later.');
//         }
//     };
    

//     return (
//         <form onSubmit={handleSubmit}>
//             {error && <p style={{ color: 'red' }}>{error}</p>}
//             <label>Name:</label>
//             <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
//             <br />
//             <label>Password:</label>
//             <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
//             <br />
//             {/* Use Link for navigation */}
//             <Link to="/dashboard">
//                 <button type="submit">Sign In</button>
//             </Link>
//         </form>
//     );
// };

// export default SignInForm;
import React, { useState } from 'react';

const SignInForm = () => {
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:5000/signInValidate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, password })
            });

            if (!response.ok) {
                const data = await response.json();
                setError(data.error_message);
            } else {
                // Redirect to Dashboard or Home page on successful signin
                // Navigate programmatically
                window.location.href = '/dashboard'; // Change this route as per your setup
            }
        } catch (error) {
            setError('An error occurred. Please try again later.');
        }
    };
    

    return (
        <form onSubmit={handleSubmit}>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <label>Name:</label>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
            <br />
            <label>Password:</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <br />
            <button type="submit">Sign In</button>
        </form>
    );
};

export default SignInForm;
