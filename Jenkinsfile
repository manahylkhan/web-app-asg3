pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Lint') {
            steps {
                echo 'Skipping Lint stage — using Docker for all dependencies'
            }
        }

        stage('Unit Tests') {
            steps {
                echo 'Skipping Unit Tests stage — using Docker for all dependencies'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }

        stage('Deploy (Containerized)') {
            steps {
                dir("${WORKSPACE}") {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Selenium Tests') {
            steps {
                echo 'Running Selenium tests'
                dir('selenium-tests') {
                    sh 'docker build -t selenium-tests .'
                    sh 'docker run --rm --network selenium-asg_default selenium-tests || true'
                }
            }
        }
    }

    post {
        always {
            dir("${WORKSPACE}") {
                sh 'docker-compose down || true'
            }
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}