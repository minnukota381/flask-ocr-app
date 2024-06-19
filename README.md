# Flask OCR App [Image to Text Converter]

A web application that allows users to upload an image and convert it to text using Optical Character Recognition (OCR) technology. This application supports user authentication and provides a user-friendly interface for image uploads and text extraction.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (Registration, Login, Logout)
- Upload image and convert it to text
- Display extracted text
- Responsive design for mobile and desktop screens

## Installation

### Prerequisites

- Python 3.x
- Flask
- SQLite
- EasyOCR
- Pillow
- Werkzeug

### Step-by-Step Guide

1. **Clone the repository**:

   ```sh
   git clone https://github.com/minnukota381/flask-ocr-app.git
   cd flask-ocr-app
   ```

2. **Create a virtual environment**:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install the required dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   Create a `.env` file in the project root and add your secret key:

   ```bash
   SECRET_KEY=your_secret_key_here
   ```

5. **Set up the SQLite database**:

   ```sh
   python -c "from app import create_connection; create_connection()"
   ```

6. **Run the Flask application**:

   ```sh
   flask run
   ```

7. **Open the app in your browser**:
   Navigate to `http://127.0.0.1:5000` in your web browser.

## Usage

1. **Register or Login**:
   - If you are a new user, register an account.
   - If you already have an account, log in.

2. **Upload an Image**:
   - Click the "Choose File" button to select an image from your device.
   - Click "Convert" to upload the image and extract text.

3. **View Extracted Text**:
   - The extracted text from the uploaded image will be displayed in the text area.

## Project Structure

```bash
flask-ocr-app/
│
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── Procfile               # For deployment (Heroku)
├── templates/
│   ├── index.html         # Main HTML file
│   ├── login.html         # Login HTML file
│   └── register.html      # Register HTML file
├── static/
│   ├── stylesheets/
│   │   └── login.css     # CSS for login page
│   │   └── register.css  # CSS for register page
│   │   └── index.css     # CSS for main page
│   └── images/
│   └── scripts/
│       └── index.js       # JavaScript for client-side interactions
└── .env                   # Environment variables
└── README.md              # This README file
```

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **OCR Engine**: EasyOCR
- **Image Processing**: Pillow
- **Database**: SQLite
- **Authentication**: Werkzeug
- **Deployment**: Heroku

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
