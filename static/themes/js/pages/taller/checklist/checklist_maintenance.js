(function () {

    var div_page_wrapper = $('#page-wrapper');
    var modal_checklist = $('#modal_checklist');

    div_page_wrapper.on('click', ".maintenance_add_task", function(e) {
        e.preventDefault();
        var id = $(this).attr('data-id');
        var parameter = {'checklist_detail_id': id};

        $.ajax({
            type: "GET",
            url: URL_CHECKLIST_ADD_LABOUR,
            data: parameter
        }).done(function(data) {
             modal_checklist.html(data);
             modal_checklist.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', "#save_form_labour_employee", function(){
        var form_labour_employee = $('#form_labour_employee');
        var id = $(this).attr('data-checklist-detail-id');
        var parameter = {
            'form': get_FormDataserialize(form_labour_employee),
            'checklist_detail_id': id
        };
        $.ajax({
            type: "POST",
            url: URL_CHECKLIST_ADD_LABOUR,
            data: parameter
        }).done(function(data) {
             modal_checklist.modal('hide');
             // swal("Successfull!", "Add new Brand", "success")

        })

    })

})();

