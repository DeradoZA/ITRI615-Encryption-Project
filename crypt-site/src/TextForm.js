// This file uses UTF-8 encoding
// -*- coding: utf-8 -*-

import { useState } from "react";
import { useEffect } from "react";
import Output from "./Output"

function TextForm(){
    const [encMethod, setEncMethod] = useState('Transposition');
    const [encKey, setEncKey] = useState('');
    const [text, setText] = useState('');
    const [resultText, setResultText] = useState('');
    const [vernamKey, setVernamKey] = useState('');
    const [rawEncDecs, setRawEncDecs] = useState('');
    const [customDecKey, setCustomDecKey] = useState('');

    function handleSubmit(e){
        e.preventDefault();
    }

    function handleEncryptClick(){
        fetch(`http://127.0.0.1:5000/TextEncrypt/${encodeURIComponent(text)}/${encodeURIComponent(encKey)}/${encodeURIComponent(encMethod)}`)
        .then(res => {
            return res.json();
        }).then(data => {
            console.log(data)
            setResultText(data.ciphertext);
            setVernamKey(data.Vernam);
            setRawEncDecs(data.rawEncryptedDecs);
            setCustomDecKey(data.CustomDecKey)});
    }

    function handleDecryptClick(){
        if (encMethod === "Vernam"){
            fetch(`http://127.0.0.1:5000/TextDecrypt/${encodeURIComponent(resultText)}/${encodeURIComponent(vernamKey)}/${encodeURIComponent(encMethod)}`)
            .then(res => {
                return res.json();
            }).then(data => {
                console.log(data);
                setResultText(data.plaintext);
            });
        } else if (encMethod === "Transposition"){
            fetch(`http://127.0.0.1:5000/TextDecrypt/${encodeURIComponent(resultText)}/${encodeURIComponent(encKey)}/${encodeURIComponent(encMethod)}`)
            .then(res => {
                return res.json();
            }).then(data => {
                console.log(data);
                setResultText(data.plaintext);
            });
        } else if (encMethod === "Custom"){
            fetch(`http://127.0.0.1:5000/TextCustomDecrypt/${encodeURIComponent(resultText)}/${encodeURIComponent(customDecKey)}/${encodeURIComponent(rawEncDecs)}`)
            .then(res => {
                return res.json();
            }).then(data => {
                console.log(data);
                setResultText(data.plaintext);
            });
        }
    }

    useEffect(() => {
        if (encMethod === "Vernam" || encMethod === "Custom"){
            setEncKey("None");
        }
    }, [encMethod])

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
                <label for="text-input">Text</label>
                <textarea
                 id="text-input" rows='4' columns='100' value = {text} onChange={(e) => setText(e.target.value)}>
                </textarea>
                <br/>
                <button style={{position : 'relative', left:'225px'}} onClick={handleEncryptClick}>Encrypt</button>
                <button style={{position : 'relative', left:'275px'}} onClick={handleDecryptClick}>Decrypt</button>

            </form>
        </div>
        <Output encMethod = {encMethod} encKey = {encKey} text = {resultText}/>
        </div>
    );
}

export default TextForm;