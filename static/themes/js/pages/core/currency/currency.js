$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_currency = $('#add_currency');
    var modal_currency = $('#modal_currency');
    var form_currency;

    div_page_wrapper.on('click', "#add_currency", function(e) {
        e.preventDefault();
        add_currency.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_CURRENCY_ADD
        }).done(function(data) {
             modal_currency.html(data);
             modal_currency.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_currency.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_currency', function(e) {
        form_currency = $('#form_currency');
        var parameter = {
            'form': get_FormDataserialize(form_currency)
        };
        $.ajax({
            type: "POST",
            url: URL_CURRENCY_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_currency.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_CURRENCY_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.currency_edit', function (e) {
        e.preventDefault();
        var currency_id = $(this).attr('data-id');
        var parameter = {
            'currency_id': currency_id
        };
        $.ajax({
            type: "GET",
            url: URL_CURRENCY_EDIT,
            data: parameter
        }).done(function(data) {
           modal_currency.html(data);
           modal_currency.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_currency', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_currency = $('#form_currency');
        var parameter = {
            'form': get_FormDataserialize(form_currency),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_CURRENCY_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_currency.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_CURRENCY_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})