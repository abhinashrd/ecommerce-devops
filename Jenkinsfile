pipeline {
    agent any

    environment {
        ORDER_SERVICE_PORT = '8001'
        PAYMENT_SERVICE_PORT = '8002'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/abhinashrd/ecommerce-devops.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                bat 'docker build -t order-service:latest order-service'
                bat 'docker build -t payment-service:latest payment-service'
            }
        }

        stage('Run Containers') {
            steps {
                bat 'docker run -d -p %ORDER_SERVICE_PORT%:8000 --name order-container order-service:latest'
                bat 'docker run -d -p %PAYMENT_SERVICE_PORT%:8000 --name payment-container payment-service:latest'
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
