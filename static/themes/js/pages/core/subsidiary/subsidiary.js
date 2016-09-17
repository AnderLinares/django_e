$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_subsidiary = $('#add_subsidiary');
    var modal_subsidiary = $('#modal_subsidiary');
    var form_subsidiary;

    div_page_wrapper.on('click', "#add_subsidiary", function(e) {
        e.preventDefault();
        add_subsidiary.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_SUBSIDIARY_ADD
        }).done(function(data) {
             modal_subsidiary.html(data);
             modal_subsidiary.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_subsidiary.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_subsidiary', function(e) {
        form_subsidiary = $('#form_subsidiary');
        var parameter = {
            'form': get_FormDataserialize(form_subsidiary)
        };
        $.ajax({
            type: "POST",
            url: URL_SUBSIDIARY_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_subsidiary.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_SUBSIDIARY_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.subsidiary_edit', function (e) {
        e.preventDefault();
        var subsidiary_id = $(this).attr('data-id');
        var parameter = {
            'subsidiary_id': subsidiary_id
        };
        $.ajax({
            type: "GET",
            url: URL_SUBSIDIARY_EDIT,
            data: parameter
        }).done(function(data) {
           modal_subsidiary.html(data);
           modal_subsidiary.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_subsidiary', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_subsidiary = $('#form_subsidiary');
        var parameter = {
            'form': get_FormDataserialize(form_subsidiary),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_SUBSIDIARY_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_subsidiary.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_SUBSIDIARY_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})