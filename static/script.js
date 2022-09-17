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

document.addEventListener('DOMContentLoaded', function () {
    const person = {"":"Hello, there! I'm Bunny", "positive":"Wow! I wish you the best of hoppiness always :)", "neutral":"*Carrot crunch* I'm all ears to hear more.", "negative":"I feel you. I'm sure it will only get better!"};
    document.getElementById("speech").innerHTML = person[label];
    console.log(document.getElementById("speech").innerHTML, person[label])
})


