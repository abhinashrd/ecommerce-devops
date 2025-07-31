pipeline {
    agent any

    environment {
        DOCKER_IMAGE_ORDER = 'order-service:latest'
        DOCKER_IMAGE_PAYMENT = 'payment-service:latest'
    }

    stages {
        stage('Clone Repository') {
    steps {
        git url: 'https://github.com/abhinashrd/ecommerce-devops.git', branch: 'main'
    }
}


        stage('Build Docker Images') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_ORDER}", './order-service')
                    docker.build("${DOCKER_IMAGE_PAYMENT}", './payment-service')
                }
            }
        }

        stage('Run Containers') {
            steps {
                script {
                    sh 'docker-compose -f docker-compose.yml up -d'
                }
            }
        }
    }
}
