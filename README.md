# the-anything-guesser

Welcome to **The Anything Guesser**! 🎉

Ever had a secret answer that you wanted your friends to guess? Well, now you can with this simple and fun web application!

## How It Works

1. **Set an Answer**: Think of something fun, quirky, or challenging and set it as the answer.
2. **Start Guessing**: Share the link with your friends and let them type in their guesses to see if they can figure out the answer.

## Features

- **Easy to Use**: A simple Flask Web Application that allows anyone to quickly join and see 
- **Fun for All Ages**: Perfect for schools! Like Central Columbia!
- **Unlimited Guesses**: Keep guessing until you get it right!

## Get Started

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/the-anything-guesser.git
    ```
2. Navigate to the project directory:
    ```bash
    cd the-anything-guesser
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    python app.py
    ```

## Build and Deploy using Docker

1. Build the Docker image:
    ```bash
    docker build -t the-anything-guesser .
    ```
2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 the-anything-guesser
    ```

Your application should now be running on `http://localhost:5000`.

## License

This project is licensed under the MIT License.

Happy Guessing! 🎊