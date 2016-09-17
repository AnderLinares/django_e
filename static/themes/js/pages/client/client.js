$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_person = $('#add_person');
    var modal_person = $('#modal_person');
    var form_person;

    div_page_wrapper.on('click', "#add_client", function(e) {
        e.preventDefault();
        add_person.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_CLIENT_ADD
        }).done(function(data) {
             modal_person.html(data);
             modal_person.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_person.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_person', function(e) {
        form_person = $('#form_person');
        var parameter = {
            'form': get_FormDataserialize(form_person)
        };
        $.ajax({
            type: "POST",
            url: URL_CLIENT_ADD,
            data: JSON.stringify(parameter),
        }).done(function(data) {
             modal_person.modal('hide');
             swal("Successfull!", "Add new Client", "success")
        })
    });


    div_page_wrapper.on('click', '.person_edit', function (e) {
        e.preventDefault();
        var person_id = $(this).attr('data-id');
        var parameter = {
            'person_id': person_id
        };
        $.ajax({
            type: "GET",
            url: URL_CLIENT_EDIT,
            data: parameter
        }).done(function(data) {
           modal_person.html(data);
           modal_person.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_person', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_person = $('#form_person');
        var parameter = {
            'form': get_FormDataserialize(form_person),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_CLIENT_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_person.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_CLIENT_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})