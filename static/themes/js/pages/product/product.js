$(document).ready(function() {


    $('#id_product_category').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/subcategory/"+_this+"/category/"
        }).done(function(data) {
            $('#id_product_subcategory').html("");
            $.each(data,function(index, itemData){
               $('#id_product_subcategory').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });

        })
    })

    $('#id_brand').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/product-model/"+_this+"/brand/"
        }).done(function(data) {
            $('#id_model').html("");
            if (data[0] == null){
                $('#id_model').append(
                    $('<option>', {value: "", text : "---------"})
                );
            }
            $.each(data,function(index, itemData){
               $('#id_model').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });

        })
    });


});