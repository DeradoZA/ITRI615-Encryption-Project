import Navbar from "./Navbar";
import FileForm from "./FileForm";
import Header from "./Header";
import TextForm from "./TextForm";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {

  return (
      <div className="app">
        <Header />
        <Navbar />
        <Router>
          <Routes>
            <Route exact path='/' element={<TextForm />}/>
            <Route path="/text" element={<TextForm />}/>
            <Route path="/files" element={<FileForm />} />
          </Routes>
        </Router>
      </div>
  );
}

export default App;
