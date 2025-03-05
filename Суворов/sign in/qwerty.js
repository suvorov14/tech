document.getElementById('login-btn').addEventListener('click', function(){
    alert()
    const logininput = document.getElementById('login').value
    const passwordinput = document.getElementById('password').value
    let login = "user"
    let password = "password"
    if(logininput === login && passwordinput === password) {
        window.open('l.html')
    } else {

    }
})