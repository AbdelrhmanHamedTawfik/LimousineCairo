window.onload = function(){
    scrollToTop();
    hideLoading();
};

window.onscroll = function(){
    scrollNav();
    resetSectionSelection();
    showTopButton();
    scrollFade();
};

function scrollToSection(section){
    let e = document.getElementById(section);
    let nav_collpase = document.getElementById("navbarText");
    nav_collpase.classList.remove("show");
    if(e.classList.contains('scrollFade-animate')){
        $(window).scrollTop($(e).position().top - (document.querySelector('nav').offsetHeight + 10));
    }else{
        $(window).scrollTop($(e).position().top - (document.querySelector('nav').offsetHeight - 60));
    }

}

function scrollNav(){
    let navbar = document.getElementById("navbar");
    let offset = navbar.offsetTop;
    let body = document.getElementById("main-body");
    if (window.pageYOffset > offset) {
        navbar.classList.add("sticky");
        body.style.paddingTop = navbar.clientHeight + "px";
    }else{
        if(window.pageYOffset <= offset){
            navbar.classList.remove("sticky");
            body.style.paddingTop = "0px";
        }
    }
}

function resetSectionSelection(){
    let scrollY = window.pageYOffset;
    let sections = document.querySelectorAll(".section");
    for (let i = 0; i < sections.length; i++){
        let current = sections[i];
        let sectionHeight = current.offsetHeight;
        let sectionTop = current.offsetTop - (document.querySelector('nav').offsetHeight + 90);
        let el = document.querySelector(".navbar .section-button[data-bs-section*=" + current.getAttribute("id") + "]")

        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            el.classList.add("active");
        }else{
            el.classList.remove("active");
        }
    }
}

function scrollToTop(){
    window.scrollTo(0, 0);
}

function showTopButton(){
    let button = document.getElementById("top-button");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        button.style.display = "block";
    } else {
        button.style.display = "none";
    }
}

function changeLangauge(){
    let language = getCookie("language");
    if(language == ""){
        language = "EN";
    }

    if(language == "EN"){
        setCookie("language", "AR", 360);
    }else{
        setCookie("language", "EN", 360);
    }

    window.location.reload();
}

function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

function hideLoading(){
    let loading_screen = document.getElementById("loading-screen");
    setTimeout(()=>{loading_screen.classList.add("d-none")}, 500);
}

function scrollFade() {
	let viewportBottom = window.scrollY + window.innerHeight;
    let fadeElements = document.getElementsByClassName('section');

	for (let index = 0; index < fadeElements.length; index++) {
		let element = fadeElements[index];
		let rect = element.getBoundingClientRect();

		let elementFourth = rect.height/4;
		let fadeInPoint = (window.innerHeight - 200) - elementFourth;
		let fadeOutPoint = -(rect.height/2);

		if (rect.top <= fadeInPoint) {
			element.classList.add('scrollFade-animate');
		} else {
			element.classList.remove('scrollFade-animate');
		}

		if (rect.top <= fadeOutPoint) {
			element.classList.remove('scrollFade-animate');
		}
	}
}

function displayModal(el){
    let language = getCookie("language");
    if(language == ""){
        language = "EN";
    }

    $('.modal-content').load(el.getAttribute('href'),function(){
        let content_en = document.querySelector('.modal-content .content-en')
        let content_ar = document.querySelector('.modal-content .content-ar')
        if(language == "AR"){
            content_en.classList.add('d-none');
            content_ar.classList.remove('d-none');
        }else{
            content_ar.classList.add('d-none');
            content_en.classList.remove('d-none');
        }
        $('#staticBackdrop').modal({show:true});
    });
}