var updateBtns = document.getElementsByClassName("update-cart")

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var item_id = this.dataset.item
        var action = this.dataset.action
        console.log("item_id:", item_id, "action:", action)
        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log("User not logged in")
        } else {
            console.log("User logged in...")
            updateUserOrder(item_id, action)
        }
    })
}

function updateUserOrder(item_id, action){
    var url = "/update_item/"

    fetch(url, {
        method:'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'item_id':item_id, 'action':action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}