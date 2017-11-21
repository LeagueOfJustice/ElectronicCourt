function login() {
    if ($('#fieldUser').val() === "" || $('#fieldPassword').val() === "") {
        alert('Заповніть всі поля');
        return false;
    } else {
        var date = new Date;
        var author = document.getElementById('fieldUser').value;
        var text = document.getElementById('fieldPassword').value;
        out.id = 'login';

        parentElem.appendChild(out);
        document.getElementById('form').reset();
    }
}
