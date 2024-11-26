function fillLanguageInfo() {
    const select = document.getElementById('language_select');
    const name = select.options[select.selectedIndex].getAttribute('data-name');
    const level = select.options[select.selectedIndex].getAttribute('data-level');

    document.getElementById('language_name').value = name;
    document.getElementById('language_level').value = level;
  }