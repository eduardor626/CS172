function getInputValue() {
    // Selecting the input element and get its value 
    let inputVal = document.getElementById("myInput").value;

    fetch("http://localhost:3000/name").then(data => data.json()).then(data => {
        console.log("succesffully in user.js")
            // console.log(typeof(data));

        let newDiv = document.getElementById("textbox1");
        console.log(newDiv);
        console.log(data);
        newDiv.innerHTML = JSON.stringify(data, null, "  ");
    }).catch();
}

function clearValues() {
    fetch("http://localhost:3000/delete").then(data => {
        console.log(data);
        let newDiv = document.getElementById("textbox1");
        let value = "deleted data"
        newDiv.innerHTML = value;
    }).catch();
}

function createCluster() {
    fetch("http://localhost:3000/create").then(data => {
        console.log('successfully created')
        let newDiv = document.getElementById("textbox1");
        newDiv.innerHTML = "The Cluser has been created!";
    }).catch();
}