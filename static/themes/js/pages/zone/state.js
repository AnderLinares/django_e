$(document).ready(function() {


    $('#id_zone').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/country/"+_this+"/zone/"
        }).done(function(data) {
            $('#id_country').html("");
            $.each(data,function(index, itemData){
               $('#id_country').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });

        })
    })

});