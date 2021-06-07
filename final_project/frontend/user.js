function getInputValue() {
    // Selecting the input element and get its value 
    let inputVal = document.getElementById("myInput").value;

    // Displaying the value
    // alert(inputVal);
    // readQuery(inputVal).catch(console.log);
    // alert(readQuery(inputVal).catch(console.log))
    // console.log('success');

    fetch("http://localhost:3000/name").then(data => data.json()).then(data => {
        console.log("succesffully in user.js")
        console.log(typeof(data));

        let newDiv = document.getElementById("textbox1");
        console.log(newDiv);
        console.log(data);
        newDiv.innerHTML = JSON.stringify(data, null, "  ");
    }).catch();
}