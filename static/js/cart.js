$(document).ready(function(){
    $(".add_to_cart").on("click", function(e){
        console.log("got in add to cart ajax")
        e.preventDefault();
        var productId = this.dataset.id
        var action = this.dataset.action

        $.ajax({
            url:"/added_item/",
            dataType: 'json',
            data: {
                "id": productId,
                "action": action,
            },
            success: function(){
                alert("Product added to cart");
            },
        })
    })
});

