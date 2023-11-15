window.addEventListener("load", () => {
  window.onafterprint = function(){
    history.back();
  }
});