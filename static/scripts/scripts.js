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
$('#id_date_work__year').addClass('filter-margin').attr('placeholder', 'Год');
$('#id_date_work__month').addClass('filter-margin').attr('placeholder', 'Месяц');

$(function() {
      $("#chkBoxFilterSwitch").change(function() {
          if ($(this).is(':checked')) {
              $.ajax({
                  url: '/demowork/filter_ex/',
                  cache: false,
                  success: function(response) {
                      window.location.href = response.url;
                      $window.location.reload();

                  }
              })
          } else {

              $.ajax({
                  url: '/demowork/',
                  cache: false,
                  success: function (response) {
                      window.location.href = response.url;

                  }
              })
          }
      });
});

//$('#exampleModalCenter').modal(options);