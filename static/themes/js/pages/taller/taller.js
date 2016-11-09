$(window).on("load", function() {
    const  vehicle = $('#id_vehicle').val();
    if (vehicle !=""){
        $.ajax({
            type: "GET",
            url: "/api/vehicle/"+vehicle
        }).done(function(data) {
             $('#id_frm_brand').val("");
             $('#id_frm_model').val("");
             $('#id_frm_color').val("");
            if (data != null){
                 $('#id_frm_brand').val(data.brand.name);
                 $('#id_frm_model').val(data.model.name);
                 $(".colorpicker-disabled").spectrum({color:data.color, disabled: true});
            }

        })

    }
});
$(document).ready(function() {

    $('#id_vehicle').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/vehicle/"+_this
        }).done(function(data) {
             $('#id_frm_brand').val("");
             $('#id_frm_model').val("");
             $('#id_frm_color').val("");
            if (data != null){
                 $('#id_frm_brand').val(data.brand.name);
                 $('#id_frm_model').val(data.model.name);
                 $(".colorpicker-disabled").spectrum({color:data.color, disabled: true});
            }

        })
    });

    $('#id_type_solicitude_entry, #id_type_solicitude_exit').on("change", function(e){
        e.preventDefault()
        const _this = $(this).val();
        const _this_text = $('option:selected',this).text();
        const _title_act_delivery = $('#title_act_delivery');

        if (_this == ""){
            _title_act_delivery.html('');
        }else if (_this == "ENTRY"){
           _title_act_delivery.html(_this_text.toUpperCase());
        }else if (_this == "EXIT"){
           _title_act_delivery.html(_this_text.toUpperCase());
        }

    });
});
