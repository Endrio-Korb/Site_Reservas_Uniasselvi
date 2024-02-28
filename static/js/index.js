const chk_teme = document.getElementById('chk-dark')
// const tittle = document.querySelectorAll('.tittle')
// const input = document.querySelectorAll('.input')
// const btn = document.querySelectorAll('.btn')
// const nav = document.querySelectorAll('.navbar')

// chk_teme.addEventListener('change', () => {
//     // Altera o tema de fundo da página
//     document.body.classList.toggle('light')

//     // Altera o tema dos titulos
//     Array.from(tittle).forEach(function (tittle){
//         tittle.classList.toggle('light')
//     })

//     // Altera o tema do inputs
//     Array.from(input).forEach(function(input){
//         input.classList.toggle('light')
//     })

//     // Altera o tema dos botãos
//     Array.from(btn).forEach(function(btn){
//         btn.classList.toggle('light')
//     })

//     // Altera tema da navbar
//     Array.from(nav).forEach(function(nav){
//         nav.classList.toggle('light')
//     })
// })

const chk_lab = document.getElementById('checkbox-field')
const reservados = document.querySelector('#reservados')
const disponiveis = document.querySelector('#disponiveis')

chk_lab.addEventListener('change', () => {
    console.log('funcionou')
    if (reservados.classList.contains('principal')){
        reservados.classList.remove('principal')
    } else {
        reservados.classList.toggle('principal')
    }

    if (disponiveis.classList.contains('principal')){
        disponiveis.classList.remove('principal')
    } else {
        disponiveis.classList.toggle('principal')
    }
})