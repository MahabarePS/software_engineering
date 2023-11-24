import React, { useState } from 'react';

const SignUpForm = () => {
    const [name, setName] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://127.0.0.1:5000/validate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name, password: password })
            });

            if (!response.ok) {
                const data = await response.json();
                setError(data.error_message);
            } else {
                const data = await response.json();
                // Handle successful response here
                console.log(data);
            }
        } catch (error) {
            // Handle network errors or other general errors here
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
            <button type="submit">Submit</button>
        </form>
    );
};

export default SignUpForm;
