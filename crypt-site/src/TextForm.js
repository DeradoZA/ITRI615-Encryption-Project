import { useState } from "react";
import Output from "./Output"

function TextForm(){
    const [encMethod, setEncMethod] = useState('Transposition');
    const [encKey, setEncKey] = useState('');
    const [text, setText] = useState('');

    function handleSubmit(e){
        e.preventDefault();

        fetch("http://127.0.0.1:5000/TextEncrypt/" + text)
        .then(res => {
            return res.json();
        }).then(data => setText(data.Output));
    }

    return(
        <div>
        <div className="text-form">
            <form onSubmit={handleSubmit}>
                <label for="EncMethod">Encryption Method</label>
                <select id="EncMethod" value={encMethod} onChange={(e) => setEncMethod(e.target.value)}>
                    <option value ="Transposition">Transposition</option>
                    <option value="Vernam">Vernam</option>
                    <option value="Vigenere">Vigenere</option>
                    <option value="Custom">Custom</option>
                </select>
                <br/><br/>
                <label for="EncKey">Encryption Key</label>
                <input type="text" id = "EncKey" value = {encKey} onChange={(e) => setEncKey(e.target.value)}></input>
                <br/><br/>
                <label for="text-input">Plain text</label>
                <textarea
                 id="text-input" rows='4' columns='100' value = {text} onChange={(e) => setText(e.target.value)}>
                    Enter your plaintext here</textarea>
                <br/>
                <button style={{position : 'relative', left:'225px'}}>Encrypt</button>
                <button style={{position : 'relative', left:'275px'}}>Decrypt</button>

            </form>
        </div>
        <Output encMethod = {encMethod} encKey = {encKey} text = {text}/>
        </div>
    );
}

export default TextForm;