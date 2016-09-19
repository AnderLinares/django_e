$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_quotation = $('#add_quotation');
    var modal_quotation = $('#modal_quotation');
    var form_quotation;

    div_page_wrapper.on('click', "#add_quotation", function(e) {
        e.preventDefault();
        add_quotation.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_QUOTATION_ADD
        }).done(function(data) {
             modal_quotation.html(data);
             modal_quotation.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_quotation.attr("disabled",false);
        });
    });

    //  div_page_wrapper.on('change', "#id_quotation_exchange_rate", function(e) {
    //     e.preventDefault();
    //     var _this = $(this).val();
    //     if (_this == ""){
    //         var rate = parseFloat(1).toFixed(2);
    //         $("#id_rate").val(rate);
    //     }else{
    //         $.get("/api/exchange-rate/"+_this+"/", function(data){
    //            var rate = parseFloat(data.exchange_rate).toFixed(2);
    //            $("#id_rate").val(rate);
    //         });
    //
    //     }
    //     return false;
    //
    // });

     var record_td = function () {
        var result_list = [];
        $('#tbody_quotation_row tr').each(function() {
            var description = $(this).find("td").eq(0).text();
            var quantity = $(this).find("td").eq(1).text();
            var unit_price = $(this).find("td").eq(2).text();
            var amount_price = $(this).find("td").eq(3).text();
            var result_dict = {};
            result_dict.description = description;
            result_dict.quantity = parseFloat(quantity).toFixed(2);
            result_dict.unit_price = parseFloat(unit_price).toFixed(2);
            result_dict.amount_price = parseFloat(amount_price).toFixed(2);
            result_list.push(result_dict)
        });
        return result_list;
    };

    div_page_wrapper.on('click', '#save_quotation', function(e) {
        var current_date = $('#id_quotation_current_date').val();
        var vehicle = $('#id_quotation_vehicle').val();
        var client = $('#id_quotation_client').val();
        var row_sub_total =  $('#tr_row_sub_total').text();
        var row_igv = $('#tr_row_igv').text();
        var row_total = $('#tr_row_total').text();
        var list_detail = record_td();
        var exchange_rate = 1.00;
        // var exchange_rate = $('#id_quotation_exchange_rate').val();
        if (current_date == ""){
            swal("Error!", "Choice Date", "warning");
            return false;
        }
        if (vehicle == ""){
            swal("Error!", "Choice Vehicle", "warning");
            return false;
        }
        if (client == ""){
            swal("Error!", "Choice Client", "warning");
            return false;
        }
        // if (exchange_rate == ""){
        //     swal("Error!", "Choice Exchange Rate", "warning");
        //     var rate = parseFloat(1).toFixed(2);
        //     $("#id_rate").val(rate);
        //     return false;
        // }

        form_quotation = $('#form_quotation');
        var parameter = {
            "form": get_FormDataserialize(form_quotation),
            "form_quo_detail":list_detail,
            "form_quo":{
                "exchange_rate":parseFloat(exchange_rate).toFixed(2),
                "igv_tax": parseFloat(row_igv).toFixed(2),
                "sub_total":parseFloat(row_sub_total).toFixed(2),
                "total_paid": parseFloat(row_total).toFixed(2)
            }

        };
        $.ajax({
            type: "POST",
            url: URL_QUOTATION_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_quotation.modal('hide');
             swal("Successfull!", "Add new quotation", "success");
             $.get(URL_QUOTATION_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.quotation_edit', function (e) {
        e.preventDefault();
        var quotation_id = $(this).attr('data-id');
        var parameter = {
            'quotation_id': quotation_id
        };
        $.ajax({
            type: "GET",
            url: URL_QUOTATION_EDIT,
            data: parameter
        }).done(function(data) {
           modal_quotation.html(data);
           modal_quotation.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_quotation', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_quotation = $('#form_quotation');
        var parameter = {
            'form': get_FormDataserialize(form_quotation),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_QUOTATION_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_quotation.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_QUOTATION_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

    div_page_wrapper.on('change', '#id_quotation_labour', function (e) {
        e.preventDefault();
        var _this = $(this).val();
        $.get("/api/labour/"+_this+"/", function(data){
             $('#id_quotation_sale_price').val(data.sale_price);
        });
    });

    var amount_td = function () {
        var total_amount = 0;
        $('#tbody_quotation_row tr').each(function() {
            var _amount = $(this).find("td").eq(3).text();
            total_amount = parseFloat(_amount) + parseFloat(total_amount);
        });
        var _igv  = parseFloat(0.18);
        var row_igv  = (total_amount * _igv).toFixed(2);
        var row_sub_total = (total_amount - row_igv).toFixed(2);
        var total  = parseFloat(total_amount).toFixed(2);
         $('#tr_row_sub_total').html(row_sub_total);
         $('#tr_row_igv').html(row_igv);
         $('#tr_row_total').html(total);
    };

    div_page_wrapper.on('click', '#add_quotation_row', function (e) {
        e.preventDefault();
        var description = $('#id_quotation_labour').val();
        var description_text = $('#id_quotation_labour option:selected').text();
        if (description == ""){
            swal("Error!", "choice labour", "warning");
            return false;
        }
        var quantity = 1.00;
        var unit_price = parseFloat($('#id_quotation_sale_price').val());
        var amount = parseFloat(quantity) * parseFloat(unit_price);
        var _tbody = $('#tbody_quotation_row');
        var _tbody_length = $('#tbody_quotation_row tr').length;
        var _tbody_tr_id_last;
        var _tr_row_count = 1;
        if (_tbody_length > 0){
            _tbody_tr_id_last = $('#tbody_quotation_row tr:last').attr("id").split("_")[2];
            _tr_row_count = parseInt(_tbody_tr_id_last) + 1;
        }
        var html = "<tr id='tr_row_"+_tr_row_count+"'>" +
                        "<td class='text-center'>"+description_text+"</td>" +
                        "<td class='text-center'>"+quantity+"</td>" +
                        "<td class='text-center'>"+unit_price.toFixed(2)+"</td>" +
                        "<td class='text-center'>"+amount.toFixed(2)+"</td>" +
                        "<td class='text-center'>" +
                            "<button type='button' class='btn btn-danger btn-circle waves-effect remove_tr_row'><i class='fa fa-times'></i></button>" +
                        "</td>"+
                    "</tr>";
        _tbody.append(html);
        amount_td()

    });



    div_page_wrapper.on('click', '.remove_tr_row', function (e) {
        e.preventDefault();
        var _this = $(this);
        _this.parent().parent().remove();
        amount_td()
    });


    function printDiv(divName) {
         var printContents = document.getElementById(divName).innerHTML;
         var originalContents = document.body.innerHTML;
         document.body.innerHTML = printContents;
         window.open();
         window.print();
         document.body.innerHTML = originalContents;
    }


    div_page_wrapper.on('click', '#print_quotation', function (e) {
        e.preventDefault();
        printDiv('print_doc')
    });



});