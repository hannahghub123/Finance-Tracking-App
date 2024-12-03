function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}$

(document).on('click', '#add_expense', function (e) {
    e.preventDefault();
    console.log("Add Expense button clicked");
    $('.has-error').removeClass('has-error');
    $('.error-message').html('');
    $("#addExpense").modal('show');
});


$(document).on('click', '#addexpense_submit', function (e) {
    e.preventDefault();    
    $('.has-error').removeClass('has-error');
    $('.error-message').html('');
    var csrftoken = getCookie('csrftoken');
    $.post('/add-expense/', $("#add_expense_form").serialize(), function (response) {        
        if (response.status === 0) {
            $.each(response.data, function (key, value) {
                $('#id_' + key).parent().addClass('has-error');
                $('#id_' + key).siblings().html(value);
            });
        } else if (response.status == 1) {
            location.reload();
        }
    }, 'json');

});


$(document).on('click', '#add_income', function () {
    $('.has-error').removeClass('has-error');
    $('.error-message').html('');
    $("#addIncome").modal('show');
});


$(document).on('click', '#addincome_submit', function (e) {
    e.preventDefault();
    $('.has-error').removeClass('has-error');
    $('.error-message').html('');
    var csrftoken = getCookie('csrftoken');
    $.post('/add-income/', $("#add_income_form").serialize(), function (response) {
        if (response.status === 0) {
            $.each(response.data, function (key, value) {
                $('#id_' + key).parent().addClass('has-error');
                $('#id_' + key).siblings().html(value);
            });
        } else if (response.status == 1) {
            location.reload();
        }
    }, 'json');

});
