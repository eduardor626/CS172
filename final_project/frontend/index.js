const { Client } = require('@elastic/elasticsearch')
const express = require('express');
const app = express();


const config = require('config');
const elasticConfig = config.get('elastic');

const client = new Client({
    cloud: {
        id: elasticConfig.cloudID
    },
    auth: {
        username: elasticConfig.username,
        password: elasticConfig.password
    },
    node: 'http://localhost:9200'
})


//currently getting errors when trying to read the data.. maybe cause its in one line?
var json = require('../scrapedData.json');
const dataset = json

// client.info()
//     .then(response => console.log(response))
//     .catch(error => console.error(error))


async function run() {
    await client.indices.create({
        index: 'test',
        body: {
            mappings: {
                properties: {
                    id: { type: 'integer' },
                    url: { type: 'url' },
                    text: { type: 'text' },
                    time: { type: 'date' }
                }
            }
        }
    }, { ignore: [400] })

    // var dataset = json;
    // console.log(dataset);

    const body = dataset.flatMap(doc => [{ index: { _index: 'test' } }, doc])

    const { body: bulkResponse } = await client.bulk({ refresh: true, body })

    if (bulkResponse.errors) {
        const erroredDocuments = []
            // The items array has the same order of the dataset we just indexed.
            // The presence of the `error` key indicates that the operation
            // that we did for the document has failed.
        bulkResponse.items.forEach((action, i) => {
            const operation = Object.keys(action)[0]
            if (action[operation].error) {
                erroredDocuments.push({
                    // If the status is 429 it means that you can retry the document,
                    // otherwise it's very likely a mapping error, and you should
                    // fix the document before to try it again.
                    status: action[operation].status,
                    error: action[operation].error,
                    operation: body[i * 2],
                    document: body[i * 2 + 1]
                })
            }
        })
        console.log(erroredDocuments)
    }


    const { body: count } = await client.count({ index: 'test' })

    console.log(count)
    console.log(body);
    // return cluster.hits.hits;
    return body;
}

async function getBody() {
    // const body = dataset.flatMap(doc => [{ index: { _index: 'test' } }, doc])
    const { body: me } = await client.search({
        index: 'test',
        body: {
            query: {
                match_all: {}
            }
        }
    })
    console.log(me.hits.hits);
    return me.hits.hits;
}

// run().catch(console.log)

async function readAll() {
    console.log('reading from cluster')
    const { body } = await client.search({
        index: 'test',
        body: {
            query: {
                match_all: {}
            }
        }
    })
    console.log('hits!!');
    console.log(body.hits.hits)
    return body.hits.hits;

}

readAll().catch(console.log);


async function readQuery(query) {
    console.log('in read query');
    const { body } = await client.search({
        index: 'test',
        body: {
            query: {
                match: { html: query }
            }
        }
    })
    console.log('Searching for Query: ' + query);
    console.log(body.hits.hits)
    return body.hits.hits;
}
// readQuery('Symptom Monitoring Survey').catch(console.log);

app.get("/name", (req, res) => {
    readAll().catch(console.log).then(data => {
        res.send(data);
    });
})



app.get("/delete", (req, res) => {
    deleteAll();

    res.redirect("/");

})

app.get("/create", (req, res) => {
    console.log('inside data function');
    run().catch(console.log).then(data => {
        res.send(data);
    });
})


app.get('/getAll', (req, res) => {
    getBody().catch(console.log).then(data => {
        res.send(data);
    });

})

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
})

//how we 
app.get('/user.js', (req, res) => {
    res.sendFile(__dirname + '/user.js');
})

app.get('/style.css', (req, res) => {
    res.sendFile(__dirname + '/style.css');
})

app.get("/search/:query", (req, res) => {
    var query = req.params.query;
    console.log(query);
    readQuery(query).catch(console.log).then(data => {
        res.send(data);
    })
})


// function getInputValue() {
//     console.log('in here!!');
//     // Selecting the input element and get its value 
//     let inputVal = document.getElementById("myInput").value;
//     // Displaying the value
//     alert(inputVal);
//     return readQuery(inputVal).catch(console.log);
// }

function deleteAll() {
    console.log('in delete all');
    client.indices.delete({
        index: 'test',
    }).then(function(resp) {
        console.log("Successful query!");
        console.log(JSON.stringify(resp, null, 4));
    }, function(err) {
        console.trace(err.message);
    });

}


app.listen(3000, () => {
    console.log("listening on the port 3000 ");
})