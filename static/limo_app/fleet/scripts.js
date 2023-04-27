highlightPage("fleet-page")

function switchTab(tab_index){
    let tabs = document.querySelectorAll(".tab");
    let secions = document.querySelectorAll(".fleet-section");
    let active_section = document.querySelectorAll(".fleet-section.active")[0];

    active_section.classList.add("pre-active");
    active_section.classList.remove("active");
    
    setTimeout(function() {
        active_section.classList.remove("pre-active");
        secions[tab_index].classList.add("active");
    }, 400);
    

    for(let i = 0; i < tabs.length; i++){
        tabs[i].classList.remove("active")
    }
    tabs[tab_index].classList.add("active")
}