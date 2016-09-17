$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_exchangerate = $('#add_exchangerate');
    var modal_exchangerate = $('#modal_exchangerate');
    var form_exchangerate;

    div_page_wrapper.on('click', "#add_exchangerate", function(e) {
        e.preventDefault();
        add_exchangerate.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_EXCHANGERATE_ADD
        }).done(function(data) {
             modal_exchangerate.html(data);
             modal_exchangerate.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_exchangerate.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_exchangerate', function(e) {
        form_exchangerate = $('#form_exchangerate');
        var parameter = {
            'form': get_FormDataserialize(form_exchangerate)
        };
        $.ajax({
            type: "POST",
            url: URL_EXCHANGERATE_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_exchangerate.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_EXCHANGERATE_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.exchangerate_edit', function (e) {
        e.preventDefault();
        var exchangerate_id = $(this).attr('data-id');
        var parameter = {
            'exchangerate_id': exchangerate_id
        };
        $.ajax({
            type: "GET",
            url: URL_EXCHANGERATE_EDIT,
            data: parameter
        }).done(function(data) {
           modal_exchangerate.html(data);
           modal_exchangerate.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_exchangerate', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_exchangerate = $('#form_exchangerate');
        var parameter = {
            'form': get_FormDataserialize(form_exchangerate),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_EXCHANGERATE_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_exchangerate.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_EXCHANGERATE_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})