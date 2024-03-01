// const chk_teme = document.getElementById('chk-dark')
// const tittle = document.querySelectorAll('.tittle')
// const input = document.querySelectorAll('.input')
// const btn = document.querySelectorAll('.btn')
// const nav = document.querySelectorAll('.navbar')
// const text = document.querySelectorAll('.text')
// const text_table = document.querySelectorAll('.text-table')

// chk_teme.addEventListener('change', () => {
//     // Altera o tema de fundo da página
//     document.body.classList.toggle('light')

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

//     // Altera tema do texto
//     Array.from(text).forEach(function(text) {
//         text.classList.toggle('light')
//     })

//     //Altera cor do texto da tabela
//     Array.from(text_table).forEach(function(text_table) {
//         text_table.classList.toggle('light')
//     })
// })

const chk_lab = document.getElementById('checkbox-field')
const reservados = document.querySelector('#reservados')
const disponiveis = document.querySelector('#disponiveis')

chk_lab.addEventListener('change', () => {
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