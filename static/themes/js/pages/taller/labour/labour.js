$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_labour = $('#add_labour');
    var modal_labour = $('#modal_labour');
    var form_labour;

    div_page_wrapper.on('click', "#add_labour", function(e) {
        e.preventDefault();
        add_labour.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_LABOUR_ADD
        }).done(function(data) {
             modal_labour.html(data);
             modal_labour.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_labour.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_labour', function(e) {
        form_labour = $('#form_labour');
        var parameter = {
            'form': get_FormDataserialize(form_labour)
        };
        $.ajax({
            type: "POST",
            url: URL_LABOUR_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_labour.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_LABOUR_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.labour_edit', function (e) {
        e.preventDefault();
        var labour_id = $(this).attr('data-id');
        var parameter = {
            'labour_id': labour_id
        };
        $.ajax({
            type: "GET",
            url: URL_LABOUR_EDIT,
            data: parameter
        }).done(function(data) {
           modal_labour.html(data);
           modal_labour.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_labour', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_labour = $('#form_labour');
        var parameter = {
            'form': get_FormDataserialize(form_labour),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_LABOUR_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_labour.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_LABOUR_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})