$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_organization = $('#add_organization');
    var modal_organization = $('#modal_organization');
    var form_organization;

    div_page_wrapper.on('click', "#add_organization", function(e) {
        e.preventDefault();
        add_organization.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_ORGANIZATION_ADD
        }).done(function(data) {
             modal_organization.html(data);
             modal_organization.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_organization.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_organization', function(e) {
        form_organization = $('#form_organization');
        var parameter = {
            'form': get_FormDataserialize(form_organization)
        };
        $.ajax({
            type: "POST",
            url: URL_ORGANIZATION_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_organization.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_ORGANIZATION_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.organization_edit', function (e) {
        e.preventDefault();
        var organization_id = $(this).attr('data-id');
        var parameter = {
            'organization_id': organization_id
        };
        $.ajax({
            type: "GET",
            url: URL_ORGANIZATION_EDIT,
            data: parameter
        }).done(function(data) {
           modal_organization.html(data);
           modal_organization.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_organization', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_organization = $('#form_organization');
        var parameter = {
            'form': get_FormDataserialize(form_organization),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_ORGANIZATION_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_organization.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_ORGANIZATION_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})