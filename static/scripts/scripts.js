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
/* Functions */
    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-demowork").modal("show");
            },
            success: function (data) {
                $("#modal-demowork .modal-content").html(data.html_form);
            }
        });
    };
    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    $("#demowork-table tbody").html(data.html_demowork_list);
                    $("#modal-demowork").modal("hide");
                } else {
                    $("#modal-demowork .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
    /* Binding */
    // Create book
    $(".js-create-demowork").click(loadForm);
    $("#modal-demowork").on("submit", ".js-demowork-create-form", saveForm);
    // Update book
    $("#demowork-table").on("click", ".js-update-demowork", loadForm);
    $("#modal-demowork").on("submit", ".js-demowork-update-form", saveForm);
    // Delete book
    $("#demowork-table").on("click", ".js-delete-demowork", loadForm);
    $("#modal-demowork").on("submit", ".js-demowork-delete-form", saveForm);
});


//$('#exampleModalCenter').modal(options);