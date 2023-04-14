function createDiv() {
    // create a new div element
    var newDiv = document.createElement("div");
    
    // add some text to the div
    var newContent = document.createTextNode("Hello, world!");
    newDiv.appendChild(newContent);
    
    // add some style to the div
    newDiv.style.position = "absolute";
    newDiv.style.top = "400px";
    newDiv.style.left = "20px";
    newDiv.style.width = "250px";
    newDiv.style.height = "300px";
    newDiv.style.backgroundColor = "#12384A";
    newDiv.style.padding = "10px";
    newDiv.style.border = "3px solid #fba026";
    newDiv.style.borderRadius = "20px";
    newDiv.style.color = "white";
    
    // add the div to the container
    var container = document.getElementById("container");
    container.appendChild(newDiv);
    
    // save the div to local storage
    localStorage.setItem("myDiv", container.innerHTML);
  }
  
  // load the saved div from local storage on page load
//   window.onload = function() {
//     var container = document.getElementById("container");
//     container.innerHTML = localStorage.getItem("myDiv");
//   };
  