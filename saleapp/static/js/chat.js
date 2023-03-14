var animate = document.getElementsByClassName("fa-comments");

var c = ["blue", "red", "gray", "green", "pink", "purple", "orange"]
var index = 0;

function changeColor() {
    if(index > c.length) {
        index = 0;
    }

    animate[0].style.color = c[index];
    index++;
}

setInterval(changeColor, 300);