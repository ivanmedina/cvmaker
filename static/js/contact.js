function fillContactInfo() {
    const select = document.getElementById('contact_select');
    const name = select.options[select.selectedIndex].getAttribute('data-name');
    const title = select.options[select.selectedIndex].getAttribute('data-title');
    const phone = select.options[select.selectedIndex].getAttribute('data-phone');
    const email = select.options[select.selectedIndex].getAttribute('data-email');
    const address = select.options[select.selectedIndex].getAttribute('data-address');

    document.getElementById('name').value = name;
    document.getElementById('title').value = title;
    document.getElementById('phone').value = phone;
    document.getElementById('email').value = email;
    document.getElementById('address').value = address;
  }