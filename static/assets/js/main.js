$(document).ready(function () {
  //  this for increment_vlaue of increment-btn
  $(".increcment-btn").click(function (e) {
    e.preventDefault();
    var increcment_vlaue = $(".product_data").find(".qty-input").val();
    var value = parseInt(increcment_vlaue, 10);
    vlue = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });

  //  this for decrement_vlaue of decrement-btn
  $(".decrement-btn").click(function (e) {
    e.preventDefault();
    var decrement_vlaue = $(".product_data").find(".qty-input").val();
    var value = parseInt(decrement_vlaue, 10);
    vlue = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });

  $(".addToCardBtn").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var product_qty = $(this).closest(".product_data").find(".qty-input").val();
    var products_name = $(this)
      .closest(".product_data")
      .find(".products-name")
      .val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/add-to-card",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        products_name: products_name,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response.status);
        // alertfy.success(response.status)
        alertify.success(response.status);
      },
    });
  });

  $(".ChangQuantity").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var product_qty = $(this).closest(".product_data").find(".qty-input").val();
    var products_name = $(this)
      .closest(".product_data")
      .find(".products-name")
      .val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/update-card",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        products_name: products_name,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response.status);
      },
    });
  });

  $(".delete-card-item").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/delete_card_item",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response.status);
        // alertfy.success(response.status)
        // // alertify.success(response.status)
        $(".carddata").load(location.href + " .carddata");
      },
    });
  });
  // ///////// ///////// ///////// ///////// ///////// /////////

  $(".addwishlist").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      method: "POST",
      url: "/add-to-wishlist",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        alertify.success(response.status);
      },
    });
  });

  $(".delete-wishlist-item").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    console.log(product_id);

    $.ajax({
      method: "POST",
      url: "/delete-to-wishlist",
      data: {
        product_id: product_id,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        alertify.success(response.status);
        $(".wishlistdata").load(location.href + " .wishlistdata");
      },
    });
  });

  // $('.owl-carousel').owlCarousel({
  //     loop: true,
  //     autoplay: true,
  //     autoplayTimeout: 5000,
  //     autoplayHoverPause: true,
  //     dots: false,
  //     stagePadding: -5,
  //     responsiveBaseElement: 'body',
  //     responsive: {
  //         0: {
  //             items: 1,
  //         },
  //         700: {
  //             items: 2,
  //         },
  //         1220: {
  //             items: 4,
  //         },
  //     },
  // });

  var owl = $(".owl-carousel");
  owl.owlCarousel({
    loop: true,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    // nav: true,
    margin: 4,
    responsive: {
      0: {
        items: 2,
      },
      600: {
        items: 3,
      },
      960: {
        items: 4,
      },
      1200: {
        items: 5,
      },
    },
  });
  owl.on("mousewheel", ".owl-stage", function (e) {
    if (e.deltaY > 0) {
      owl.trigger("next.owl");
    } else {
      owl.trigger("prev.owl");
    }
    e.preventDefault();
  });

  const carouselItems = $(".carousel-item");
  let currentIndex = 0;

  function toggleActiveClass() {
    carouselItems.eq(currentIndex).toggleClass("active");
    currentIndex = (currentIndex + 1) % 3;
    carouselItems.eq(currentIndex).toggleClass("active");
  }

  setInterval(toggleActiveClass, 6000);
});

$(document).ready(function () {
  const carouselItems = $(".carousel-item");
  const indicators = $(".carousel-indicators li");

  let currentIndex = 0;

  function toggleActiveClass() {
    carouselItems.eq(currentIndex).toggleClass("active");
    currentIndex = (currentIndex + 1) % carouselItems.length;
    carouselItems.eq(currentIndex).toggleClass("active");
    indicators.removeClass("active");
    indicators.eq(currentIndex).addClass("active");
  }

  setInterval(toggleActiveClass, 3000);

  indicators.click(function () {
    const targetIndex = $(this).data("slide-to");
    if (targetIndex !== currentIndex) {
      carouselItems.eq(currentIndex).toggleClass("active");
      currentIndex = targetIndex;
      carouselItems.eq(currentIndex).toggleClass("active");
      indicators.removeClass("active");
      indicators.eq(currentIndex).addClass("active");
    }
  });

  // $('.carousel-control-next').click(function () {
  //     carouselItems.eq(currentIndex).toggleClass('active');
  //     currentIndex = (currentIndex + 3) % carouselItems.length;
  //     carouselItems.eq(currentIndex).toggleClass('active');
  //     indicators.removeClass('active');
  //     indicators.eq(currentIndex).addClass('active');
  // });

  // $('.carousel-control-prev').click(function () {
  //     carouselItems.eq(currentIndex).toggleClass('active');
  //     currentIndex = (currentIndex - 3 + carouselItems.length) % carouselItems.length;
  //     carouselItems.eq(currentIndex).toggleClass('active');
  //     indicators.removeClass('active');
  //     indicators.eq(currentIndex).addClass('active');
  // });
});
