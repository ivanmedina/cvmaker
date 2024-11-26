function goToStep(step) {
    const tabs = document.querySelectorAll('#stepper button');
    const content = document.querySelectorAll('.tab-pane');
  
    tabs.forEach((tab, index) => {
      if (index === step - 1) {
        tab.classList.add('active');
      } else {
        tab.classList.remove('active');
      }
    });
  
    content.forEach((pane, index) => {
      if (index === step - 1) {
        pane.classList.add('show', 'active');
      } else {
        pane.classList.remove('show', 'active');
      }
    });
}

function finish() {
    const form = document.getElementById('create-cv-form');
    const formData = new FormData(form);

    const cvData = {
        name: formData.get('name'),
        title: formData.get('title'),
        address: formData.get('address'),
        phone: formData.get('phone'),
        email: formData.get('email'),
        languages: formData.getAll('language_name').map((name, index) => ({
            name: name,
            level: formData.getAll('language_level')[index]
        })),
        school: formData.get('school'),
        career: formData.get('career'),
        skills: formData.getAll('skill'),
        certifications: formData.getAll('certification[]'),
        aboutme: formData.get('description'),
        jobs: formData.getAll('company[]').map((company, index) => ({
            company: company,
            title: formData.getAll('job_title[]')[index],
            date: `${formData.getAll('date1[]')[index]}-${formData.getAll('date2[]')[index]}`,
            description: formData.getAll('job_description[]')[index]
        }))
    };

    fetch('/save_cv', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cvData)
    })
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'cv_data.json';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

