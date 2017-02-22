$('.btn_help').on('click', function () {
    $(this).removeClass('btn_join');
    $(this).removeClass('btn_log');
    $(this).addClass('btn_help');
});
$('.btn_join').on('click', function () {
    $(this).removeClass('btn_help');
    $(this).removeClass('btn_log');
    $(this).addClass('btn_join');
});
$('.btn_log').on('click', function () {
    $(this).removeClass('btn_help');
    $(this).removeClass('btn_join');
    $(this).addClass('btn_log');
});
