

function destaque() {
    const chk_lab = document.getElementById('checkbox-field')
    const reservados = document.querySelector('#reservados')
    const disponiveis = document.querySelector('#disponiveis')

    chk_lab.addEventListener('change', () => {
        if (chk_lab.checked == true){
            reservados.classList.remove('principal')
            disponiveis.classList.toggle('principal')
        } else {
            reservados.classList.toggle('principal')
            disponiveis.classList.remove('principal')
        }
    })
}


const chkSidebar = document.getElementById("chk-burguer")
const sidebar = document.querySelector('.sidebar')
const sideItem = document.querySelector('.side-item')
chkSidebar.addEventListener('change', () => {
    if (chkSidebar.checked == true) {
        sidebar.classList.toggle('active')
        sideItem.classList.toggle('active')
    } else {
        sidebar.classList.remove('active')
    }
})
