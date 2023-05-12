function showAlert() {
  var message = '<div><h3>Покупка билета</h3>' +
                '<label for="quantity">Количество мест (от 1 до 5):</label>' +
                '<input type="number" id="quantity" min="1" max="5">' +
                '<br>' +
                '<label for="time">Время сеанса:</label>' +
                '<select id="time">' +
                '<option value="10:00">10:00</option>' +
                '<option value="11:00">11:00</option>' +
                '<option value="12:00">12:00</option>' +
                '<option value="13:00">13:00</option>' +
                '<option value="14:00">14:00</option>' +
                '<option value="15:00">15:00</option>' +
                '<option value="16:00">16:00</option>' +
                '<option value="18:00">18:00</option>' +
                '<option value="20:00">20:00</option>' +
                '</select>' +
                '</div>';

  alertify.alert(message);
}