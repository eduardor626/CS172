# getting the deployment instance
curl -u elastic:YyiJ5D5IYVz7D99wHtDwvdAS  
"https://cs172-deployment-925d89.es.us-west1.gcp.cloud.es.io:9243"



#command to create index
curl -X PUT -u elastic:YyiJ5D5IYVz7D99wHtDwvdAS https://cs172-deployment-925d89.es.us-west1.gcp.cloud.es.io:9243/
myindex\?pretty

#now that the index is created we must figure out how to populate it?

 curl -X PUT -u elastic:YyiJ5D5IYVz7D99wHtDwvdAS "https://cs172-deployment-925d89.es.us-west1.gcp.cloud.es.io:9243/_doc/1" -H
'Content-Type: Application/json' -d'{"html": "<td><tr>span<td></tr>"}' 



curl -X GET -u elastic:YyiJ5D5IYVz7D99wHtDwvdAS "https://cs172-deployment-925d89.es.us-west1.gcp.cloud.es.io:9243/myindex-100/_search?pretty" -H 'Content-Type: application/json' -d'
{
    "query": {
        "match_all": {}
    }
}
'

curl -X PUT -u elastic:YyiJ5D5IYVz7D99wHtDwvdAS https://cs172-deployment-925d89.es.us-west1.gcp.cloud.es.io:9243/myindex-100/_doc/2 -H 'Content-Type: application/json' -d'{"html": "<td><tr>span<td></tr>"}'