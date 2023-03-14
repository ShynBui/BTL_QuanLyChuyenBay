function create_options() {
    let option = ''
    fetch("/api/index/")
    .then(res => res.json())
    .then(data => {
        data.forEach((item, index) => {
            option += `<option id="${index}" value="${item.location}">${item.location}</option>`
        })

        let select_container = document.getElementById("validationCustom01");
        select_container.innerHTML = option;
        select_container = document.getElementById("validationCustom02");
        select_container.innerHTML = option;
    })
}

function getCurrentDate() {
    let today = new Date();
    let currentDate = today.toISOString().split('T')[0];
    document.getElementById("validationCustom03").value = currentDate;
}

function create_prices(flight_id) {
    let price = ''
    fetch("/api/index/price/")
    .then(res => res.json())
    .then(data => {
        data.forEach((item, index) => {
            if (item.flight_id == flight_id) {
                price += `<span id="${index}">${item.price}000 VNĐ loại ${item.rank}</span><br>`;
            }
        })
        document.getElementById(`p-${flight_id}`).innerHTML = price;
    })
}