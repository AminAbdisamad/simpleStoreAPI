document.getElementById('btn').addEventListener('click', function(e) {
  //   function for retreiving data
  getData('http://127.0.0.1:4000/store');
});

function getData(url) {
  const xr = new XMLHttpRequest();
  xr.open('GET', url, true);
  xr.onload = function() {
    if (this.status === 200) {
      console.log(this.response);
      //   document.querySelector('.output').innerHTML = this.response;
    }
  };
  xr.send();
}
