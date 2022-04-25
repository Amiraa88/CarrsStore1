        let menu = document.querySelector('#menu-btn');
            let navbar = document.querySelector('.navbar');

            menu.onclick = () => {
                menu.classList.toggle('fa-times');
                navbar.classList.toggle('active')
            }

            document.querySelector('#search').onclick = () => {
                document.querySelector('.search-container').classList.toggle('active');
            }

            document.querySelector('#close-search').onclick = () => {
                document.querySelector('.search-container').classList.remove('active');
            }

            window.onscroll = () => {
                if (window.scrollY > 0) {
                    document.querySelector('.header').classList.add('active');
                } else {
                    document.querySelector('.header').classList.remove('active');
                }


                menu.classList.remove('fa-times');
                navbar.classList.remove('active')
            }

            window.onload = () => {
                if (window.scrollY > 0) {
                    document.querySelector('.header').classList.add('active');
                } else {
                    document.querySelector('.header').classList.remove('active');
                }
            }

            
            // scroll top
            let span = document.querySelector(".top");

            window.onscroll = function () {
                console.log(window.scrollY);
                if (window.scrollY >= 100) {
                    span.style.display = "block";
                } else {
                    span.style.display = "none";
                }
                //  this.scrollY >= 1000 ? span.classList.add("show") : span.classList.remove("show");
            };

            span.onclick = function () {
                window.scrollTo({
                    top: 0,
                    behavior: "smooth",
                });
            };

        let thumbnails = document.getElementsByClassName('thumbnail')

        let activeImages = document.getElementsByClassName('active')

        for (var i = 0; i < thumbnails.length; i++) {

            thumbnails[i].addEventListener('mouseover', function () {
                console.log(activeImages)

                if (activeImages.length > 0) {
                    activeImages[0].classList.remove('active')
                }


                this.classList.add('active')
                document.getElementById('featured').src = this.src
            })
        }


        let buttonRight = document.getElementById('slideRight');
        let buttonLeft = document.getElementById('slideLeft');

        buttonLeft.addEventListener('click', function () {
            document.getElementById('slider').scrollLeft -= 180
        })

        buttonRight.addEventListener('click', function () {
            document.getElementById('slider').scrollLeft += 180
        })


        
//comments
var addBtn = document.querySelector(".add-btn");
var textarea = document.getElementById("comment-content");
 var list = document.querySelector(".comment-list");

addBtn.addEventListener("click", function() {
  var li = document.createElement("li");
  list.appendChild(li);
  li.classList.add("comment");
  li.innerHTML = '<div class="comment-content"><img src="image/pic-2.png" width="40" alt="user avatar"><div class="user"><strong>user name</strong><span>1 days ago</span></div><p>' + textarea.value + '</p></div>'
  
}, false);
