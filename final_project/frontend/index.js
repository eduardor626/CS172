const { Client } = require('@elastic/elasticsearch')
const config = require('config');
const elasticConfig = config.get('elastic');

//currently getting errors when trying to read the data.. maybe cause its in one line?
let json = require('../frontend/random.json');
// console.log(json);


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


// client.info()
//     .then(response => console.log(response))
//     .catch(error => console.error(error))

// async function run() {
//     await client.indices.create({
//         index: 'tweets',
//         body: {
//             mappings: {
//                 properties: {
//                     id: { type: 'integer' },
//                     url: { type: 'url' },
//                     text: { type: 'text' },
//                     time: { type: 'date' }
//                 }
//             }
//         }
//     }, { ignore: [400] })

// const dataset = [{
//     id: 1,
//     url: 'https://cen.ucr.edu/',
//     text: 'If I fall, don\'t bring me back.',
//     date: new Date()
// }, {
//     id: 2,
//     url: 'https://cen.ucr.edu/',
//     text: 'Winter is coming',
//     date: new Date()
// }, {
//     id: 3,
//     url: 'https://cen.ucr.edu/',
//     text: 'A Lannister always pays his debts.',
//     date: new Date()
// }, {
//     id: 4,
//     url: 'https://cen.ucr.edu/',
//     text: 'I am the blood of the dragon.',
//     date: new Date()
// }, {
//     id: 5, // change this value to a string to see the bulk response with errors
//     url: 'https://cen.ucr.edu/',
//     text: 'A girl is Arya Stark of Winterfell. And I\'m going home.',
//     date: new Date()
// }]
// console.log(typeof(dataset));
//     dataset = json;

//     const body = dataset.flatMap(doc => [{ index: { _index: 'tweets' } }, doc])

//     const { body: bulkResponse } = await client.bulk({ refresh: true, body })

//     if (bulkResponse.errors) {
//         const erroredDocuments = []
//             // The items array has the same order of the dataset we just indexed.
//             // The presence of the `error` key indicates that the operation
//             // that we did for the document has failed.
//         bulkResponse.items.forEach((action, i) => {
//             const operation = Object.keys(action)[0]
//             if (action[operation].error) {
//                 erroredDocuments.push({
//                     // If the status is 429 it means that you can retry the document,
//                     // otherwise it's very likely a mapping error, and you should
//                     // fix the document before to try it again.
//                     status: action[operation].status,
//                     error: action[operation].error,
//                     operation: body[i * 2],
//                     document: body[i * 2 + 1]
//                 })
//             }
//         })
//         console.log(erroredDocuments)
//     }

//     const { body: count } = await client.count({ index: 'tweets' })
//     console.log(count)
// }

// run().catch(console.log)

// async function readAll() {
//     const { body } = await client.search({
//         index: 'tweets',
//         body: {
//             query: {
//                 match_all: {}
//             }
//         }
//     })
//     console.log('hits!!');
//     console.log(body.hits.hits)
// }
// readAll().catch(console.log)


// async function readQuery(query) {
//     const { body } = await client.search({
//         index: 'tweets',
//         body: {
//             query: {
//                 match: { html: query }
//             }
//         }
//     })
//     console.log('Searching for Query...' + query);
//     console.log(body.hits.hits)
// }
// readQuery('Optimized Sensing and Recovery').catch(console.log);

// client.indices.delete({
//     index: 'tweets',
// }).then(function(resp) {
//     console.log("Successful query!");
//     console.log(JSON.stringify(resp, null, 4));
// }, function(err) {
//     console.trace(err.message);
// });