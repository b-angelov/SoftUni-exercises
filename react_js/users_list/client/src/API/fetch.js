
async function fetchItems(url="http://localhost:3030/jsonstore/users",failFunc=()=>{}){
    try{
    let response = await fetch(url);
    response = await response.json();
    return response;}catch{
        failFunc()
    }
}

async function addItem(data,method="POST",url="http://localhost:3030/jsonstore/users"){
    const controller = new AbortController()
    const signal = controller.signal
    setTimeout(() => controller.abort(), 8000)

    let response = await fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    },{signal});
    response = await response.json();
    return response;
}

async function deleteItem(id,url="http://localhost:3030/jsonstore/users"){
    let response = await fetch(url + `/${id}`, {
        method: "DELETE",
        headers: {"Content-Type": "application/json"},
    });
    response = await response.json();
    return response;
}

export {fetchItems, addItem, deleteItem}