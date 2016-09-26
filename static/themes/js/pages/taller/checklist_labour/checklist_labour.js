$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_checklist_labour = $('#add_checklist_labour');
    var modal_checklist_labour = $('#modal_checklist_labour');
    var form_checklist_labour_employee;


    div_page_wrapper.on('click', '.checklist_labour_task', function(e) {
        e.preventDefault();
        var checklist_labour_id = $(this).attr('data-id');
        var parameter = {
            'checklist_labour_id': checklist_labour_id
        };
        $.ajax({
            type: "GET",
            url: URL_CHECKLIST_LABOUR_TASK,
            data: parameter
        }).done(function(data) {
           modal_checklist_labour.html(data);
           modal_checklist_labour.modal({backdrop: 'static', keyboard: false});
        })
    });

    div_page_wrapper.on('click', '#save_checklist_labour_task', function(e) {
        form_checklist_labour_employee = $('#form_checklist_labour_employee');
        var form_pk = $(this).attr('data-id');
        var parameter = {
            'form': get_FormDataserialize(form_checklist_labour_employee),
            'form_pk':form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_CHECKLIST_LABOUR_TASK,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_checklist_labour.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_CHECKLIST_LABOUR_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.checklist_labour_edit', function (e) {
        e.preventDefault();
        var checklist_labour_id = $(this).attr('data-id');
        var parameter = {
            'checklist_labour_id': checklist_labour_id
        };
        $.ajax({
            type: "GET",
            url: URL_CHECKLIST_LABOUR_EDIT,
            data: parameter
        }).done(function(data) {
           modal_checklist_labour.html(data);
           modal_checklist_labour.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_checklist_labour', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_checklist_labour = $('#form_checklist_labour');
        var parameter = {
            'form': get_FormDataserialize(form_checklist_labour),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_CHECKLIST_LABOUR_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_checklist_labour.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_CHECKLIST_LABOUR_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})