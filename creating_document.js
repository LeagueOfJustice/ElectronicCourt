function creatingDocument() {
    if ( $('#author-name').val() === "" || $('#deal-name').val() === ""
    || $('#pozyvach').val() === "" || $('#vidpovidach').val() === "" || $('#predmet').val() === "" || $('#text-document').val() === "" ) {
        alert('Заповніть всі поля');
        return false;
    } else {
        document.getElementById('creating_document').reset();
        alert('Документ успішно створений.');

        var name = document.getElementById('text-document').value;
        var img = document.getElementById('author-name').value;
        var img = document.getElementById('deal-name').value;
        var img = document.getElementById('pozyvach').value;
        var img = document.getElementById('vidpovidach').value;
        var img = document.getElementById('predmet').value;

        parentElem.appendChild(out);
        document.getElementById('form').reset();
    }
}
