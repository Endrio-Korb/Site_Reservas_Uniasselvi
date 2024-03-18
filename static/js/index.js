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
    if (chk_lab.checked == true){
        reservados.classList.remove('principal')
        disponiveis.classList.toggle('principal')
    } else {
        reservados.classList.toggle('principal')
        disponiveis.classList.remove('principal')
    }
})

class MobileNavbar {
    constructor(mobileMenu, navList, navLinks) {
        this.mobileMenu = document.querySelector(mobileMenu);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelectorAll(navLinks);
        this.activeClass = "active";

        this.handleClick = this.handleClick.bind(this);
    }

    animateLinks() {
        this.navLinks.forEach((link, index) => {
            link.style.animation
            ? (link.style.animation = "")
            : (link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`);
        });
    }

    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.mobileMenu.classList.toggle(this.activeClass);
        this.animateLinks();
    }

    addClickEvent() {
        this.mobileMenu.addEventListener("click", this.handleClick);
    }

    init() {
      if (this.mobileMenu) {
        this.addClickEvent();
      }
      return this;
    }
}

const mobileNavbar = new MobileNavbar(
    ".mobile-menu",
    ".nav-list",
    ".nav-list li",
);

mobileNavbar.init();