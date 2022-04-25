let sideMenu = document.querySelector('#side-menu');
let sideBar = document.querySelector('.side-bar');

sideMenu.onclick = () =>{
   sideMenu.classList.toggle('fa-times');
   sideBar.classList.toggle('active');
};



document.querySelector('.reset-btn .btn').onclick = () =>{
   window.location.reload();
};



// scroll top
let span = document.querySelector(".top");

window.onscroll = function () {
   console.log(window.scrollY);
   if (window.scrollY >= 100) {
      span.style.display = "block";
   } else {
      span.style.display = "none";
   }
   //  this.scrollY >= 100 ? span.style.display = "block" : span.style.display = "none";
};

span.onclick = function () {
   window.scrollTo({
   top: 0,
   behavior: "smooth",
   });
};



// search
const search = () => {
    const searchbox = document.getElementById("search-box").value.toUpperCase();
    const storeitems = document.getElementById("product-list");
    const product = document.querySelectorAll(".cars-list");
    const pname = storeitems.getElementsByTagName("h3");

    for (var i = 0; i < pname.length; i++) {
        let match = product[i].getElementsByTagName('h3')[0];

        if (match) {
            let textvalue = match.textContent || match.innerHTML;

            if (textvalue.toUpperCase().indexOf(searchbox) > -1) {
            product[i].style.display = "";
            } else {
            product[i].style.display = "none";
            }
        }
    }
}




// cars
const product = [
    {
        "id": 1,
        "name": "JEEP 2019",
        "price": 15.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22607892/1_cleaned.jpg?width=800",
        "discription": "Fusion SE",
        "brand": "Chevrolet",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 2,
        "name": "2017 Chevrolet",
        "price": 37.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/22378856/1_cleaned.jpg?width=800",
        "discription": "Camaro SS",
        "brand": "Chevrolet",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 3,
        "name": "2015 Ford",
        "price": 21.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/21627904/1_cleaned.jpg?width=800",
        "discription": "Explorer Limited",
        "brand": "ford",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 4,
        "name": "2019 BMW",
        "price": 38.998,
        "rating": 3,
        "img": "https://media-service.carmax.com/img/vehicles/21165700/1_cleaned.jpg?width=800",
        "discription": "X3 XDrive30i",
        "brand": "BMW",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 5,
        "name": "2011 Chevrolet",
        "price": 22.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22378094/1_cleaned.jpg?width=800",
        "discription": "Silverado 1500 LT",
        "brand": "Chevrolet",
       "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 6,
        "name": "2020 Honda",
        "price": 24.998,
        "rating": 3,
        "img": "https://media-service.carmax.com/img/vehicles/22038571/1_cleaned.jpg?width=800",
        "discription": "HR-V LX",
        "brand": "Honda",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 7,
        "name": "2018 Mercedes-Benz",
        "price": 56.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22141737/1_cleaned.jpg?width=800",
        "discription": "GLA250",
        "brand": "Mercedes-Benz",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 8,
        "name": "2017 Audi",
        "price": 31.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/21192273/1_cleaned.jpg?width=800",
        "brand": "Audi",
        "discription": "Q5 Premium Plus",
        "case": "NEW",
        "available": true,
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 9,
        "name": "2019 BMW",
        "price": 31.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/21665051/1_cleaned.jpg?width=800",
        "discription": "X1 SDrive28i",
        "brand": "BMW",
        "case": "NEW",
        "available": true,
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 5,
        "name": "2011 Chevrolet",
        "price": 22.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22378094/1_cleaned.jpg?width=800",
        "discription": "Silverado 1500 LT",
        "brand": "Chevrolet",
       "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 6,
        "name": "2020 Honda",
        "price": 24.998,
        "rating": 3,
        "img": "https://media-service.carmax.com/img/vehicles/22038571/1_cleaned.jpg?width=800",
        "discription": "HR-V LX",
        "brand": "Honda",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 7,
        "name": "2018 Mercedes-Benz",
        "price": 56.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22141737/1_cleaned.jpg?width=800",
        "discription": "GLA250",
        "brand": "Mercedes-Benz",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 8,
        "name": "2017 Audi",
        "price": 31.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/21192273/1_cleaned.jpg?width=800",
        "brand": "Audi",
        "discription": "Q5 Premium Plus",
        "case": "NEW",
        "available": true,
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 9,
        "name": "2019 BMW",
        "price": 31.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/21665051/1_cleaned.jpg?width=800",
        "discription": "X1 SDrive28i",
        "brand": "BMW",
        "case": "NEW",
        "available": true,
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 15,
        "name": "2016 Lincoln",
        "price": 29.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/21358104/1_cleaned.jpg?width=800",
        "discription": "MKZ",
        "brand": "MKZ",
       "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 16,
        "name": "2018 Audi",
        "price": 54.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/22154253/1_cleaned.jpg?width=800",
        "discription": "S4 Premium Plus",
        "brand": "Audi",
       "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 1,
        "name": "JEEP 2019",
        "price": 15.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/22607892/1_cleaned.jpg?width=800",
        "discription": "Fusion SE",
        "brand": "Chevrolet",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 2,
        "name": "2017 Chevrolet",
        "price": 37.998,
        "rating": 5,
        "img": "https://media-service.carmax.com/img/vehicles/22378856/1_cleaned.jpg?width=800",
        "discription": "Camaro SS",
        "brand": "Chevrolet",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 3,
        "name": "2015 Ford",
        "price": 21.998,
        "rating": 4,
        "img": "https://media-service.carmax.com/img/vehicles/21627904/1_cleaned.jpg?width=800",
        "discription": "Explorer Limited",
        "brand": "ford",
        "available": true,
        "case": "USED",
        "colors": ["red", "purple", "green"]
    },
    {
        "id": 4,
        "name": "2019 BMW",
        "price": 38.998,
        "rating": 3,
        "img": "https://media-service.carmax.com/img/vehicles/21165700/1_cleaned.jpg?width=800",
        "discription": "X3 XDrive30i",
        "brand": "BMW",
        "available": true,
        "case": "NEW",
        "colors": ["red", "purple", "green"]
    },
];


let perPage = 8;
let currentPage = 1;
let start = 0;
let end = perPage;
let totalPages = Math.ceil(product.length / perPage);


function getCurrentPage(currentPage) {
    start = (currentPage - 1) * perPage;
    end = currentPage * perPage;
}


function renderProduct() {
    let html = '';
    let content = product.map((item, index) => {
         if (index >= start && index < end) {
            html += '<div class="cars-list data-category="">';
            html += '<a href="jeep.html">';
            html += '<div class="images-car">';
            html += '<img src=' + item.img + '>';
            html += '</div>';
            html += '</a>';
            html += '<div class="car-tile-content">';
            html += '<h3>';
            html += '<a href="jeep.html">';
            html += '<span class="year-make">'+ item.name  +'</span>';
            html += '<span class="model">' + item.discription +'</span>';
            html += '</a>';
            html += '</h3>';
            html += '<p class="info">';
            html += '<span class="price">' + '$' +item.price + '*' + '</span>';
            html += '<span class="bullet"> • </span>';
            html += '<span class="miles">' + item.case + '</span>';
            html += '</p>';
            html += '<hr>';
            html += '<span class="transfer">⁠Available at your store TopCars 6 Octoper, Egypt</span>'
            html += '</div>';
            html += '<div class="btns">';
            html += '<button class="first">' + 'Wishlist' + '</button>';
            html += '<button class="secound">' + 'Reservation' + '</button>';
            html += '</div>';
            html += '</div>';
            return html;
         }
        // console.log(html);
   });
   document.getElementById('product-list').innerHTML = html;
}
renderProduct();


function changePage() {
    const currentPages = document.querySelectorAll('.number-page li');
    // console.log(currentPage)
    for (let i = 0; i < currentPages.length; i++) {
        currentPages[i].addEventListener('click', () => {
            let value = i + 1;
            // console.log(value);
            currentPage = value;
            $('.number-page li').removeClass('active');
            currentPages[i].classList.add('active')
            getCurrentPage(currentPage);
            renderProduct();
        })
    }
}
changePage()



// pagination
let btnNext = document.querySelector('.btn-next');
let btnPrev = document.querySelector('.btn-prev');

btnNext.addEventListener('click', () => {
    currentPage++;

    if (currentPage > totalPages) {
        currentPage = totalPages;
    }
    if (currentPage == totalPages) {
        $('.btn-next').addClass('btn-active');
    } else {
        $('.btn-next').removeClass('btn-active');
    }
    console.log(currentPage);
    const btnPrev = document.querySelector('.btn-prev');
    btnPrev.classList.remove('btn-active');
    $('.number-page li').removeClass('active');
    $(`.number-page li:eq(${currentPage - 1})`).addClass('active');
    getCurrentPage(currentPage);
    renderProduct();
})

btnPrev.addEventListener('click', () => {
    currentPage--;

    if (currentPage < 1) {
        currentPage = 1;
    }
    if (currentPage == 1) {
        $('.btn-prev').addClass('btn-active');
    } else {
        $('.btn-prev').removeClass('btn-active');
    }
    const btnNext = document.querySelector('.btn-next');
    btnNext.classList.remove('btn-active');
    $('.number-page li').removeClass('active');
    $(`.number-page li:eq(${currentPage - 1})`).addClass('active');
    getCurrentPage(currentPage);
    renderProduct();
})
