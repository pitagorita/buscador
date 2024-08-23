document.getElementById('query').addEventListener('input', function() {
    const query = this.value;
    fetch(`/buscar?q=${encodeURIComponent(query)}`)
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '';

            if (data.length > 0) {
                data.forEach(item => {
                    let p = document.createElement('p');
                    p.textContent = JSON.stringify(item);
                    resultsDiv.appendChild(p);
                });
            } else {
                resultsDiv.textContent = 'No se encontraron resultados';
            }
        });
});
