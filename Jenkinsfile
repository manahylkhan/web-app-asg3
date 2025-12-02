pipeline {
    agent any

    stages {

        /* -------------------------
           1) CHECKOUT CODE
           ------------------------- */
        stage('Checkout Code') {
            steps {
                checkout scm
                echo "Code successfully pulled from GitHub"
            }
        }

        /* -------------------------
           2) CODE LINTING
           ------------------------- */
        stage('Code Linting') {
            steps {
                echo "Running flake8 linting..."
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install flake8
                    flake8 app/ --exit-zero --count --statistics --show-source || true
                '''
            }
        }

        /* -------------------------
           3) CODE BUILD (Docker Image)
           ------------------------- */
        stage('Code Build') {
            steps {
                echo "Building Docker image for Flask app..."
                sh 'docker build -t myapp:latest .'
            }
        }

        /* -------------------------
           4) UNIT TESTING (pytest)
           ------------------------- */
        stage('Unit Testing') {
            steps {
                echo "Running unit tests using pytest..."
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r app/requirements.txt
                    pytest app/tests -v
                '''
            }
        }

        /* -------------------------
           5) Containerized Deployment
           ------------------------- */
        stage('Containerized Deployment') {
            steps {
                echo "Deploying application using docker-compose..."
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }

        /* -------------------------
           6) Selenium/E2E Testing
           ------------------------- */
        stage('Selenium Testing') {
            steps {
                echo "Running Selenium/End-to-End tests..."
                dir('selenium-tests') {
                    // Build selenium test container
                    sh 'docker build -t selenium-tests .'

                    // Run tests inside same docker-compose network
                    sh 'docker run --rm --network selenium-asg_default selenium-tests'
                }
            }
        }
    }

    /* -------------------------
       POST BUILD CLEANUP
       ------------------------- */
    post {
        always {
            echo "Cleaning up containers..."
            sh 'docker-compose down || true'
        }

        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed. Please check logs."
        }
    }
}
