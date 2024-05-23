# Rahnuma

Rahnuma is a Flask web application for navigating through different pages, with user authentication and session management.

## Features

- User login and logout functionality
- Session management with a 30-minute lifetime
- Flash messages for providing feedback to users

## How to Use

1. Clone the repository to your local machine.
2. Install Flask using `pip install Flask`.
3. Run the Flask application by executing `python app.py` in your terminal.
4. Access the application in your web browser at `http://localhost:5000`.

## Routes

- `/`: Login page. Users can log in with a username.
- `/home`: Home page.
- `/about`: About page.
- `/service`: Service page.
- `/contact`: Contact page.
- `/user`: User page, accessible only after login. Displays the username of the logged-in user.
- `/logout`: Logs out the current user and redirects to the login page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
