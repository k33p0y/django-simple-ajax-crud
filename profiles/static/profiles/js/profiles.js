$(function () {
    $(".js-create-profile").click(function () {
      $.ajax({
        url: '/profiles/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-profile").modal("show");
        },
        success: function (data) {
          $("#modal-profile .modal-content").html(data.html_form);
        }
      });
    });
  
  });

  $("#modal-profile").on("submit", ".js-profile-create-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $("#profile-table tbody").html(data.html_profile_list);  // <-- Replace the table body
            $("#modal-profile").modal("hide");
        }
        else {
          $("#modal-profile .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });