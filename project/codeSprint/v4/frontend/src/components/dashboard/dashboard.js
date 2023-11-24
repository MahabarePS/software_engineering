import React from 'react';

const Sidebar = () => {
    return (
        <div className="sidebar bg-dark">
            <ul className="nav flex-column">
                <li className="nav-item"><a className="nav-link text-white" href="#">Profile</a></li>
                <li className="nav-item"><a className="nav-link text-white" href="#">Feedback</a></li>
                <li className="nav-item"><a className="nav-link text-white" href="#">HOF</a></li>
                <li className="nav-item"><a className="nav-link text-white" href="#">Refer</a></li>
                <li className="nav-item"><a className="nav-link text-white" href="/">Logout</a></li>
            </ul>
        </div>
    );
};

const Header = () => {
    return (
        <div className="header bg-primary text-white text-center py-3">
            <h1>Dashboard Header</h1>
        </div>
    );
};

const Content = () => {
    return (
        <div className="content p-4">
            <h2>Welcome to your Dashboard!</h2>
            <p>This is the main content area.</p>
        </div>
    );
};

const Footer = () => {
    return (
        <div className="footer bg-dark text-white text-center py-3">
            <p>Dashboard Footer</p>
        </div>
    );
};

const Dashboard = () => {
    return (
        <div className="dashboard d-flex">
            <Sidebar />
            <div className="main flex-grow-1">
                <Header />
                <Content />
                <Footer />
            </div>
        </div>
    );
};

export default Dashboard;
