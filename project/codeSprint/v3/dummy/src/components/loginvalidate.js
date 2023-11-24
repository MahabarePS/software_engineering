// import React, { useState } from 'react';
// import { useSession } from './SessionContext';
// const LoginValidate = () => {
//     const [name, setName] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState('');
//     const [successMessage, setSuccessMessage] = useState('');
//     const { session, setSession } = useSession();

//     // const { login } = useSession();

//     const handleSubmit = async (e) => {
//         e.preventDefault();

//             const response = await fetch('http://127.0.0.1:5000/validate1', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ name: name, password: password }),
//             });

//             if (response.ok) {
//                 const data = await response.json();
//                 if (data.success) {
//                     // Successful login
//                     setSuccessMessage(data.message);
//                     setError(''); // Clear any previous error messages
//                 } else {
//                     setError(data.error); // Display any error message from the server
//                     setSuccessMessage(''); // Clear any previous success messages
//                 }
//             } else {
//                 setError('An error occurred. Please try again later.');
//                 setSuccessMessage(''); // Clear any previous success messages
//             }
            
//         } 
    

//     return (
//         <div>
//             <form onSubmit={handleSubmit}>
//                 {error && <p style={{ color: 'red' }}>{error}</p>}
//                 {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
//                 <label>Name:</label>
//                 <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
//                 <br />
//                 <label>Password:</label>
//                 <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
//                 <br />
//                 <button type="submit">Submit</button>
//             </form>
//         </div>
//     );
// };

// export default LoginValidate;

// Modify your LoginValidate component to handle session:
import React, { useState } from 'react';
import { useSession } from './SessionContext';

const LoginValidate = () => {
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');
    const { session, setSession } = useSession();

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch('http://127.0.0.1:5000/validate1', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: name, password: password }),
        });

        if (response.ok) {
            const data = await response.json();
            if (data.message) {
                // Successful login
                setSuccessMessage(data.message);

                // Update the session on successful login
                setSession({ user_id: session.user_id, isLoggedIn: true });
                setError('');
            } else {
                setError(data.error_message);
                setSuccessMessage('');
            }
        } else {
            setError('Invalid username or password.Please try again later.');
            setSuccessMessage('');
        }
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                {error && <p style={{ color: 'red' }}>{error}</p>}
                {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
                <label>Name:</label>
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                <br />
                <label>Password:</label>
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
                <br />
                <button type="submit">Submit</button>
            </form>
        </div>
    );
};

export default LoginValidate;
