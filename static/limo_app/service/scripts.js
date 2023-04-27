drawRelatedTopics();
highlightPage("services-page")

function moveToSelected(element) {
    if(element == null || element == undefined || $(".topic-item").length <= 1){
        return 
    }
    
    let selected = element;
    if (selected.classList.contains("next")) {
        selected = $(".selected").next();
    } else if (selected.classList.contains("prev")) {
        selected = $(".selected").prev();
    }

    let next = $(selected).next();
    if(next.length == 0){
        $("#right-button").addClass("disabled")
    }else{
        $("#right-button").removeClass("disabled")
    }

    let prev = $(selected).prev();
    if(prev.length == 0){
        $("#left-button").addClass("disabled")
    }else{
        $("#left-button").removeClass("disabled")
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

    $(nextSecond).nextAll().removeClass().addClass('topic-item');
    $(nextSecond).nextAll().addClass('hideRight');

    $(prevSecond).prevAll().removeClass().addClass('topic-item');
    $(prevSecond).prevAll().addClass('hideLeft');

}

function drawRelatedTopics(){
    let topics = document.querySelectorAll(".topic-item")
    if(topics.length <= 0){
        return
    }
    
    let mid_index = Math.floor(topics.length/2)
    topics[mid_index].classList.add("selected")

    if(topics[mid_index + 1]){
        topics[mid_index + 1].classList.add("next")
    }

    if(topics[mid_index - 1]){
        topics[mid_index - 1].classList.add("prev")
    }

    if(topics[mid_index + 2]){
        topics[mid_index + 2].classList.add("nextRightSecond")
    }

    if(topics[mid_index - 2]){
        topics[mid_index - 2].classList.add("prevLeftSecond")
    }

    for(let i = mid_index+3; i < topics.length; i++ ){
        topics[i].classList.add("hideRight")
    }

    for(let i = 0; i < mid_index-2; i++ ){
        topics[i].classList.add("hideLeft")
    }

    let next = document.querySelectorAll(".topic-item.next")
    let prev = document.querySelectorAll(".topic-item.prev")
    if(next.length < 1){
        $("#right-button").addClass("disabled")
    }

    if(prev.length < 1){
        $("#left-button").addClass("disabled")
    }
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