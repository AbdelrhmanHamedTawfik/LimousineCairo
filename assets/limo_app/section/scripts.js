function animateSocial(el, isEnter) {
    el.classList.remove("in-active")
    el.classList.remove("active")
     requestAnimationFrame(() => {
      requestAnimationFrame(() => {
            if(isEnter){
                el.classList.add("active")
                el.classList.remove("in-active")
            }else{
                el.classList.add("in-active")
                el.classList.remove("active")
            }
      });
    });  
}

function selectRate(el) {
    el.classList.add("active")
    let pre_elms = document.querySelectorAll(".review-star")
    for(let i=0; i<pre_elms.length; i++){
        if(pre_elms[i] == el){
            break;
        }else{
            pre_elms[i].classList.add("active")
        }
    }
}

function deSelectRate(el) {
    if(!el.classList.contains("selected")){
        el.classList.remove("active")
    }
    
    let pre_elms = document.querySelectorAll(".review-star")
    for(let i=0; i<pre_elms.length; i++){
        if(pre_elms[i] == el){
            break;
        }else{
            if(!pre_elms[i].classList.contains("selected")){
                pre_elms[i].classList.remove("active")
            }
        }
    }
}

function setRating(el){
    let pre_elms = document.querySelectorAll(".review-star")
    for(let i=0; i<pre_elms.length; i++){
        pre_elms[i].classList.remove("active")
        pre_elms[i].classList.remove("selected")
    }

    el.classList.add("active")
    el.classList.add("selected")
    for(let i=0; i<pre_elms.length; i++){
        if(pre_elms[i] == el){
            break;
        }else{
            pre_elms[i].classList.add("active")
            pre_elms[i].classList.add("selected")
        }
    }
}

function submitReview(){
    let form = document.querySelectorAll('#needs-validation-review')[0]
    let ratings_starts = document.querySelectorAll('.review-star.active.selected').length

    if (form.checkValidity() === false) {
        form.classList.add('was-validated');
        return false;
    } else {
        let data = new FormData();
        let name = $('#review-name-field').val()
        let quote = $('#review-quote-field').val()
        
        data.append('name', name);
        data.append('quote', quote);
        data.append('rating', ratings_starts);

        $.ajaxSetup({
            headers: { "X-CSRFToken": getCookie("csrftoken") }
        });

        $.ajax({
            type: 'POST',
            url: 'insert-review',
            data: data,
            processData: false,
            contentType: false,
            success: function(data) {
                if(data.success){
                    let language = getCookie("language")
                    let msg = "Thank you for submitting a review"

                    if(language == "AR"){
                        msg = "شكرا لارسالكم التقييم"
                    }

                    alert(msg);
                    window.location.reload()

                }else{
                    let language = getCookie("language")
                    let msg = "There was an Error please try again later"

                    if(language == "AR"){
                        msg = "حدث خطا يرجي الماولة في وقت لاحق"
                    }

                    alert(msg);
                    window.location.reload()
                }
            }
        });

        return true;
    }
}
