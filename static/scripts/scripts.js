$("#exitConfirm").confirm({
    title:"Подтверждение выхода",
    text:"Вы дествительно хотите продолжить?",
    confirmButton: "Да",
    cancelButton: "Нет",
    confirmButtonClass: "btn-danger",
    cancelButtonClass: "btn-default",
    dialogClass: "modal-dialog modal-lg"
});

$('.dropdown-toggle').dropdown();


$('#id_id_otdel').addClass('filter-margin');
$('#id_year_work').addClass('filter-margin');
$('#id_month_work').addClass('filter-margin');

$('#chkBoxFilterSwitch').change(function() {
  if ($(this).is(':checked')) {
      alert('+');
      document.location.href = '/demowork/filter_ex/'

  } else {
      alert('-');
      document.location.href = '/demowork/'
  }
});

$(function () {
    $(".js-create-demowork").click(function () {
        $.ajax({
            url: 'new/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-demowork").modal("show");
            },
            success: function (data) {
                $("#modal-demowork .modal-content").html(data.html_form);
            }
        });
    });
});

$("#modal-demowork").on("submit", ".js-demowork-create-form", function () {
    var form = $(this);
    $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            if (data.form_is_valid) {
                $("#demoworks-table tbody").html(data.html_demoworks_list); // <-- Replace the table body
                $("#modal-demowork").modal("hide"); // <-- Close the modal
            } else {
                $("#modal-demowork .modal-content").html(data.html_form);
            }
        }
    });
    return false;
});


//$('#exampleModalCenter').modal(options);