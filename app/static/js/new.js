// window.onload = function(){
//     var hw = document.getElementById('about');
//     hw.addEventListener('click', function(){
//         alert('Hello world');
//     })
// }

// document.getElementById("about").onclick = function () {
//   alert('hello!');
//
// };
var pre_elem = document.getElementById("home");

function onClicked(elem) {

  // test

  // test
  if(pre_elem != elem) {
    pre_elem.classList.remove('active');
    elem.classList.add('active');

    var pre_elemContents = pre_elem.id + '_contents'
    var elemContents = elem.id + '_contents'



    elemContents = document.getElementById(elemContents);
    pre_elemContents = document.getElementById(pre_elemContents);

    elemContents.style.display = 'block';
    pre_elemContents.style.display = 'none';

    pre_elem = elem;
  }
}
