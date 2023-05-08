import { useState } from "react";
import Output from "./Output";

function FileForm(){
    const [file, setFile] = useState(null);
    const [encMethod, setEncMethod] = useState('Transposition');
    const [encKey, setEncKey] = useState('');
    const [vernamKey, setVernamKey] = useState('');
    const [rawEncDecs, setRawEncDecs] = useState('');
    const [customDecKey, setCustomDecKey] = useState('');

    function handleFile(event){
        setFile(event.target.files[0]);
    }

    function handleSubmit(event){
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('encryptionMethod', encMethod);
        formData.append('encryptionkey', encKey);
        console.log(formData);
    }

    return(
        <div>
            <div className="file-form">
                <form onSubmit={handleSubmit}>
                    <label for="EncMethod">Encryption Method</label>
                    <select id="EncMethod" value={encMethod} onChange={(e) => {setEncMethod(e.target.value)}}>
                        <option value ="Transposition">Transposition</option>
                        <option value="Vernam">Vernam</option>
                        <option value="Vigenere">Vigenere</option>
                        <option value="Custom">Custom</option>
                    </select>
                    <br/><br/>
                    <label for="key">Encryption key:</label>
                    <input type="text" id="key" value={encKey} onChange={(e) => {setEncKey(e.target.value)}}/>
                    <br/><br/>
                    <label for="fileupload">Upload File</label>
                    <input type="file" id="fileupload" onChange={handleFile}/>
                    <br/><br/>
                    <button style={{position : 'relative', left:'225px'}}>Encrypt</button>
                    <button style={{position : 'relative', left:'275px'}}>Decrypt</button>
                </form>
            </div>
            <Output />
        </div>
    );
}

export default FileForm;