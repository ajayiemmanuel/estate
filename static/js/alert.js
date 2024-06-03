const alertBox = document.querySelector('.alert');
const open_alert = document.getElementById('open_alert');
const close_alert = document.getElementById('close_alert');
let timer;
open_alert.addEventListener('click',()=>{
    showAlert();
})
//close alert
close_alert.addEventListener('click',()=>{
    hideAlertBox();
    clearTimeout(timer);
})
//Show alertBox function
function showAlert(){
    alertBox.classList.remove('hide');
    alertBox.classList.add('show');
    //Hide animation onload
    if(alertBox.classList.contains('hidden')){
       alertBox.classList.remove('hidden')
    }
    //After 6 seconds hide alert box
    timer = setTimeout(function (){
        hideAlertBox();
     },6000)
}
//hide alertBox function
function hideAlertBox(){
     alertBox.classList.remove('show');
     alertBox.classList.add('hide');
}