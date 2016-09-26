$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_typejob = $('#add_typejob');
    var modal_typejob = $('#modal_typejob');
    var form_typejob;

    div_page_wrapper.on('click', "#add_typejob", function(e) {
        e.preventDefault();
        add_typejob.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_TYPEJOB_ADD
        }).done(function(data) {
             modal_typejob.html(data);
             modal_typejob.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_typejob.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_typejob', function(e) {
        form_typejob = $('#form_typejob');
        var parameter = {
            'form': get_FormDataserialize(form_typejob)
        };
        $.ajax({
            type: "POST",
            url: URL_TYPEJOB_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_typejob.modal('hide');
             swal("Successfull!", "Add new Type Job", "success");
             $.get(URL_TYPEJOB_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.typejob_edit', function (e) {
        e.preventDefault();
        var typejob_id = $(this).attr('data-id');
        var parameter = {
            'typejob_id': typejob_id
        };
        $.ajax({
            type: "GET",
            url: URL_TYPEJOB_EDIT,
            data: parameter
        }).done(function(data) {
           modal_typejob.html(data);
           modal_typejob.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_typejob', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_typejob = $('#form_typejob');
        var parameter = {
            'form': get_FormDataserialize(form_typejob),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_TYPEJOB_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_typejob.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_TYPEJOB_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

});