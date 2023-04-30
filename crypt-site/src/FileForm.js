function FileForm(){
    return(
        <div className="file-form">
            <form>
                <label for="EncMethod">Encryption Method</label>
                <select id="EncMethod">
                    <option value ="Transposition">Transposition</option>
                    <option value="Vernam">Vernam</option>
                    <option value="Vigenere">Vigenere</option>
                    <option value="Custom">Custom</option>
                </select>
                <br/><br/>
                <label for="key">Encryption key:</label>
                <input type="text" id="key"/>
                <br/><br/>
                <label for="fileupload">Upload File</label>
                <input type="file" id="fileupload"/>
                <br/><br/>
                <button style={{position : 'relative', left:'225px'}}>Encrypt</button>
                <button style={{position : 'relative', left:'275px'}}>Decrypt</button>
            </form>
        </div>
    );
}

export default FileForm;