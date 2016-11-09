$(document).ready(function() {
    const work_assignment_table = $("#work_assignment_table");


    $('#id_vehicle').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/vehicle/"+_this
        }).done(function(data) {
             $('#id_frm_brand').val("");
             $('#id_frm_model').val("");
             $('#id_frm_serie').val("");
             $('#id_frm_motor').val("");
             $('#id_frm_vin').val("");
            if (data != null){
                 $('#id_frm_brand').val(data.brand.name);
                 $('#id_frm_model').val(data.model.name);
                 $('#id_frm_serie').val(data.number_serie);
                 $('#id_frm_motor').val(data.number_motor);
                 $('#id_frm_vin').val(data.number_vin);
            }

        })
    });


    work_assignment_table.on("change", ".cate_labour", function(){
        var _this = $(this).val();
        var _name = $(this).attr("name").split("-", 2);
        var _field = "id_"+_name[0]+"-"+_name[1]+"-"+"labour";

        $.ajax({
            type: "GET",
            url: "/api/labour/"+_this+"/labour"
        }).done(function(data) {
            work_assignment_table.find('#'+_field).html("");
            $.each(data,function(index, itemData){
                work_assignment_table.find('#'+_field).append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
                );
            });


        })
    });


});
