(function () {

    $('#id_checklist_detail_date_initial').datepicker({autoclose: true, format: 'yyyy-mm-dd', language:'es'});

     $('#id_checklist_detail_hour_initial').clockpicker(
         {
             placement: 'bottom',
             align: 'left',
             autoclose: true,
             'default': 'now'
     });


    $('#exampleBasic').wizard({
         validator: function () {
          var checklist_detail_service = $('#id_checklist_detail_service_checklist').val();
          var checklist_detail_type_transport = $('#id_checklist_detail_type_transport').val();
          var checklist_detail_type_checklist = $('#id_checklist_detail_type_checklist').val();
          var checklist_client = $('#id_checklist_client').val();
          var checklist_number_contract = $('#id_checklist_number_contract').val();

           if (checklist_detail_service == "" || checklist_detail_service == null){
               swal("Error!", "Choice Service !", "warning");
               return false;
           }
           if (checklist_detail_type_transport == "" || checklist_detail_type_transport == null){
               swal("Error!", "choice Vehicle!", "warning");
                return false;
           }
           if (checklist_detail_type_checklist == "" || checklist_detail_type_checklist == null){
               swal("Error!", "Choice Type Checklist!", "warning");
               return false;
           }
           if (checklist_client == "" || checklist_client == null){
               swal("Error!", "Choice Client Checklist!", "warning");
                return false;
           }
           if (checklist_number_contract == "" || checklist_number_contract == null){
               swal("Error!", "Choice Number Contract!", "warning");
                return false;
           }

           return true;

        },
        onFinish: function () {
            swal({
                title: "Are you sure?",
                text: "You send the information!",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#03a9f3",
                confirmButtonText: "Yes, send it!",
                closeOnConfirm: false
            }, function(isConfirm){
                if (isConfirm) {
                    swal("Submit!", "The form has been sent.", "success");
                    $("#form_checklist").submit();
                }
            });

        }
    });



})();
