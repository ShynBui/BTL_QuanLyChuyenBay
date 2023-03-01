function selectFlight(flightId) {
     fetch(`/api/cart/select-flight-${flightId}`, {
        method: "GET",
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then((data) => {
        window.location="/buy-ticket/step-3";
    })
}


function selectSeat(obj, seatID, seatName, seatRankId) {
    fetch(`/api/cart/select-seat-${seatID}`, {
        method: "POST",
        body: JSON.stringify({
            "id": seatID,
            "name": seatName,
            "rank_id": seatRankId
        }),
        headers: {
            "Content-Type": "application/json"
        }
    }).then(res => res.json()).then((data) => {
        if(data['status'] == 201) {
            if(obj.classList.contains("vip-seat"))
                obj.classList.add("selected-vip-seat")
            else
                obj.classList.add("selected-seat")
            obj.innerHTML = seatName
            records = document.querySelectorAll(".record")
            if (records.length > 0)
                records[records.length - 1].insertAdjacentHTML("afterend",
                `
                    <div id="s-${data['cart']['seats'][seatID].id}" class="d-flex record">
                        <div class="col-3">${seatName}</div>
                        <div class="col-5">${data['cart']['seats'][seatID].rank}</div>
                        <div>${(data['cart']['seats'][seatID].price*1000).toLocaleString("en-US") + " VNĐ"}</div>
                    </div>
                `
                );
            else {
                head = document.querySelector(".head-list")
                head.insertAdjacentHTML("afterend",
                `
                    <div id="s-${data['cart']['seats'][seatID].id}" class="d-flex record">
                        <div class="col-3">${seatName}</div>
                        <div class="col-5">${data['cart']['seats'][seatID].rank}</div>
                        <div>${(data['cart']['seats'][seatID].price*1000).toLocaleString("en-US") + " VNĐ"}</div>
                    </div>
                `
                 );
            }
        }
        else if (data['status'] == 200) {
            console.log(data)
            if(obj.classList.contains("vip-seat"))
                obj.classList.remove("selected-vip-seat")
            else
                obj.classList.remove("selected-seat")
            obj.innerHTML = ''
            revSeat = document.getElementById(`s-${data['seat_id']}`)
            revSeat.remove()
        }
        else {
            alert("Đã có lỗi xảy ra")
            window.location="/buy-ticket";
        }
    }).then(update => total())
}

function total() {
    fetch('/api/cart/total').then(res => res.json()).then((data) => {
        var totalPrice = document.querySelector("#total-price")
        totalPrice.innerHTML = (data.total_price*1000).toLocaleString("en-US") + " VNĐ"

        var totalQuantity = document.querySelector("#total-quantity")
        totalQuantity.innerHTML = data.total_quantity + ""

    }).catch(err => console.error(err))
}

function goToStep4(){
    records = document.querySelectorAll(".record")
    if (records.length > 0)
        window.location="/buy-ticket/step-4";
    else
        alert("Bạn chưa chọn ghế")
}