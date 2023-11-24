// SessionContext.js

import React, { createContext, useContext, useState } from 'react';

const SessionContext = createContext();

export const useSession = () => {
  const context = useContext(SessionContext);
  if (!context) {
    throw new Error('useSession must be used within a SessionProvider');
  }
  return context;
};

export const SessionProvider = ({ children }) => {
  const [userSession, setUserSession] = useState(null);

  const login = (username) => {
    setUserSession({ username });
  };

  const logout = () => {
    setUserSession(null);
  };

  return (
    <SessionContext.Provider value={{ userSession, login, logout }}>
      {children}
    </SessionContext.Provider>
  );
};
