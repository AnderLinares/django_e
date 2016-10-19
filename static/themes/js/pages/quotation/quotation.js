$(document).ready(function() {
     var _tbody = $('#tbody_quotation_row');

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
                    })
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
                   $('<option>', {
                       value: itemData.id,
                       text : itemData.name
                    })
               );
            });
        })
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
        var _find_tr, _quantity, t_quantity, html;
        if (type=='supplier_product'){
            var supplier_product = $('#id_product_supplier option:selected');
            _find_tr = _tbody.find('#tr_row_'+supplier_product.val()).length;
            if (_find_tr >= 1){
                _quantity = $('#tr_row_'+supplier_product.val()).find('.touchspin-step');
                t_quantity = parseInt(_quantity.val()) + default_quantity;
                _quantity.val(t_quantity);
            }else{
                 html = "<tr id='tr_row_"+supplier_product.val()+"'>" +
                        "<td><select id='select_name_"+supplier_product.val()+"' name='select_name_"+supplier_product.val()+"' class='form-control'><option value='"+supplier_product.val()+"'>"+supplier_product.text()+"</option></select></td>" +
                        "<td><input id='select_quantity_"+supplier_product.val()+"' name='select_quantity_"+supplier_product.val()+"' type='text' value='"+default_quantity+"' class='touchspin-step'></td>" +
                        "<td><button type='button' class='btn btn-danger remove_tr_row'>remove</button></td>" +
                        "</tr>";
                _tbody.append(html);
            }

        }
        if (type=='supplier_product_category'){
            var category = $('#id_category option:selected');
            var product = $('#id_product option:selected');
            var product_name = category.text()+" / "+product.text();

            _find_tr = _tbody.find('#tr_row_'+product.val()).length;
            if (_find_tr >= 1){
                _quantity = $('#tr_row_'+product.val()).find('.touchspin-step');
                t_quantity = parseInt(_quantity.val()) + default_quantity;
                _quantity.val(t_quantity);
            }else{
                html = "<tr id='tr_row_"+product.val()+"'>" +
                       "<td><select id='select_name_"+product.val()+"' name='select_name_"+product.val()+"' class='form-control'><option value='"+product.val()+"'>"+product_name+"</option></select></td>" +
                       "<td><input  id='select_quantity_"+product.val()+"' name='select_quantity_"+product.val()+"' type='text' value='"+default_quantity+"' class='touchspin-step'></td>" +
                       "<td><button type='button' class='btn btn-danger remove_tr_row'>remove</button></td>" +
                       "</tr>";
                _tbody.append(html);
            }
        }

        $(".touchspin-step").TouchSpin({min: 1,max: 100, step: 1});

    }


    _tbody.on('click', '.remove_tr_row', function (e) {
        e.preventDefault();
        var _this = $(this);
        _this.parent().parent().remove();
    });

    $('#submit_form').on("click", function(e){
        var tbody = _tbody.find("tr").length;
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
                var form_quotation = $('#Quotation_Store_form');
                var form_detail = quotation_detail();
                var parameter = {
                    'form': get_FormDataserialize(form_quotation),
                    'form_detail': form_detail
                };

                $.ajax({
                    type: "POST",
                    url: "../../../quotation/quotation_store/new/",
                    data: JSON.stringify(parameter)
                }).done(function(data) {
                      window.location.reload(true);

                })

            });
        }
    });



    var quotation_detail = function () {
        var result_list = [];
        $('#tbody_quotation_row tr').each(function() {
            var product = $(this).find("td").eq(0).find('select').val();
            var quantity = $(this).find("td").eq(1).find('input').val();
            var result_dict = {};
            result_dict.product = product;
            result_dict.quantity = parseInt(quantity);
            result_list.push(result_dict)
        });
        return result_list;
    };


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