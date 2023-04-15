function moveToSelected(element) {
    let selected = element;
    if (selected.classList.contains("next")) {
        selected = $(".selected").next();
        if(selected.length == 0){
            selected = element
        }
    } else if (selected.classList.contains("prev")) {
        selected = $(".selected").prev();
        if(selected.length == 0){
            selected = element
        }
    }

    let next = $(selected).next();
    if(next.length == 0){
        next = $(".topic-item")[0]
    }

    let prev = $(selected).prev();
    if(prev.length == 0){
        prev = $(".topic-item")[$(".topic-item").length-1]
    }

    let prevSecond = $(prev).prev();
    let nextSecond = $(next).next();
    
    $(selected).removeClass().addClass("topic-item");
    $(selected).addClass("selected");

    $(prev).removeClass().addClass("topic-item");
    $(prev).addClass("prev");

    $(next).removeClass().addClass("topic-item");
    $(next).addClass("next");

    $(nextSecond).removeClass().addClass("topic-item");
    $(nextSecond).addClass("nextRightSecond");

    $(prevSecond).removeClass().addClass("topic-item");
    $(prevSecond).addClass("prevLeftSecond");

    $(nextSecond).next().removeClass().addClass('topic-item');
    $(nextSecond).next().addClass('hideRight');

    $(prevSecond).prev().removeClass().addClass('topic-item');
    $(prevSecond).prev().addClass('hideLeft');

}

function switchTab(tab_index){
    let tabs = document.querySelectorAll(".tab");
    let secions = document.querySelectorAll(".services-section");
    let active_section = document.querySelectorAll(".services-section.active")[0];

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