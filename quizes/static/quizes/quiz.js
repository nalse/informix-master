const url = window.location.href
const scoreBox = document.getElementById("score-box")
const resultBox= document.getElementById('result-box')
const timerBox = document.getElementById('timer-box')
const backButton = document.getElementById("back");
const nextButton = document.getElementById("next");
const number = document.getElementById("number");
const sual = document.getElementById("sual")
const quizForm = document.getElementById("quiz-form")
const csrf= document.getElementsByName("csrfmiddlewaretoken")
const image=document.getElementById("image")
const resultSual=document.getElementById("result-sual")
const insideSual=document.getElementById("inside-sual")
const quizAndAnswer= document.getElementById("quizAndAnswer")
const heller= document.getElementById("heller")
const netice= document.getElementById("netice")
const say= document.getElementById("say")

resultBox.style=" padding-top:30px;"
let a= false
let i=0
let t=0
let m=0
let p=0

const activateTimer = (time) =>{    
   if(time.toString().length <2){
     timerBox.innerHTML = `<b>0${time}:00</b>`
   }
   else{
    timerBox.innerHTML = `<b> Vaxtınız gedir${time}:00</b>`
   }
   let minutes = time-1
   let seconds = 60
   let displaySeconds
   let displayMinutes
const timer = setInterval(()=>{
    seconds--    
    if(seconds < 0){
        seconds = 59
        minutes--
    }
    if(minutes.toString().length <2){
        displayMinutes = '0' + minutes
      }
    else{
        displayMinutes = minutes
    }
    if(seconds.toString().length <2){
        displaySeconds = '0' + seconds
    }
    else{
        displaySeconds = seconds
    }
    if(minutes ===0 && seconds === 0){
        timerBox.innerHTML = "<b><p class='section-title pr-5'><span class='pr-2'>Vaxtınız bitdi:</span></p> 00:00</b>"
        setTimeout(() => {
        alert("Vaxtiniz bitdi")
        clearInterval(timer)
        sendData()   
    },500)
    }
    if(a){
        timerBox.innerHTML = "<b>{{quizes.sual_sayi}} 00:00</b>"
        setTimeout(() => {
            clearInterval(timer)
            console.log("super")
        },500)
    }
    timerBox.innerHTML = `<h5 style="color:red;"><b>${displayMinutes}:${displaySeconds}</b></h5>`
    
   },1000)
}
$.ajax({    
    type:'GET',
    url: `${url}data`,
    success: function(response){
        data = response.data2
        data.forEach(el=> {
            const questionBox = document.createElement("div")
            questionBox.style="display: none";
            $(document).ready(function() {
                showDive();
            });
            for (const [question,answers] of Object.entries(el)){
                questionBox.classList.add("testler"); 
                answers.forEach(answer=>{
                    questionBox.innerHTML +=`
                        <h5 class="test" >
                             ${answer}
                        </h5><hr> `
                }) 
                if(t===0){
                    t=t+1
                    $.ajax({
                        type:'GET',
                        url: `${url}data`,
                        success: function(response){
                            data = response.data
                            data.forEach(el=> {
                                const quizBox = document.createElement("div")
                                for (const [question,answers] of Object.entries(el)){
                                    quizBox.classList.add("sual-cavab")
                                    quizBox.style="display: none";
                                    $(document).ready(function() {
                                        showDive();
                                    });
                                    answers.forEach(answer=>{
                                        quizBox.innerHTML +=`
                                            <div class="cavab" style="box-shadow: rgba(3, 102, 214, 0.3) 0px 0px 0px 3px; padding:10px 2px; margin-bottom:15px;">
                                                <input type="radio" class="ans" id ="${question}-${answer}" name="${question}" value="${answer}" >
                                                <label for="${question}">${answer}</label>
                                            </div> `  
                                    }) 
                                }                  
                                sual.append(quizBox)
                            });
                        },
                        error: function(error){
                            console.log(error)
                        }
                    })
                }  
            }                  
            sual.append(questionBox)
        });
        activateTimer(response.time)
    },
    error: function(error){
        console.log(error)
    }
})

$.ajax({
        type:'GET',
        url: `${url}data`,
        success: function(response){
            data = response.data3
              
            data.forEach(el=> {             
                const solution = document.createElement("div")
                    for (const [question,answers] of Object.entries(el)){                            
                        solution.classList.add("heller");  
                        solution.style="background-color:white"
                        solution.innerHTML +=`
                                <div class="">
                                    ${question}
                                </div><hr> `
                        answers.forEach(answer=>{
                            solution.innerHTML +=`
                                <div class="cavab" style="margin-bottom:15px">
                                <label>${answer}</label>
                                 </div> `
                        })      
                    } 
                quizAndAnswer.append(solution)               
            });
        },
        error: function(error){
            console.log(error)
        }
})

const sendData = () => {  
    const elements= [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{     
        if(el.checked){
            data[el.name]= el.value
        }
        else{
            if(!data[el.name]){
                data[el.name]= null
            }
        }
    })
    $.ajax({
        type: "POST",
        url: `${url}save/`,
        data: data,
        success: function(response){     
            quizAndAnswer.style="display:block"  
            const results = response.results
            netice.innerHTML = `Sizin nəticəniz: ${response.score.toFixed(1)}%`
            quizForm.classList.add('not-visible')
            results.forEach(res=>{
                const resDiv = document.createElement("div")         
                for (const [question, resp] of Object.entries(res)){
                    netice.style="display: block";
                    say.style="display: none";
                    resDiv.classList.add("res-ans")   
                    resDiv.append(quizAndAnswer.childNodes[0])
                    if(resp == 'not answered'){ 
                        const answer = resp['answered']
                        const correct = resp['correct_answer'] 
                        resDiv.style="border:3px solid #aee4f2; background-color:#aee4f2;color:black; margin-bottom:30px;"
                        resDiv.innerHTML += `<br><b>Bu sualın cavabını qeyd etməmisiniz! Sualın izahına baxa bilərsiniz.</b>` 
                    }
                    else{
                        const answer = resp['answered']
                        const correct = resp['correct_answer']
                        if(answer == correct){
                            resDiv.style="border:3px solid #5eed51; background-color:#5eed51;color:black; margin-bottom:30px;"
                            resDiv.innerHTML += `<br><b>Bu suala doğru cavab vermisiniz:   ${answer}</b>`
                        }
                        else{
                            resDiv.style="border:3px solid #ed5151; background-color:#ed5151;color:black; margin-bottom:30px;"
                            resDiv.innerHTML +=`<br><b>Bu suala yalnış cavab vermisiniz : ${answer}</b>`
                            resDiv.innerHTML +=`<br><b>Sualın izahına baxa bilərsiniz. Doğru cavab : ${correct}</b>`
                        }
                    }                                  
                }
                resultBox.append(resDiv)    
            })
        },
        error:function(error){
            console.log(error)
        }
    })
}
quizForm.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
    a=true
})

var visibleDiv =0
function showDive(){
    insideSual.style="display:none"
    $(".sual-cavab").hide();
    $(".sual-cavab:eq("+visibleDiv+")").show();
    $(".testler").hide();
    $(".testler:eq("+visibleDiv+")").show();
}
function showNext(){
    if((visibleDiv == $(".sual-cavab").length-1)&&(visibleDiv == $(".testler").length-1)){
        visibleDiv =0;
    }
    else{
        visibleDiv ++;
    }
    showDive();  
}
function showPrev(){
    if(visibleDiv == 0){
        visibleDiv == $(".sual-cavab").length-1;

        visibleDiv == $(".testler").length-1;
    }
    else{
        visibleDiv --;
    }    
    showDive();   
}
