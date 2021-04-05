$(document).ready(function(){
    $(".add_remove").on("click", function(){
        var productId = this.dataset.id
        var action = this.dataset.action
        console.log(productId, action)

        $.ajax({
            url:"/added_item/",
            dataType: 'json',
            data: {
                "id": productId,
                "action": action,
            },
            success: function(){
                console.log("Buttons working")
                location.reload();
            },
        });
    });
});

