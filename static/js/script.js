function include(url) {
    document.write('<script src="' + url + '"></script>');
    return false;
}

/* cookie.JS
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/jquery.cookie.js');


/* DEVICE.JS
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/device.min.js');

/* Easing library
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/jquery.easing.1.3.js');


/* ToTop
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/jquery.ui.totop.js');
$(function () {
    $().UItoTop({ easingType: 'easeOutQuart' });
});


/* DEVICE.JS AND SMOOTH SCROLLIG
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/jquery.mousewheel.min.js');
// include('js/jquery.simplr.smoothscroll.min.js');
// $(function () {
//     if ($('html').hasClass('desktop')) {
//         $.srSmoothscroll({
//             step: 25,
//             speed: 400
//         });
//     }
// });

/* videoBG
 ========================================================*/
// include('js/video/jquery.videoBG.js');
// $(function () {
//     if ($('html').hasClass('desktop')) {
//         $('.only-video').videoBG({
//             mp4: 'video/header.mp4',
//             webm: 'video/header.webm',
//             poster: 'video/header.jpg',
//             scale: true,
//             zIndex: 0
//         });
//     }
// });

/* Copyright Year
 ========================================================*/
var currentYear = (new Date).getFullYear();
$(document).ready(function () {
    $("#copyright-year").text((new Date).getFullYear());
});


/* Superfish menu
 ========================================================*/
include('https://td-pilomaterial.ru/assets/js/superfish.js');


/* Orientation tablet fix
 ========================================================*/
$(function () {
// IPad/IPhone
    var viewportmeta = document.querySelector && document.querySelector('meta[name="viewport"]'),
        ua = navigator.userAgent,

        gestureStart = function () {
            viewportmeta.content = "width=device-width, minimum-scale=0.25, maximum-scale=1.6, initial-scale=1.0";
        },

        scaleFix = function () {
            if (viewportmeta && /iPhone|iPad/.test(ua) && !/Opera Mini/.test(ua)) {
                viewportmeta.content = "width=device-width, minimum-scale=1.0, maximum-scale=1.0";
                document.addEventListener("gesturestart", gestureStart, false);
            }
        };

    scaleFix();
    // Menu Android
    if (window.orientation != undefined) {
        var regM = /ipod|ipad|iphone/gi,
            result = ua.match(regM)
        if (!result) {
            $('.sf-menu li').each(function () {
                if ($(">ul", this)[0]) {
                    $(">a", this).toggle(
                        function () {
                            return false;
                        },
                        function () {
                            window.location.href = $(this).attr("href");
                        }
                    );
                }
            })
        }
    }
});
var ua = navigator.userAgent.toLocaleLowerCase(),
    regV = /ipod|ipad|iphone/gi,
    result = ua.match(regV),
    userScale = "";
if (!result) {
    userScale = ",user-scalable=0"
}
document.write('<meta name="viewport" content="width=device-width,initial-scale=1.0' + userScale + '">');

$(document).ready(function () {
    var navBtn = $('#navBtn');
    var nav = $('#nav');

    $(".animlogo").animated("flipInX", "flipOutX");
    $(".y, .yy, .yyy").animated("fadeIn", "fadeOut");
    // $(".r").animated("fadeInRight", "fadeOutRight");
    // $(".l").animated("fadeInLeft", "fadeOutLeft");
    // $(".d").animated("fadeInUp", "fadeOutUp");

    $(".r").animated("fadeInRight", "");
    $(".l, .bl").animated("fadeInLeft", "");
    $(".d").animated("fadeInUp", "");
	$(".d0").animated("fadeInUp", "");
    $(".i1, .i2, .i3, .i4").animated("fadeIn", "");

   $("a.fb").fancybox({
                'transitionIn'  : 'elastic',
                'transitionOut' : 'elastic',
                'speedIn'   : 260,
                'speedOut'    : 200,
                'overlayShow' : false

            });

    $(document).click(function (e) {
        if (navBtn.hasClass('active')) {
            var target = e.clientX;
            if (target > (nav.width())) {
                navBtn.removeClass('active');
                nav.removeClass('active');
                return false;
            }
        }
    });


    navBtn.click(function () {
        if (navBtn.hasClass('active')) {
            navBtn.removeClass('active');
            nav.removeClass('active');
        } else {
            navBtn.addClass('active');
            nav.addClass('active');
        }
        return false;
    });


    $(function () {
        // init Isotope
        var $container = $('.isotope').isotope({
            itemSelector: '.element-item',
            layoutMode: 'fitRows'
        });
        setTimeout(function(){
            $('.isotope').isotope('layout');
        },200);
        $('.button').click(function () {
            var fin = $('#filters').find('.active');
            fin.removeClass('active');
            $(this).addClass('active');
            var filterValue = $(this).attr('data-filter');
            $container.isotope({ filter: filterValue });
            return false;
        });
    });

    if ($('#tabs').length > 0) {
        $('#tabs').easyResponsiveTabs();
    }

    if ($('#owl1').length > 0) {
        var owl = $("#owl1");
        owl.owlCarousel({
            items: 2,
            itemsDesktop: [1199, 1],
            itemsDesktopSmall: [979, 1],
            itemsTablet: [767, 1],
            singleItem: false,
            paginationSpeed: 800,
            pagination: true,
            navigation: false,
            autoPlay: 6000
        });
    }
});

$(window).load(function(){
    $('.isotope').isotope('layout');
});
