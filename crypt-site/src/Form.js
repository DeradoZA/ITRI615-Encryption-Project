function Form(){
    return(
        <div className="file-form">
            <form>
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

export default Form;