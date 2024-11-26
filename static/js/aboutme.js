function fillAboutMeInfo() {
    const select = document.getElementById('about_me_select');
    const description = select.options[select.selectedIndex].getAttribute('data-description');

    document.getElementById('description').value = description;
  }