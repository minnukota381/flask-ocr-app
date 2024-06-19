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
