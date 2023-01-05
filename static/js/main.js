// === NavBar Indicator + back to top btn === //

let myButton = document.getElementById("mybtn");
let navBar =  document.getElementById("navbar")

window.onscroll =  function () {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        myButton.style.display = "block";
        navBar.style.backgroundColor = "#000";
    }
    else {
        myButton.style.display = "none";
        navBar.style.backgroundColor = "transparent";

    }
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        let scrolled = (winScroll / height ) * 100;
        document.getElementById('mybar').style.width = scrolled + "%";
}

myButton.addEventListener('click',() =>{
    document.body.scrollTop  = 0;
    document.documentElement.scrollTop = 0;
})

// === NavBar Indicator + back to top btn === //

// ==== light theme and Dark theme  === //
const light =  document.getElementById("light");
        light.onclick = function() {
            document.body.classList.toggle("dark-theme")
            document.getElementById("light").style.display = "none";
            document.getElementById("dark").style.display = "block";
            document.getElementById("dark-logos").style.display = "none";
            document.getElementById("light-logos").style.display = "flex";



           
        }
        const dark = document.getElementById("dark");
        dark.onclick = function () {
            document.body.classList.remove("dark-theme");
            document.getElementById("light").style.display = "block";
            document.getElementById("dark").style.display = "none";
            document.getElementById("dark-logos").style.display = "flex";
            document.getElementById("light-logos").style.display = "none";
            


          

        }

// ==== light theme and Dark theme  === //

// ==== For Slide right navigation Bar Responsive === ///

    

    function rightNav(bar) {
        bar.classList.toggle("change");
        var x = document.getElementById("rightnavitems");
        if (x.style.left === "-100%") {
             x.style.left = "0%";
        }
        else {
            x.style.left = "-100%";

        }

        
    }
    const servicesItem = () => {
        const resNav = document.getElementById("servicessubitems");
       
        if (resNav.style.display === "block") {
            resNav.style.display = "none";
            

        }
        else {
            resNav.style.display = "block";
            
        }
        
    } 
   const dropclose = () => {
    const dropClose = document.getElementById("servicessubitems");
    if (dropClose.style.display === "none") {
        dropClose.style.display = "block";
        

    }
    else {
        dropClose.style.display = "none";
        
    }
   }

// ==== For Slide right navigation Bar Responsive  === ///


// ==== For Slide Left navigation Bar === ///

const sliderNav = () => {
    document.getElementById("left-slide-menu").style.left = "0";
}
const closeLeftNav = () => {
    document.getElementById("left-slide-menu").style.left = "-200%";
}

// ====  Slide Left navigation Bar End  === ///





// 

// === text animation ===  // 
var words = ['SEO', 'Web Designing', 'Web Development', ' Social Marketing', 'Web Design','ADs ManageMent'],
    part,
    i = 0,
    offset = 0,
    len = words.length,
    forwards = true,
    skip_count = 0,
    skip_delay = 15,
    speed = 70;
var wordflick = function () {
  setInterval(function () {
    if (forwards) {
      if (offset >= words[i].length) {
        ++skip_count;
        if (skip_count == skip_delay) {
          forwards = false;
          skip_count = 0;
        }
      }
    }
    else {
      if (offset == 0) {
        forwards = true;
        i++;
        offset = 0;
        if (i >= len) {
          i = 0;
        }
      }
    }
    part = words[i].substr(0, offset);
    if (skip_count == 0) {
      if (forwards) {
        offset++;
      }
      else {
        offset--;
      }
    }
    $('.word').text(part);
  },speed);
};

$(document).ready(function () {
  wordflick();
});

// === text animation ===  // 
