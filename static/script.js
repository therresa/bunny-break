// if (localStorage.getItem("points") === null) {
//     localStorage.setItem('points', 0)
// }

document.getElementById("chatbox-icon").onclick = function (e) {
    document.getElementById('chatbox-title').style.display = "block";
    document.getElementById('toggle-form-area').style.display = "block";
    document.getElementById('minimize').style.display = "block";
}


document.getElementById("minimize").onclick = function (e) {
    document.getElementById('chatbox-title').style.display = "none";
    document.getElementById('toggle-form-area').style.display = "none";
    document.getElementById('minimize').style.display = "none";
}


