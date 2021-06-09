function getInputValue() {
    // Selecting the input element and get its value 
    let inputVal = document.getElementById("myInput").value;

    fetch("http://localhost:3000/name").then(data => data.json()).then(data => {
        console.log("succesffully in user.js")
            // console.log(typeof(data));

        let newDiv = document.getElementById("textbox1");
        console.log(newDiv);
        console.log(data);

        // newDiv.innerHTML = JSON.stringify(data, null, "  ");

        // EXTRACT VALUE FOR HTML HEADER. 
        // ('Book ID', 'Book Name', 'Category' and 'Price')
        var col = [];
        for (var i = 0; i < data.length + 2; i++) {
            for (var key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                    console.log(key);
                }
            }
        }
        console.log(col);

        // CREATE DYNAMIC TABLE.
        var table = document.createElement("table");

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        var tr = table.insertRow(-1); // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th"); // TABLE HEADER.
            th.innerHTML = col[i].substring(1);
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < data.length; i++) {
            tr = table.insertRow(-1);
            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);

                if (col[j] == "_source") {
                    console.log(data[i][col[j]].url)
                    console.log("url exists!!!");
                    tabCell.innerHTML = data[i][col[j]].url;
                } else {
                    tabCell.innerHTML = data[i][col[j]];
                }
            }
        }
        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        newDiv.innerHTML = "";
        newDiv.appendChild(table);


    }).catch();
}

function getAll() {

    let inputVal = document.getElementById("myInput").value;

    fetch("http://localhost:3000/getAll").then(data => data.json()).then(data => {
        console.log(data);
        let newDiv = document.getElementById("textbox1");
        // console.log(data);

        // newDiv.innerHTML = JSON.stringify(data, null, "  ");

        // EXTRACT VALUE FOR HTML HEADER. 
        // ('Book ID', 'Book Name', 'Category' and 'Price')
        var col = [];
        for (var i = 0; i < data.length; i++) {
            for (var key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                    console.log(key);

                }
            }
        }
        col.append('url');
        console.log(col);

        // CREATE DYNAMIC TABLE.
        // var table = document.createElement("table");

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        // var tr = table.insertRow(-1); // TABLE ROW.

        // for (var i = 0; i < col.length; i++) {
        //     var th = document.createElement("th"); // TABLE HEADER.
        //     th.innerHTML = col[i].substring(1);
        //     tr.appendChild(th);
        // }

        // // ADD JSON DATA TO THE TABLE AS ROWS.
        // for (var i = 0; i < data.length; i++) {
        //     tr = table.insertRow(-1);
        //     for (var j = 0; j < col.length; j++) {
        //         var tabCell = tr.insertCell(-1);

        //         if (col[j] == "_source") {
        //             console.log(data[i][col[j]].url)
        //             console.log("url exists!!!");
        //             tabCell.innerHTML = data[i][col[j]].url;
        //         } else {
        //             tabCell.innerHTML = data[i][col[j]];
        //         }
        //     }
        // }
        // // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        // newDiv.innerHTML = "";
        // newDiv.appendChild(table);


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

function searchQuery() {
    var element = document.getElementById("myInput").value;
    console.log(element);
    var str = "http://localhost:3000/search/" + element;
    console.log(str);
    fetch(str).then(data => data.json()).then(data => {
        console.log("succesffully in searchquery in user.js")

        let newDiv = document.getElementById("textbox1");
        console.log(newDiv);
        console.log(data);
        // newDiv.innerHTML = JSON.stringify(data, null, "  ");

        // EXTRACT VALUE FOR HTML HEADER. 
        // ('Book ID', 'Book Name', 'Category' and 'Price')
        var col = [];
        for (var i = 0; i < data.length + 2; i++) {
            for (var key in data[i]) {
                if (col.indexOf(key) === -1) {
                    col.push(key);
                    console.log(key);
                }
            }
        }
        console.log(col);

        // CREATE DYNAMIC TABLE.
        var table = document.createElement("table");

        // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.

        var tr = table.insertRow(-1); // TABLE ROW.

        for (var i = 0; i < col.length; i++) {
            var th = document.createElement("th"); // TABLE HEADER.
            th.innerHTML = col[i].substring(1);
            tr.appendChild(th);
        }

        // ADD JSON DATA TO THE TABLE AS ROWS.
        for (var i = 0; i < data.length; i++) {
            tr = table.insertRow(-1);
            for (var j = 0; j < col.length; j++) {
                var tabCell = tr.insertCell(-1);

                if (col[j] == "_source") {
                    console.log(data[i][col[j]].url)
                    console.log("url exists!!!");
                    tabCell.innerHTML = data[i][col[j]].url;
                } else {
                    tabCell.innerHTML = data[i][col[j]];
                }
            }
        }
        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
        newDiv.innerHTML = "";
        newDiv.appendChild(table);


    }).catch();

}