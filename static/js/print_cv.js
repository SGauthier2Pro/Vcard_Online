window.addEventListener("load", () => {
  window.onprint = function(){
    history.back();
  }
});