function visible_id_flight(medium_num) {
    if(medium_num > 0) {
        document.getElementById("id").setAttribute("disabled", "")
    }
}


function visible_medium(isMedium) {
    let number_items = document.getElementsByClassName("input-number")
    if(isMedium.checked) {
        for (let i = 0; i < number_items.length; i++)
            number_items[i].removeAttribute("disabled")
    }
    else {
        for (let i = 0; i < number_items.length; i++) {
            number_items[i].checked = false
            number_items[i].setAttribute("disabled", "")
        }
        document.getElementById("medium").innerHTML = ""
    }
}


function create_options(id) {
    let option = ''
    fetch("/api/admin/flights/new/")
    .then(res => res.json())
    .then(data => {
        data.forEach((item, index) => {
            option += `<option id="${index}" value="${item.name}">${item.name}</option>`
        })

        const select_container = document.getElementById(`form-select-${id}`);
        select_container.innerHTML = option;
    })
}


function number_of_mediums(str_number) {
    const number = Number(str_number)
    let h = "";
    for (let i = 0; i < number; i++) {
        h += `
            <div class="medium-item${i}">
                <hr>
                <div class="form-group ">
                    <label for="name-stop-${i}" class="control-label">Tên trạm
                        <strong style="color: red">*</strong>
                    </label>
                    <input class="form-control" id="name-stop-${i}" required
                           maxlength="50" name="name-stop-${i}" type="text" value="">
                </div>
                <div class="form-group ">
                    <label for="stop-time-begin-${i}" class="control-label">Thời gian bắt đầu dừng
                        <strong style="color: red">*</strong>
                    </label>
                    <input class="form-control" id="stop-time-begin-${i}" required
                           maxlength="50" name="stop-time-begin-${i}" type="datetime-local" value="">
                </div>
                <div class="form-group ">
                    <label for="stop-time-finish-${i}" class="control-label">Thời gian dừng kết thúc
                        <strong style="color: red">*</strong>
                    </label>
                    <input class="form-control" id="stop-time-finish-${i}" required
                           maxlength="50" name="stop-time-finish-${i}" type="datetime-local" value="">
                </div>
                <div class="form-group ">
                    <label for="description-${i}" class="control-label">Mô tả</label>
                    <input class="form-control" id="description-${i}"
                           maxlength="200" name="description-${i}" type="text" value="">
                </div>
                <div class="group-special">
                    <div class="form-group">
                        <label class="control-label">Sân bay dừng
                            <strong style="color: red">*</strong>
                        </label>
                        <select class="form-select" id="form-select-${i}"
                        name="form-select-${i}" aria-label="Default select example">
                            ${create_options(i)}
                        </select>
                    </div>
                </div>
            </div>
            `
    }

    let d = document.getElementById("medium")
    d.innerHTML = h;
}