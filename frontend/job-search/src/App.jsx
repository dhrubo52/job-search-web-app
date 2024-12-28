import { BrowserRouter, Routes, Route } from 'react-router';

import LoginRegister from './views/LoginRegister'
import './App.css'

function App() {
    return (
        <>
            <Routes>
                <Route path='/' element={<LoginRegister />} />
            </Routes>
        </>
    )
}

export default App
