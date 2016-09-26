$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_typevehicle = $('#add_typevehicle');
    var modal_typevehicle = $('#modal_typevehicle');
    var form_typevehicle;

    div_page_wrapper.on('click', "#add_typevehicle", function(e) {
        e.preventDefault();
        add_typevehicle.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_TYPEVEHICLE_ADD
        }).done(function(data) {
             modal_typevehicle.html(data);
             modal_typevehicle.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_typevehicle.attr("disabled",false);
        });
        return false;
    });


    div_page_wrapper.on('click', '#save_typevehicle', function(e) {
        e.preventDefault();
        form_typevehicle = $('#form_typevehicle');
        var parameter = {
            'form': get_FormDataserialize(form_typevehicle)
        };
        $.ajax({
            type: "POST",
            url: URL_TYPEVEHICLE_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_typevehicle.modal('hide');
             swal("Successfull!", "Add new Type Job", "success");
             $.get(URL_TYPEVEHICLE_LIST, function(data){
                $("#list_table").html(data);
    	     });
        });
        return false;
    });


    div_page_wrapper.on('click', '.typevehicle_edit', function (e) {
        e.preventDefault();
        var typevehicle_id = $(this).attr('data-id');
        var parameter = {
            'typevehicle_id': typevehicle_id
        };
        $.ajax({
            type: "GET",
            url: URL_TYPEVEHICLE_EDIT,
            data: parameter
        }).done(function(data) {
           modal_typevehicle.html(data);
           modal_typevehicle.modal({backdrop: 'static', keyboard: false});
        })
        return false;
    });


    div_page_wrapper.on('click', '#update_typevehicle', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_typevehicle = $('#form_typevehicle');
        var parameter = {
            'form': get_FormDataserialize(form_typevehicle),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_TYPEVEHICLE_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_typevehicle.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_TYPEVEHICLE_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });
        return false;
    });

});