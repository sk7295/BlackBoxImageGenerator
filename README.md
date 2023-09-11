# Black Box Model Visualization App

This repository contains a Flask application that allows users to visualize black box models. Users can input the name of their model, specify inputs and outputs, and the application will generate a visual representation of the model as a black box.

## Prerequisites

- Python 3.8 or newer
- Docker (optional for containerized deployment)

## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/ahillman89/BlackBoxImageGenerator.git
    cd BlackBoxImageGenerator
    ```

2. **Set up a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Local Development Server

1. **Start the Flask development server**:

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

    Visit `http://127.0.0.1:5000/` in your web browser to access the application.

### Using Docker

1. **Build the Docker image**:

    ```bash
    docker build -t bbm_visualization .
    ```

2. **Run the Docker container**:

    ```bash
    docker run -p 5000:5000 bbm_visualization
    ```

    Access the application at `http://localhost:5000/`.

## Deployment to Google App Engine

1. **Install the Google Cloud SDK**:
   
    Follow the instructions [here](https://cloud.google.com/sdk/docs/install) to install the Google Cloud SDK.

2. **Authenticate with Google Cloud**:

    ```bash
    gcloud auth login
    ```

3. **Set the Google Cloud project**:

    ```bash
    gcloud config set project YOUR_PROJECT_ID
    ```

4. **Deploy the application**:

    ```bash
    gcloud app deploy
    ```

    Once deployed, you can view your application in the browser using the URL provided by the Google Cloud SDK.

## Troubleshooting

If you face a "502 Bad Gateway" error with NGINX when accessing your application on Google App Engine, you either have a memor problem or your app is not starting properly when the app engine instance is spun up by Google App Engine.

## Contributing

Pull requests are welcome. For major changes, please open an issue first or email me to discuss what you would like to change.

## License

This project is licensed under the MIT License.

