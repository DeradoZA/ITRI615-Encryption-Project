import { useLocation } from "react-router-dom";

function Output(){
    const location = useLocation();
    const currentPath = location.pathname;

    console.log(currentPath);
    if (currentPath === "/text"){
        return(
            <div className="output">
                <label for="Output">Result</label>
                <textarea id="Output" rows='4' columns='100'></textarea>
            </div>
        );
    }
    else{
        return(
            <div className="output">
                <h1>Output</h1>
                <a href="/filedownload">Download File</a>
            </div>
        );
    }
    
}

export default Output;