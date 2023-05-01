import Navbar from "./Navbar";
import FileForm from "./FileForm";
import Output from "./Output";
import Header from "./Header";
import TextForm from "./TextForm";
import { BrowserRouter as Router, Route, Switch, Link } from "react-router-dom";

function App() {

  return (
    <Router>
      <div className="app">
        <Header />
        <Navbar />
        <Switch>
          <Route exact path='/'>
            <TextForm />
          </Route>
          <Route path="/text">
            <TextForm />
          </Route>
          <Route path="/files">
            <FileForm />
          </Route>
        </Switch>
        <Output />
      </div>
    </Router>
  );
}

export default App;
