$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_measurement = $('#add_measurement');
    var modal_measurement = $('#modal_measurement');
    var form_measurement;

    div_page_wrapper.on('click', "#add_measurement", function(e) {
        e.preventDefault();
        add_measurement.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_MEASUREMENT_ADD
        }).done(function(data) {
             modal_measurement.html(data);
             modal_measurement.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_measurement.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_measurement', function(e) {
        form_measurement = $('#form_measurement');
        var parameter = {
            'form': get_FormDataserialize(form_measurement)
        };
        $.ajax({
            type: "POST",
            url: URL_MEASUREMENT_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_measurement.modal('hide');
             swal("Successfull!", "Add new Brand", "success")
             $.get(URL_MEASUREMENT_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.measurement_edit', function (e) {
        e.preventDefault();
        var measurement_id = $(this).attr('data-id');
        var parameter = {
            'measurement_id': measurement_id
        };
        $.ajax({
            type: "GET",
            url: URL_MEASUREMENT_EDIT,
            data: parameter
        }).done(function(data) {
           modal_measurement.html(data);
           modal_measurement.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_measurement', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_measurement = $('#form_measurement');
        var parameter = {
            'form': get_FormDataserialize(form_measurement),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_MEASUREMENT_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_measurement.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_MEASUREMENT_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})