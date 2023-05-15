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
    const [action, setAction] = useState('');
    let url = '';

    function handleSubmit(e){
        e.preventDefault();

        const formData = new FormData();
        formData.append('text', text);
        formData.append('encryptionMethod', encMethod);
        formData.append('encryptionkey', encKey);
        formData.append('vernamKey', vernamKey);
        formData.append('rawEncDecs', rawEncDecs);
        formData.append('customDecKey', customDecKey);

        if (action === 'Encrypt'){
            url = 'http://127.0.0.1:5000/TextEncrypt'
        }
        else if (action === 'Decrypt'){
            url = 'http://127.0.0.1:5000/TextDecrypt'
        }

        fetch(url, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
            response.json().then(data => {
                console.log(data)
                setVernamKey(data.Vernam)
                setRawEncDecs(data.rawEncDecs)
                setCustomDecKey(data.CustomKey)
                setResultText(data.resulttext)
            });
            } else {
            throw new Error('Network response was not ok');
            }
        }).catch(error => console.log(error));
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
                    <button style={{position : 'relative', left:'225px'}} onClick={() => setAction('Encrypt')}>Encrypt</button>
                    <button style={{position : 'relative', left:'275px'}} onClick={() => setAction('Decrypt')}>Decrypt</button>
    
                </form>
            </div>
            <Output encMethod = {encMethod} encKey = {encKey} text = {resultText}/>
            </div>
        );
    }

export default TextForm;