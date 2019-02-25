function spoiler(n) {
    element = document.getElementById(n);
    if (element.style.display == 'none')
        element.style.display = 'block'
    else element.style.display = 'none';
}

function showHide(n) {
    var encr = document.getElementById(n);
    if (encr.type == 'password')
        encr.type = 'text'
    else encr.type = 'password';
}
var copy_login = document.querySelector('.copy-login')
copy_login.addEventListener('click', function (event) {
    var login_to = document.querySelector('.login-to-copy');
        login_to.focus();
        login_to.select();
        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            console.log('Copying text command was ' + msg);
        }
        catch (err) {
            console.log('Oops, unable to copy');
        }
});
var copy_password = document.querySelector('.copy-password')
copy_password.addEventListener('click', function (event) {
    var password_to = document.querySelector('.password-to-copy');
        password_to.focus();
        password_to.select();
        try {
            var successful = document.execCommand('copy');
            var msg = successful ? 'successful' : 'unsuccessful';
            console.log('Copying text command was ' + msg);
        }
        catch (err) {
            console.log('Oops, unable to copy');
        }
});