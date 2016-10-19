$(document).ready(function() {


    $('#id_organization').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/subsidiary/"+_this+"/organization/"
        }).done(function(data) {
            $('#id_subsidiary').html("");
            $.each(data,function(index, itemData){
               $('#id_subsidiary').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.subsidiary_name
                    })
               );
            });

        })
    })

});