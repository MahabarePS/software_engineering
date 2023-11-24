// sessioncontext.js

import React, { createContext, useContext, useState } from 'react';

const SessionContext = createContext();

const SessionProvider = ({ children }) => {
    const [session, setSession] = useState({ user_id: null, isLoggedIn: false });

    return (
        <SessionContext.Provider value={{ session, setSession }}>
            {children}
        </SessionContext.Provider>
    );
};

const useSession = () => {
    const context = useContext(SessionContext);
    if (!context) {
        throw new Error('useSession must be used within a SessionProvider');
    }
    return context;
};

export { SessionProvider, useSession };
