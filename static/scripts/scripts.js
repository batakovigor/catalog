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


//$('#exampleModalCenter').modal(options);