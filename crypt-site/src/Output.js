import { useLocation } from "react-router-dom";

function Output(props){
    const location = useLocation();
    const currentPath = location.pathname;

    console.log(currentPath);
    if (currentPath === "/text" || currentPath === "/"){
        return(
            <div className="output">
                <label for="Output">Result</label>
                <textarea id="Output" rows='4' columns='100' value = {props.text}></textarea>
            </div>
        );
    }
}

export default Output;