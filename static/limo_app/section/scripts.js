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