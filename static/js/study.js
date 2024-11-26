function fillStudyInfo() {
    const select = document.getElementById('study_select');
    const school = select.options[select.selectedIndex].getAttribute('data-school');
    const career = select.options[select.selectedIndex].getAttribute('data-career');
    const description = select.options[select.selectedIndex].getAttribute('data-description')
    document.getElementById('school').value = school;
    document.getElementById('career').value = career;
    document.getElementById('studies-description').value = description;

  }