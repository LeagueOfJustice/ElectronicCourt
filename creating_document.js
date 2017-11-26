function creatingDocument() {
    if ( $('#author-name').val() === "" || $('#deal-name').val() === ""
    || $('#Plaintiff').val() === "" || $('#Defendant').val() === "" || $('#Subject').val() === "" || $('#text-document').val() === "" ) {
        alert('Заповніть всі поля');
        return false;
    } else {
        document.getElementById('creating_document').reset();
        alert('Документ успішно створений.');

        var name = document.getElementById('text-document').value;
        var img = document.getElementById('author-name').value;
        var img = document.getElementById('deal-name').value;
        var img = document.getElementById('Plaintiff').value;
        var img = document.getElementById('Defendant').value;
        var img = document.getElementById('Subject').value;

        parentElem.appendChild(out);
        document.getElementById('form').reset();
    }
}
