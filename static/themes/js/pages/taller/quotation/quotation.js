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


    div_page_wrapper.on('click', '#save_quotation', function(e) {
        form_quotation = $('#form_quotation');
        var parameter = {
            'form': get_FormDataserialize(form_quotation)
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

})