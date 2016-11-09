$(document).ready(function() {
     var _table = $('#id_table_qt_maintenance');
     var _igv_tax = parseFloat($('#id_frm_igv_tax').val());


    $('#id_frm_product_category').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/product/"+_this+"/category"
        }).done(function(data) {
            $('#id_frm_product').html("");
            $.each(data,function(index, itemData){
               $('#id_frm_product').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });
        })
    });

    $('#id_frm_handwork_category').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/handwork/"+_this+"/category"
        }).done(function(data) {
            $('#id_frm_handwork').html("");
            $.each(data,function(index, itemData){
               $('#id_frm_handwork').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });
        })
    });

    $("#add_product").on("click", function(){
        var category = $('#id_frm_product_category').val();
        var product = $('#id_frm_product').val();

        if(category == ""){
            swal("Campos Vacio!", "Seleccione Categoria", "error");
            $('#id_frm_product_category').focus();
            return false;
        }
        if(product == ""){
            swal("Campos Vacio!", "Seleccione Product", "error");
            $('#id_frm_product').focus();
            return false;
        }
        add_items('product')
    });

    $("#add_handwork").on("click", function(){
        var category = $('#id_frm_handwork_category').val();
        var handwork = $('#id_frm_handwork').val();

        if(category == ""){
            swal("Campos Vacio!", "Seleccione Categoria", "error");
            $('#id_frm_handwork_category').focus();
            return false;
        }
        if(handwork == ""){
            swal("Campos Vacio!", "Seleccione Mano de Obra", "error");
            $('#id_frm_handwork').focus();
            return false;
        }
        add_items('handwork')
    });



    function add_items(type) {
        var default_quantity = 1;
        var _find_tr, _quantity,_importe, t_quantity,t_import, html;
        if (type=='product'){

            var _product = $('#id_frm_product').val();
            $.ajax({
            type: "GET",
            url: "/api/product/"+_product
            }).done(function(data) {
                _find_tr = _table.find('tbody#tbody_maintenance_product_row tr#tr_row_'+data.id).length;
                if (_find_tr >= 1){
                     _quantity = $('#tr_row_'+data.id).find('.touchspin-step');
                    _importe = $('#tr_row_'+data.id).find('#select_importe_'+data.id);

                    t_quantity = parseInt(_quantity.val()) + default_quantity;
                    _quantity.val(t_quantity);
                    t_import = parseFloat(t_quantity) * parseFloat(data.sale_price);
                    _importe.val(t_import.toFixed(2))
                }else{
                     html = "<tr id='tr_row_"+data.id+"'>" +
                            "<td><input type='text' id='select_name_"+data.id+"' name='select_name_"+data.id+"' class='form-control' value='"+data.name+"' readonly /></td>" +
                            "<td><input id='select_quantity_"+data.id+"' name='select_quantity_"+data.id+"' type='text' value='"+default_quantity+"' class='touchspin-step cls_quantity'></td>" +
                            "<td><input type='text' id='select_price_"+data.id+"' name='select_price_"+data.id+"' class='form-control cls_price' value='"+data.sale_price+"' readonly></td>" +
                            "<td><input type='text' id='select_importe_"+data.id+"' name='select_importe_"+data.id+"'  class='form-control cls_importe' value='"+data.sale_price+"' readonly></td>" +
                            "<td><button type='button' class='btn btn-danger remove_tr_row'><i class='icon-cross3'></i></button></td>" +
                            "</tr>";
                    _table.find('#tbody_maintenance_product_row').append(html);
                }
                $(".touchspin-step").TouchSpin({min: 1,max: 100, step: 1});
                load_balance()
            });
        }
        if (type=='handwork'){
            var _handwork = $('#id_frm_handwork').val();
            $.ajax({
            type: "GET",
            url: "/api/handwork/"+_handwork
            }).done(function(data) {
                _find_tr = _table.find('#tbody_maintenance_handwork_row tr#tr_row_'+data.id).length;
                if (_find_tr >= 1){
                    _quantity = $('#tr_row_'+data.id).find('.touchspin-step');
                    _importe = $('#tr_row_'+data.id).find('#select_importe_'+data.id);

                    t_quantity = parseInt(_quantity.val()) + default_quantity;
                    _quantity.val(t_quantity);
                    t_import = parseFloat(t_quantity) * parseFloat(data.price);
                    _importe.val(t_import.toFixed(2))

                }else{
                     html = "<tr id='tr_row_"+data.id+"'>" +
                            "<td><input type='text' id='select_name_"+data.id+"' name='select_name_"+data.id+"' class='form-control' value='"+data.name+"' readonly /></td>" +
                            "<td><input id='select_quantity_"+data.id+"' name='select_quantity_"+data.id+"' type='text' value='"+default_quantity+"' class='touchspin-step cls_quantity'></td>" +
                            "<td><input type='text' id='select_price_"+data.id+"' name='select_price_"+data.id+"' class='form-control cls_price' value='"+data.price+"' readonly></td>" +
                            "<td><input type='text' id='select_importe_"+data.id+"' name='select_importe_"+data.id+"'  class='form-control cls_importe' value='"+data.price+"' readonly></td>" +
                            "<td><button type='button' class='btn btn-danger remove_tr_row'><i class='icon-cancel-circle2'></i></button></td>" +
                            "</tr>";
                    _table.find('#tbody_maintenance_handwork_row').append(html);
                }
                $(".touchspin-step").TouchSpin({min: 1,max: 100, step: 1});
                load_balance()
            });
        }

    }

    _table.on('click', '.remove_tr_row', function (e) {
        e.preventDefault();
        var _this = $(this);
        _this.parent().parent().remove();
        load_balance()
    });

    function load_balance(){
        var amount = parseFloat(0);
         _table.find('tbody tr > td:nth-child(4)').each(function (index) {
            amount += parseFloat($(this).find('input').val());
        });
        var new_amount = amount.toFixed(2);
        var igv_amount = parseFloat(new_amount * _igv_tax).toFixed(2);
        var new_total = parseFloat(new_amount) + parseFloat(igv_amount);
        $('#id_sub_total').val(new_amount);
        $('#id_igv_total').val(igv_amount);
        $('#id_total_paid').val(new_total.toFixed(2));

    }

    _table.on('click', '.bootstrap-touchspin-down, .bootstrap-touchspin-up', function(event) {
        var _this = $(this);
        const id_tr = _this.parent().parent().parent().parent().attr("id");
        const quantity = $("#"+id_tr).find('.cls_quantity').val();
        const price = $("#"+id_tr).find('.cls_price').val();
        const importe = $("#"+id_tr).find('.cls_importe');
        if (quantity  == "0" || quantity == ""){
           $("#"+id_tr).find('.cls_quantity').val('1');
        }else{
            const new_import = parseFloat(quantity) * parseFloat(price);
            importe.val(new_import.toFixed(2))
        }
        load_balance()
    });




    $('#submit_form').on("click", function(e){
        var client = $('#id_client').val();
        var vehicle = $('#id_vehicle').val();

        if(client == ""){
            swal("Campos Vacio!", "Seleccione Cliente", "error");
            return false;
        }
        if(vehicle == ""){
            swal("Campos Vacio!", "Seleccione Vehiculo", "error");
            return false;
        }

        var tbody = _table.find("tbody tr").length;
        if(tbody<1){
            swal("Productos no Asignados!", "No se ha agregado ningun producto.", "error");
            return false;
        }else{
            swal({
                title: "Estas tu seguro?",
                text: "Deseas enviar en formulario de Cotizacion",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#2196F3",
                confirmButtonText: "Yes, Enviar",
                cancelButtonText: "No, Cancelar",
                closeOnConfirm: false
            }, function(){
                var form_quotation = $('#Quotation_Maintenance_form');
                var form_detail = quotation_detail();
                var parameter = {
                    'form': get_FormDataserialize(form_quotation),
                    'form_detail': form_detail
                };

                $.ajax({
                    type: "POST",
                    url: "../../../quotation/quotation_maintenance/new/",
                    data: JSON.stringify(parameter)
                }).done(function(data) {
                      window.location.reload(true);

                })

            });
        }
    });


    var quotation_detail = function () {
        var result_list = [];
        _table.find('tbody#tbody_maintenance_product_row tr').each(function() {
            var _description = $(this).find("td").eq(0).find('input').val();
            var _quantity = $(this).find("td").eq(1).find('input').val();
            var _price = $(this).find("td").eq(2).find('input').val();
            var _import = $(this).find("td").eq(3).find('input').val();
            var result_dict = {};
            result_dict.description = _description;
            result_dict.quantity = parseInt(_quantity);
            result_dict.price = parseFloat(_price);
            result_dict.importe = parseFloat(_import);
            result_list.push(result_dict)
        });
        _table.find('tbody#tbody_maintenance_handwork_row tr').each(function() {
            var _description = $(this).find("td").eq(0).find('input').val();
            var _quantity = $(this).find("td").eq(1).find('input').val();
            var _price = $(this).find("td").eq(2).find('input').val();
            var _import = $(this).find("td").eq(3).find('input').val();
            var result_dict = {};
            result_dict.description = _description;
            result_dict.quantity = parseInt(_quantity);
            result_dict.price = parseFloat(_price);
            result_dict.importe = parseFloat(_import);
            result_list.push(result_dict)
        });
        return result_list;
    };


    //
    //
    // function printDiv(divName) {
    //      var printContents = document.getElementById(divName).innerHTML;
    //      var originalContents = document.body.innerHTML;
    //      document.body.innerHTML = printContents;
    //      window.print();
    //      document.body.innerHTML = originalContents;
    // }
    //
    //
    //  $("#btnPrint").on('click', function (e) {
    //     e.preventDefault();
    //     printDiv('print_qt')
    // });

});