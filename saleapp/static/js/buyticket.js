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