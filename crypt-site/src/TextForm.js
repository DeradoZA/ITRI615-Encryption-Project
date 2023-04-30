function TextForm(){
    return(
        <div className="text-form">
            <form>
                <label for="EncMethod">Encryption Method</label>
                <select id="EncMethod">
                    <option value ="Transposition">Transposition</option>
                    <option value="Vernam">Vernam</option>
                    <option value="Vigenere">Vigenere</option>
                    <option value="Custom">Custom</option>
                </select>
                <br/><br/>
                <label for="EncKey">Encryption Key</label>
                <input type="text" id = "EncKey"></input>
                <br/><br/>
                <label for="text-input">Plain text</label>
                <textarea id="text-input" rows='4' columns='100'>Enter your plaintext here</textarea>
                <br/>
                <button style={{position : 'relative', left:'225px'}}>Encrypt</button>
                <button style={{position : 'relative', left:'275px'}}>Decrypt</button>

            </form>
        </div>
    );
}

export default TextForm;