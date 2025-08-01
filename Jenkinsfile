pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred') // Jenkins credentials ID
        IMAGE_NAME_ORDER = "abhinashrd/order-service"
        IMAGE_NAME_PAYMENT = "abhinashrd/payment-service"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/abhinashrd/ecommerce-devops.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${IMAGE_NAME_ORDER}", "./order-service")
                    docker.build("${IMAGE_NAME_PAYMENT}", "./payment-service")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', "${DOCKERHUB_CREDENTIALS}") {
                        docker.image("${IMAGE_NAME_ORDER}").push("latest")
                        docker.image("${IMAGE_NAME_PAYMENT}").push("latest")
                    }
                }
            }
        }
    }
}
