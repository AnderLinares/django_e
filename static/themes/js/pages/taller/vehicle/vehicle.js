$(document).ready(function () {
    $('#myTable').DataTable();

    var div_page_wrapper = $('#page-wrapper');
    var add_vehicle = $('#add_vehicle');
    var modal_vehicle = $('#modal_vehicle');
    var form_vehicle;

    div_page_wrapper.on('click', "#add_vehicle", function(e) {
        e.preventDefault();
        add_vehicle.attr("disabled",true);
        $.ajax({
            type: "GET",
            url: URL_VEHICLE_ADD
        }).done(function(data) {
             modal_vehicle.html(data);
             modal_vehicle.modal({backdrop: 'static', keyboard: false});
        }).always(function() {
              add_vehicle.attr("disabled",false);
        });
    });


    div_page_wrapper.on('click', '#save_vehicle', function(e) {
        form_vehicle = $('#form_vehicle');
        var parameter = {
            'form': get_FormDataserialize(form_vehicle)
        };
        $.ajax({
            type: "POST",
            url: URL_VEHICLE_ADD,
            data: JSON.stringify(parameter)
        }).done(function(data) {
             modal_vehicle.modal('hide');
             swal("Successfull!", "Add new vehicle", "success");
             $.get(URL_VEHICLE_LIST, function(data){
                $("#list_table").html(data);
    	     });
        })
    });


    div_page_wrapper.on('click', '.vehicle_edit', function (e) {
        e.preventDefault();
        var vehicle_id = $(this).attr('data-id');
        var parameter = {
            'vehicle_id': vehicle_id
        };
        $.ajax({
            type: "GET",
            url: URL_VEHICLE_EDIT,
            data: parameter
        }).done(function(data) {
           modal_vehicle.html(data);
           modal_vehicle.modal({backdrop: 'static', keyboard: false});
        })
    });


    div_page_wrapper.on('click', '#update_vehicle', function (e) {
        e.preventDefault();
        var form_pk = $(this).attr('data-id');
        form_vehicle = $('#form_vehicle');
        var parameter = {
            'form': get_FormDataserialize(form_vehicle),
            'form_pk': form_pk
        };
        $.ajax({
            type: "POST",
            url: URL_VEHICLE_EDIT,
            data: JSON.stringify(parameter)
        }).done(function(data) {
           modal_vehicle.modal('hide');
           swal("Successfull!", "", "success")
        }).always(function() {
            $.get(URL_VEHICLE_LIST, function(data){
                $("#list_table").html(data);
    	    });
        });

    });

})