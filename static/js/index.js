const chk_teme = document.getElementById('chk-dark')
const tittle = document.querySelectorAll('.tittle')

chk_teme.addEventListener('change', () => {
    document.body.classList.toggle('dark')
    Array.from(tittle).forEach(function (tittle){
        tittle.classList.toggle('dark')
    })

})