(function () {

    var div_page_wrapper = $('#page-wrapper');
    var modal_labour = $('#modal_labour');

    div_page_wrapper.on('click', '.labour_employees_add_task', function (e) {
        e.preventDefault();
        var labour_id = $(this).attr('data-id');
        var parameter = {
            'labour_id': labour_id
        };
        $.ajax({
            type: "GET",
            url: URL_LABOUR_EDIT,
            data: parameter
        }).done(function(data) {
           modal_labour.html(data);
           modal_labour.modal({backdrop: 'static', keyboard: false});
        })
    });

})();

