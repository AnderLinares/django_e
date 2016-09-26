$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_client = $('#add_client');
    var modal_client = $('#modal_client');
    var form_client;

    div_page_wrapper.on('click', "#add_client", function(e) {
        add_client.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_CLIENT_ADD
        }).done(function(data) {
             modal_client.html(data);
             modal_client.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_client.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_client', function(e) {
        form_client = $('#form_client');
        var parameter = {
            'form': get_FormDataserialize(form_client)
        };
        $.ajax({
            type: "POST",
            url: URL_CLIENT_ADD,
            data: JSON.stringify(parameter),
        }).done(function(data) {
             modal_client.modal('hide');
             swal("Successfull!", "Add new Client", "success")
        }).always(function() {
            $.get(URL_CLIENT_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });
    });


    div_page_wrapper.on('click', '.client_edit', function (e) {
        e.preventDefault();
        var client_id = $(this).attr('data-id');
        var parameter = {
            'client_id': client_id
        };
        $.ajax({
            type: "GET",
            url: URL_CLIENT_EDIT,
            data: parameter
        }).done(function(data) {
           modal_client.html(data);
           modal_client.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_client', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_client = $('#form_client');
        var parameter = {
            'form': get_FormDataserialize(form_client),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_CLIENT_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_client.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_CLIENT_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})