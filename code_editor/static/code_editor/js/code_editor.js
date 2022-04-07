const htmlEditor = CodeMirror(document.querySelector('.editor .code .html-code'), {
    lineNumbers:true,
    tabSize: 4,
    mode: "xml",
    value: `<h1 class='welcome'>Welcome to the show</h1>`
});

const cssEditor = CodeMirror(document.querySelector('.editor .code .css-code'), {
    lineNumbers:true,
    tabSize: 4,
    mode: "css",
    value: `.welcome {
    color: red;
}`
});

const jsEditor = CodeMirror(document.querySelector('.editor .code .javascript-code'), {
    lineNumbers:true,
    tabSize: 4,
    lineWrapping: true,
    mode: "javascript",
});

console.log(htmlEditor)


document.querySelector('#run-btn').addEventListener('click', function(){
    console.log('ran')
    let htmlCode = htmlEditor.getValue()
    let cssCode = '<style>' + cssEditor.getValue() + '</style>'
    let jsCode = '<scri' + 'pt>' + jsEditor.getValue() + '</scri' + 'pt>'
    let previewWindow = document.querySelector('#preview-window').contentWindow.document
    previewWindow.open()
    previewWindow.write(htmlCode+cssCode+jsCode)
    previewWindow.close()
})