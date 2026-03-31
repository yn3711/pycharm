window.onload = function() {
  var e = document.getElementById('test');
  e.style.color = 'blue';
  //console.log('test');
  //alert("test");
}

history.pushState(null, null, location.href);
window.addEventListener('popstate', (e) => {
  history.go(1);
  alert("こんにちは");
});