**#RAHNUMA**

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

**UI REPRESENTATION:**

**LOGIN PAGE:**

![LOGIN PAGE](https://github.com/user-attachments/assets/08f18366-fd3d-4f96-93ec-7076b28dc2e6)


**HOME PAGE:**

![HOME PAGE](https://github.com/user-attachments/assets/4e4ea279-262d-4c60-ae8a-ec30a6b46fbb)

**SERVICE PAGE:**

![SERVICE PAGE](https://github.com/user-attachments/assets/5e30f67d-ec30-41fd-b2bd-b1fbf5b1f53e)

**ABOUT PAGE:**

![ABOUT PAGE](https://github.com/user-attachments/assets/6cf60906-316b-47f5-aaad-415f163e431d)

**CONTACT PAGE:**

![CONTACT PAGE](https://github.com/user-attachments/assets/7411689b-d63e-4032-92d0-d525be897679)

