import { useState } from "react";
import Output from "./Output";
import { useEffect } from "react";

function FileForm(){
    const [file, setFile] = useState(null);
    const [encMethod, setEncMethod] = useState('Transposition');
    const [encKey, setEncKey] = useState('');
    const [vernamKey, setVernamKey] = useState('');
    const [rawEncDecs, setRawEncDecs] = useState('');
    const [customDecKey, setCustomDecKey] = useState('');
    const [action, setAction] = useState('');
    let url = '';

    function handleFile(event){
        setFile(event.target.files[0]);
    }

    function handleSubmit(event){
        event.preventDefault();
        const formData = new FormData();
        formData.append('file', file);
        formData.append('encryptionMethod', encMethod);
        formData.append('encryptionkey', encKey);
        formData.append('vernamKey', vernamKey);
        formData.append('rawEncDecs', rawEncDecs);
        formData.append('customDecKey', customDecKey);
        console.log(formData);

        if (action === 'Encrypt'){
            url = 'http://127.0.0.1:5000/EncryptFileUpload'
        }
        else if (action === 'Decrypt'){
            url = 'http://127.0.0.1:5000/DecryptFileUpload'
        }

        fetch(url, {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
            response.json().then(data => {
                console.log(data)
                setVernamKey(data.vernam)
                setRawEncDecs(data.rawEncDecs)
                setCustomDecKey(data.CustomKey)
                // Extract the file data
                const fileData = data.file.data;
                const fileName = data.file.name;
                const mimeType = data.file.mime_type;

                const fileContent = atob(fileData);
                const uint8Array = new Uint8Array(fileContent.length);
                
                for (let i = 0; i < fileContent.length; i++) {
                  uint8Array[i] = fileContent.charCodeAt(i);
                }
                
                const file = new File([uint8Array], fileName, { type: mimeType });
                
                const url = URL.createObjectURL(file);
                
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', fileName);
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
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
            <div className="file-form">
                <form onSubmit={handleSubmit}>
                    <label htmlFor="EncMethod">Method</label>
                    <select id="EncMethod" name="encryptionMethod" value={encMethod} onChange={(e) => {setEncMethod(e.target.value)}}>
                        <option value ="Transposition">Transposition</option>
                        <option value="Vernam">Vernam</option>
                        <option value="Vigenere">Vigenere</option>
                        <option value="Custom">Custom</option>
                    </select>
                    <br/><br/>
                    <label for="key">Key</label>
                    <input type="text" id="key" value={encKey} onChange={(e) => {setEncKey(e.target.value)}}/>
                    <br/><br/>
                    <label for="fileupload">Upload File</label>
                    <input type="file" id="fileupload" name="file" onChange={handleFile}/>
                    <br/><br/>
                    <button style={{position : 'relative', left:'225px'}} onClick={() => setAction('Encrypt')}>Encrypt</button>
                    <button style={{position : 'relative', left:'275px'}} onClick={() => setAction('Decrypt')}>Decrypt</button>
                </form>
            </div>
        </div>
    );
}

export default FileForm;