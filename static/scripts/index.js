const fileInput = document.getElementById('fileInput');
const imagePreview = document.getElementById('imagePreview');

fileInput.addEventListener('change', function() {
    const file = this.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function(event) {
            const img = document.createElement('img');
            img.src = event.target.result;
            imagePreview.innerHTML = '';
            imagePreview.appendChild(img);
        }

        reader.readAsDataURL(file);
    } else {
        imagePreview.innerHTML = '';
    }
});

// SECRET_KEY=d6b1f318fd76050b8f8eae6161e82af4
// FLASK_ENV=development
// FLASK_DEBUG=1
// PORT=10000
