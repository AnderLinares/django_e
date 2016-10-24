$(document).ready(function() {
     var _tbody = $('#tbody_po_store_row');
     var _igv = parseFloat($('#id_igv_tax').val());

    $('#id_supplier').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/supplier-product/"+_this+"/supplier/"
        }).done(function(data) {
            $('#id_product_supplier').html("");
            $('#id_product_supplier').append(
               $('<option>', {value: '', text : '---------'})
            );
            $.each(data[0].product,function(index, itemData){
               $('#id_product_supplier').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.product_category.name +" / "+ itemData.name
                    }).attr("data-price",itemData.purchase_price)
               );
            });

        })
    });

    $('#id_category').on("change", function(){
        var _this = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/subcategory/"+_this+"/category/"
        }).done(function(data) {
            $('#id_sub_category').html("");
            $('#id_sub_category').append(
               $('<option>', {value: '', text : '---------'})
            );
            $.each(data,function(index, itemData){
               $('#id_sub_category').append(
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });
        })
    });
    $('#id_sub_category').on("change", function(){
        var category = $("#id_category").val();
        var subcategory = $(this).val();
        $.ajax({
            type: "GET",
            url: "/api/product/"+category+"/"+subcategory+"/"
        }).done(function(data) {
            $('#id_product').html("");
            $('#id_product').append(
               $('<option>', {value: '', text : '---------'})
            );
            $.each(data,function(index, itemData){
               $('#id_product').append(
                   $("<option>", {
                       value: itemData.id,
                       text : itemData.name
                    }).attr("data-price",itemData.purchase_price)
               );
            });
        })
    });

    _tbody.on("focusout",".cls_discount", function(){
        const id_tr = $(this).parent().parent().attr('id');
        const discount = $(this).val();
        const quantity = $("#"+id_tr).find('.cls_quantity').val();
        const price = $("#"+id_tr).find('.cls_price').val();
        const importe = $("#"+id_tr).find('.cls_import');
        const total = parseFloat(quantity) * parseFloat(price);
        if (discount  == "0" || discount == ""){
            importe.val(total.toFixed(2));
            $(this).val('0');
        }else{
            const new_import = (parseFloat(total) * parseFloat(discount)) / 100 ;
            importe.val(new_import.toFixed(2))
        }
        po_total()
    });

    $('#add_supplier_product').on("click", function(){
        var supplier = $('#id_supplier').val();
        var supplier_product = $('#id_product_supplier').val();

        if(supplier == ""){
            swal("Campos Vacio!", "Seleccione Proveedor", "error");
            return false;
        }
        if(supplier_product == ""){
            swal("Campos Vacio!", "Seleccione Product", "error");
            return false;
        }
        addproduct('supplier_product')
    });

     $('#add_supplier_product_category').on("click", function(){
        var category = $('#id_category').val();
        var sub_category = $('#id_sub_category').val();
        var product = $('#id_product').val();
        if(category == ""){
            swal("Campos Vacio!", "Seleccione Categoria", "error");
            return false;
        }
        if(sub_category == ""){
            swal("Campos Vacio!", "Seleccione Sub-Categoria", "error");
            return false;
        }
        if(product == ""){
            swal("Campos Vacio!", "Seleccione Product", "error");
            return false;
        }
        addproduct('supplier_product_category')
    });

    function addproduct(type) {
        var default_quantity = 1;
        var _find_tr, _quantity, t_quantity, t_import, html, _price, _import;
        if (type=='supplier_product'){
            var supplier_product = $('#id_product_supplier option:selected');
            var price = supplier_product.attr("data-price");
            var importe = parseFloat(price) * parseFloat(default_quantity);
            _find_tr = _tbody.find('#tr_row_'+supplier_product.val()).length;
            if (_find_tr >= 1){
                _quantity = $('#tr_row_'+supplier_product.val()).find('.cls_quantity');
                _price = $('#tr_row_'+supplier_product.val()).find('.cls_price');
                _import = $('#tr_row_'+supplier_product.val()).find('.cls_import');
                t_quantity = parseInt(_quantity.val()) + default_quantity;
                t_import = parseFloat(t_quantity) * parseFloat(_price.val());
                _quantity.val(t_quantity);
                _import.val(t_import.toFixed(2))
            }else{
                 html = "<tr id='tr_row_"+supplier_product.val()+"'>" +
                        "<td><select id='select_name_"+supplier_product.val()+"' name='select_name_"+supplier_product.val()+"' class='form-control'><option value='"+supplier_product.val()+"'>"+supplier_product.text()+"</option></select></td>" +
                        "<td><input id='select_quantity_"+supplier_product.val()+"' name='select_quantity_"+supplier_product.val()+"' type='text' value='"+default_quantity+"' class='touchspin-step cls_quantity'></td>" +
                        "<td><input id='select_price_"+supplier_product.val()+"' name='select_price_"+supplier_product.val()+"' type='text' value='"+price+"' class='form-control cls_price'></td>" +
                        "<td><input id='select_discount_"+supplier_product.val()+"' name='select_discount_"+supplier_product.val()+"' type='text' value='0' class='form-control cls_discount'></td>" +
                        "<td><input id='select_import_"+supplier_product.val()+"' name='select_import_"+supplier_product.val()+"' type='text' value='"+importe.toFixed(2)+"' class='form-control cls_import'></td>" +
                        "<td><button type='button' class='btn btn-danger remove_tr_row'><i class='icon-cancel-circle2'></i></button></td>" +
                        "</tr>";
                _tbody.append(html);
            }

        }
        if (type=='supplier_product_category'){
            var category = $('#id_category option:selected');
            var product = $('#id_product option:selected');
            var product_name = category.text()+" / "+product.text();
            var purchase_price = product.attr("data-price");

            _find_tr = _tbody.find('#tr_row_'+product.val()).length;
            if (_find_tr >= 1){
                _quantity = $('#tr_row_'+product.val()).find('.touchspin-step');
                t_quantity = parseInt(_quantity.val()) + default_quantity;
                _quantity.val(t_quantity);
            }else{
                html = "<tr id='tr_row_"+product.val()+"'>" +
                       "<td><select id='select_name_"+product.val()+"' name='select_name_"+product.val()+"' class='form-control'><option value='"+product.val()+"'>"+product_name+"</option></select></td>" +
                       "<td><input  id='select_quantity_"+product.val()+"' name='select_quantity_"+product.val()+"' type='text' value='"+default_quantity+"' class='touchspin-step'></td>" +
                       "<td><input id='select_price_"+product.val()+"' name='select_price_"+product.val()+"' type='text' value='"+purchase_price+"' class='form-control'></td>" +
                       "<td><input id='select_discount_"+product.val()+"' name='select_discount_"+product.val()+"' type='text' value='0' class='form-control'></td>" +
                       "<td><input id='select_import_"+product.val()+"' name='select_import_"+product.val()+"' type='text' value='"+purchase_price+"' class='form-control'></td>" +
                       "<td><button type='button' class='btn btn-danger remove_tr_row'><i class='icon-cancel-circle2'></i></button></td>" +
                       "</tr>";
                _tbody.append(html);
            }
        }
        $(".touchspin-step").TouchSpin({min: 1,max: 100, step: 1});
        po_total();
    }


    _tbody.on('click', '.remove_tr_row', function (e) {
        e.preventDefault();
        var _this = $(this);
        _this.parent().parent().remove();
        po_total()
    });


    var po_store_detail = function () {
        var result_list = [];
        $('#tbody_po_store_row tr').each(function() {
            var product = $(this).find("td").eq(0).find('select').val();
            var description = $(this).find("td").eq(0).find('select').text();
            var quantity = $(this).find("td").eq(1).find('input').val();
            var price = $(this).find("td").eq(2).find('input').val();
            var discount = $(this).find("td").eq(3).find('input').val();
            var importe = $(this).find("td").eq(4).find('input').val();
            var result_dict = {};
            result_dict.product = product;
            result_dict.description = description;
            result_dict.quantity = parseInt(quantity);
            result_dict.price = parseFloat(price);
            result_dict.discount = parseFloat(discount);
            result_dict.importe = parseFloat(importe);
            result_list.push(result_dict)
        });
        return result_list;
    };

    var po_total = function () {
        const quality =  po_store_detail();
        var importe = parseFloat(0);
        $.each(quality,function(index, itemData){
           importe += itemData.importe;
        });
        var igv_total = importe * _igv;
        var sub_total = importe - igv_total;
        var total = importe;
        var result = {};
        result.igv_tax = _igv;
        result.igv_total = igv_total;
        result.sub_total = sub_total;
        result.total = total;

        var _tbody_po_store_row = $("#tbody_po_store_row_total");
        _tbody_po_store_row.find('#id_igv_total').val(igv_total.toFixed(2));
        _tbody_po_store_row.find('#id_sub_total').val(sub_total.toFixed(2));
        _tbody_po_store_row.find('#id_total_paid').val(total.toFixed(2));
        return result
    };

    _tbody.on('click', '.bootstrap-touchspin-down', function(event) {
        var _this = $(this);
        touchspin_load(_this)
    });
    _tbody.on('click', '.bootstrap-touchspin-up', function(event) {
        var _this = $(this);
        touchspin_load(_this)
    });

    function touchspin_load(_this){
        const id_tr = _this.parent().parent().parent().parent().attr("id");
        const quantity = $("#"+id_tr).find('.cls_quantity').val();
        const price = $("#"+id_tr).find('.cls_price').val();
        const importe = $("#"+id_tr).find('.cls_import');
        if (quantity  == "0" || quantity == ""){
           $("#"+id_tr).find('.cls_quantity').val('1');
        }else{
            const new_import = parseFloat(quantity) * parseFloat(price);
            importe.val(new_import.toFixed(2))
        }
        $("#"+id_tr).find('.cls_discount').trigger('focus').blur();
        po_total()
    }



    $('#submit_form').on("click", function(e){
        var tbody = _tbody.find("tr").length;
        var currency = $('#id_currency').val();
        var purchase_condition = $('#id_purchase_condition').val();

        if(currency == ""){
            swal("Campos Vacio!", "Seleccione Moneda", "error");
            return false;
        }
        if(purchase_condition == ""){
            swal("Campos Vacio!", "Seleccione Condicion Compra", "error");
            return false;
        }

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
                var form_po = $('#Purchase_Order_form');
                var form_detail = po_store_detail();
                var parameter = {
                    'form': get_FormDataserialize(form_po),
                    'form_detail': form_detail
                };
                console.log(parameter);
                $.ajax({
                    type: "POST",
                    url: "../../../logistic/purchase-order/new/",
                    data: JSON.stringify(parameter)
                }).done(function(data) {
                      window.location.reload(true);
                })

            });
        }
    });



    function printDiv(divName) {
         var printContents = document.getElementById(divName).innerHTML;
         var originalContents = document.body.innerHTML;
         document.body.innerHTML = printContents;
         window.print();
         document.body.innerHTML = originalContents;
    }


     $("#btnPrint").on('click', function (e) {
        e.preventDefault();
        printDiv('print_qt')
    });

});