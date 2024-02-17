const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById("modal-body-confirm");
const startBtn = document.getElementById("start-button");
const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk');
    const name =modalBtn.getAttribute('data-quiz');
    const time =modalBtn.getAttribute('data-time') + "  dəqiqə";
    const topic =modalBtn.getAttribute('data-topic');
    const question =modalBtn.getAttribute('data-quiestions');
    
    modalBody.innerHTML =   `
            <div class="h5 mb-3"> Həqiqətən <b>${name}</b> testinə başlamağa hazırsan? </div>
            <div class="h5 mb-3">  <b>QEYD:</b> Əgər bu testi işləmisinizsə, nəticəniz dəyişmir! Göstərdiyiniz nəticə "Nəticələrim" bölməsində yerləşdirilib </div>
            <div class= "text-muted"
                <ul>
                    <li>Sual sayı: <b>${question}</b></li>
                    <li>Vaxt: <b>${time} </b></li>
                    <li>Kateqoriya: <b>${topic}</b> </li>
                </ul>
            </div>
    `
    startBtn.addEventListener('click' , ()=>{
        window.location.href = url+pk
    })
}))


