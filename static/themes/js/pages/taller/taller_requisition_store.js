$(document).ready(function() {
    const requisition_store_table = $("#requisition_store_table");

    requisition_store_table.on("change", ".cls_category", function(){
        var _this = $(this).val();
        var _name = $(this).attr("name").split("-", 2);
        var _field = "id_"+_name[0]+"-"+_name[1]+"-"+"product";

        $.ajax({
            type: "GET",
            url: "/api/product/"+_this+"/category"
        }).done(function(data) {
            requisition_store_table.find('#'+_field).html("");
            $.each(data,function(index, itemData){
                requisition_store_table.find('#'+_field).append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
                );
            });
        })
    });





});
