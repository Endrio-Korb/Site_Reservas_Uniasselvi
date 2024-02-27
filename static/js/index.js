const chk_teme = document.getElementById('chk-dark')

chk_teme.addEventListener('change', () => {
    document.body.classList.toggle('dark')
})