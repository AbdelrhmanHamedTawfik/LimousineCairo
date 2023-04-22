adjustRequests()
highlightPage("requests-page")

function markAsRead(type, id){
    let url = "update-order"
    let target = "#order-" + id
    let data = new FormData();
    data.append('id', id);

    if(type != 1){
        url = "update-complain"
        target = "#complain-" + id
    }

    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        processData: false,
        contentType: false,
        success: function(data) {
            if(data.success){
                let target_div = document.querySelector(target + " .new-icon")
                target_div.classList.add("read")

                if(data.show_notifications){
                    let notifcation = $("#notification")
                    if(notifcation != null || notifcation != undefined){
                        notifcation.removeClass("d-none")
                    }
                }else{
                    let notifcation = $("#notification")
                    if(notifcation != null || notifcation != undefined){
                        notifcation.addClass("d-none")
                    }
                }
            }
        }
    });
}

function adjustRequests(){
    if($(window).width() < 800) {
        let orders = document.querySelectorAll(".bookings-item")
        let complains = document.querySelectorAll(".complains-item")
        for(let i = 0; i < orders.length; i++){
            orders[i].classList.add("collapsed")
            orders[i].setAttribute("onclick", 'showOrder(this)')
        }

        for(let i = 0; i < complains.length; i++){
            complains[i].classList.add("collapsed")
            complains[i].setAttribute("onclick", 'showComplain(this)')
        }
    }
}

function showOrder(el){
    if(!el.classList.contains("collapsed")){
        el.classList.add("collapsed")
        return
    }
    let orders = document.querySelectorAll(".bookings-item")
    for(let i = 0; i < orders.length; i++){
        if(!orders[i].classList.contains("collapsed")){
            orders[i].classList.add("collapsed")
        }
    }

    el.classList.remove("collapsed")
    
}

function showComplain(el){
    if(!el.classList.contains("collapsed")){
        el.classList.add("collapsed")
        return
    }

    let complains = document.querySelectorAll(".complains-item")
    for(let i = 0; i < complains.length; i++){
        if(!complains[i].classList.contains("collapsed")){
            complains[i].classList.add("collapsed")
        }
    }

    el.classList.remove("collapsed")
}