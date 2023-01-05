var preloader = document.getElementById("loading");


function myFunction(){
    preloader.style.display = 'none';
   
    
};

window.addEventListener('load', function(load) {
window.removeEventListener('load', load, false);               
setTimeout(function(){loading.style.display = 'none'},3000);

},false);








