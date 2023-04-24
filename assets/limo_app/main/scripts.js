window.onload = function(){
    scrollToTop();
    hideLoading();
};

window.onscroll = function(){
    showTopButton();
    resetSectionSelection();
};

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

function changeLangauge(language){
    setCookie("language", language, 360);
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

function showModal(modal_type){
    let booking = document.querySelector('#booking-modal')
    let issues = document.querySelector('#issue-modal')
    let success_screen = document.querySelector('#success-screen')
    let fail_screen = document.querySelector('#fail-screen')
    success_screen.classList.remove("active")
    fail_screen.classList.remove("active")

    if(modal_type == 1){
        booking.classList.remove("d-none")
        issues.classList.add("d-none")
    }else{
        booking.classList.add("d-none")
        issues.classList.remove("d-none")
    }

    $('#bookModal').modal('show');
}

function validateForm(form_type){
    let form = document.querySelectorAll('.needs-validation')[0]
    if(form_type != 1){
        form = document.querySelectorAll('.needs-validation')[1]
    }
    if (form.checkValidity() === false) {
        form.classList.add('was-validated');
        return false;
    } else {
        let data = new FormData();
        let name = $('#name-field').val()
        let phone = $('#phone-field').val()
        let date = $('#date-field').val()
        let car = $('#car-field').val()
        let details = $('#details-field').val()
        
        if(form_type != 1){
            name = $('#name-field-2').val()
            phone = $('#phone-field-2').val()
            details = $('#details-field-2').val()
        }
        
        
        data.append('name', name);
        data.append('phone', phone);
        data.append('date', date);
        data.append('car', car);
        data.append('details', details);
        data.append('form_type', form_type);
        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });
        $.ajax({
            type: 'POST',
            url: 'order-complain',
            data: data,
            processData: false,
            contentType: false,
            success: function(data) {
                let success_screen = document.querySelector('#success-screen')
                let fail_screen = document.querySelector('#fail-screen')
                if(data.success){
                    success_screen.classList.add("active")
                    let notifcation = $("#notification")
                    if(notifcation != null || notifcation != undefined){
                        notifcation.removeClass("d-none")
                    }
                }else{
                    fail_screen.classList.add("active")
                }
            }
        });

        return true;
    }
}

function hideLoading(){
    let loading_screen = document.getElementById("loading-screen");
    setTimeout(()=>{loading_screen.classList.add("d-none")}, 500);
}

function highlightPage(page_id){
    $('.navbar-nav li').removeClass("active")
    $('#' + page_id).addClass("active")
}