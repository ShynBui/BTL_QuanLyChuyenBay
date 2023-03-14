$(document).ready(function() {

    createHotTourTemplate(hotTours);
    createBg(hotTours);
    createHandBook(handBooks);
    createExperince(experiences);

    $('header, section, footer').addClass('wow animate__fadeIn')

    $('section.hot-tour > div.items div.item').addClass('c4-izmir c4-gradient-top-right')
    $('section.hot-tour > div.items div.item > div.cover').addClass('c4-layout-center-center')
    $('section.hot-tour > div.items div.item > div.cover > div.item-title').addClass('c4-izmir-title-wrapper c4-reveal-up')
    $('section.hot-tour > div.items div.item > div.cover > div.item-title > h3 ~ div').addClass('c4-izmir-title')
    $('section.hot-tour > div.items div.item > div.cover > div.item-info').addClass('c4-izmir-caption-wrapper c4-reveal-down')

    $('section.handbook > div.handbook-content div.handbook-item:nth-child(odd) div.handbook-img').addClass('wow animate__bounceInLeft')
    $('section.handbook > div.handbook-content div.handbook-item:nth-child(even) div.handbook-img').addClass('wow animate__bounceInRight')
    $('section.handbook > div.handbook-content div.handbook-item:nth-child(even) div.handbook-info').addClass('wow animate__bounceInLeft')
    $('section.handbook > div.handbook-content div.handbook-item:nth-child(odd) div.handbook-info').addClass('wow animate__bounceInRight')
    
    $('section.experience > div.content div.E-item:nth-child(odd)').addClass('wow animate__slideInDown')
    $('section.experience > div.content div.E-item:nth-child(even)').addClass('wow animate__slideInUp')

    wow = new WOW ({
        boxClass: 'wow',
        animateClass: 'animate__animated',
        offset: 0,
        mobile: true,
        live: true
    })    
    wow.init();


})

const createStar = (rating) => {
    var star = ''
    for(var i = 0; i < rating; i++)
        star += `<i class='fas fa-star'></i>`
    return star;
}

const createHotTourTemplate = (hotTours) => {
    var output = ''
    hotTours.forEach(hotTour => output += 
        `<div class='flex row33 item col33 '>
            <div class='cover'>
                <div class='item-title'>
                    <h3>${hotTour.name}</h3>
                    <div class='flex'>
                        <div class='rating'>
                            ${createStar(hotTour.star)}
                            <p>${hotTour.review} Đánh giá</p>
                        </div>
                    </div>
                </div>
                <div class='flex item-info'>
                    <div class='flex'>
                        <div>
                            <p><i class='far fa-calendar-alt'></i> Ngày đi: ${hotTour.date}</p>
                            <p><i class='fas fa-dollar-sign'></i> Giá: ${hotTour.priceText}</p>
                            <p><i class='fas fa-map-marker-alt'></i> Nơi khởi hành: Tp HCM</p>
                            <p><i class='fas fa-clock'></i> Số ngày: ${hotTour.period}</p>
                            <p><i class='fas fa-sort-numeric-up-alt'></i> Số lượng: ${hotTour.number} người</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>`);

    $('.cover-items').html(output);
}

const createBg = (arr) => {
    for(var i = 1; i <= arr.length; i++) {
        $(`.item:nth-child(${i})`).addClass(`item${i}`)
    }
}

const createHandBook = (handBooks) => {
    handBooks.forEach((item, index) => {
        var image = `<img src=${item.img} alt=''>`
        var infomation = `
            <h3>${item.name}</h3>
            <p class='date'><i class='far fa-calendar-alt'></i> ${item.date}</p>
            <div class='info'>${item.info}</div>
        `
        $(`.item${++index}-c3`).html(image)
        $(`.item${index}-c7`).html(infomation)
    })
}
const createExperince = (experiences) => {
    var ex = ''
    experiences.forEach(item => {
        ex += `<div class='E-item col33'>
                        <h3>${item.name}</h3>
                        <div class='E-img'>
                            <img src=${item.img} alt=''>
                        </div>
                        <div class='E-info'>${item.info}</div>
                    </div>`
    })

    $('.E-items').html(ex)
}