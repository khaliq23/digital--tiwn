document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    fetch('/api/predict', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({/* input data */})
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('results').innerText = JSON.stringify(data);
    });
});
