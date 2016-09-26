$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_report = $('#add_report');
    var modal_report = $('#modal_report');
    var form_report;

    div_page_wrapper.on('click', "#add_report", function(e) {
        e.preventDefault();
        add_report.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_REPORT_ADD
        }).done(function(data) {
             modal_report.html(data);
             modal_report.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_report.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_report', function(e) {
        var form_report = $('#form_report');
        var parameter = {
            'form': get_FormDataserialize(form_report)
        };

        $.ajax({
            type: "POST",
            url: URL_REPORT_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_report.modal('hide');
             swal("Successfull!", "Add new Type Job", "success");
             $.get(URL_REPORT_LIST, function(data){
                $("#list_table").html(data);
    	     });
        });

    });


    div_page_wrapper.on('click', '.report_edit', function (e) {
        e.preventDefault();
        var report_id = $(this).attr('data-id');
        var parameter = {
            'report_id': report_id
        };
        $.ajax({
            type: "GET",
            url: URL_REPORT_EDIT,
            data: parameter
        }).done(function(data) {
           modal_report.html(data);
           modal_report.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_report', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_report = $('#form_report');
        var parameter = {
            'form': get_FormDataserialize(form_report),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_REPORT_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_report.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_REPORT_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

});