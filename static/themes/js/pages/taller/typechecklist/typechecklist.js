$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_typechecklist = $('#add_typechecklist');
    var modal_typechecklist = $('#modal_typechecklist');
    var form_typechecklist;

    div_page_wrapper.on('click', "#add_typechecklist", function(e) {
        e.preventDefault();
        add_typechecklist.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_TYPECHECKLIST_ADD
        }).done(function(data) {
             modal_typechecklist.html(data);
             modal_typechecklist.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_typechecklist.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_typechecklist', function(e) {
        e.preventDefault();
        form_typechecklist = $('#form_typechecklist');
        var parameter = {
            'form': get_FormDataserialize(form_typechecklist)
        };
        $.ajax({
            type: "POST",
            url: URL_TYPECHECKLIST_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_typechecklist.modal('hide');
             swal("Successfull!", "Add new Type Job", "success");
             $.get(URL_TYPECHECKLIST_LIST, function(data){
                $("#list_table").html(data);
    	     });
        });
        return false;
    });


    div_page_wrapper.on('click', '.typechecklist_edit', function (e) {
        e.preventDefault();
        var typechecklist_id = $(this).attr('data-id');
        var parameter = {
            'typechecklist_id': typechecklist_id
        };
        $.ajax({
            type: "GET",
            url: URL_TYPECHECKLIST_EDIT,
            data: parameter
        }).done(function(data) {
           modal_typechecklist.html(data);
           modal_typechecklist.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_typechecklist', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_typechecklist = $('#form_typechecklist');
        var parameter = {
            'form': get_FormDataserialize(form_typechecklist),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_TYPECHECKLIST_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_typechecklist.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_TYPECHECKLIST_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

});