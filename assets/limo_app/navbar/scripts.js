function scrollToSection(section){
    let el = document.getElementById(section);
    let current = document.querySelector("#navbar");
    $(window).scrollTop($(el).position().top);

}

function resetSectionSelection(){
    let sections_data = getSectionsData();
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        let scrollY = window.pageYOffset;
        for (let section in sections_data){
            let el = document.querySelectorAll(".sections-buttons .section-item")[section]
            // console.log(el)
            if (scrollY > sections_data[section].top && scrollY <= sections_data[section].top + sections_data[section].height){
                el.classList.add("active");
            }else{
                el.classList.remove("active");
            }
        }
    }
}

function getSectionsData(){
    let sections = document.querySelectorAll(".section:not(#sepcial-section)");
    let sections_data = {}
    for (let i = 0; i < sections.length; i++){
        let current = sections[i];
        if(current.getAttribute("id") == "sepcial-section"){
            continue;
        }

        let sectionHeight = current.offsetHeight;
        let sectionTop = current.offsetTop - 120;
        sections_data[i] = {height:sectionHeight, top:sectionTop}
    }
    
    return sections_data
}