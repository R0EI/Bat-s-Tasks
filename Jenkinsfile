pipeline{
    
    agent any

    options {
        timestamps() 
    }

    environment {
       AWS_ACCOUNT_ID= "644435390668"
       AWS_DEFAULT_REGION="eu-west-3"
       IMAGE_REPO_NAME= "roei"
       IMAGE_TAG= "latest"
    }

    stages{
        stage("Init"){
            steps{
                deleteDir()
                checkout scm

            }
        }   

        stage("Build APP") {
            steps {
                script{
                    sh "docker build -f Dockerfile.app -t ${IMAGE_REPO_NAME} ."
                }
            }
        }

        stage("Test App container") {
               steps {
                   sh """
                    docker-compose build -f docker-compose.yml --no-cache
                    docker-compose -f docker-compose.yml up -d 
                    sleep 10
                    curl 13.38.82.108:80
                """
           }
        }

        stage("E2E Test") {
            steps{
                sh """
                chmod 777 test/test.sh
                ./test/test.sh
                cat score.txt
                docker-compose -f docker-compose.yml down -v
                """
            }
        }

        stage("Tagging commit and tags"){
            when {
                branch 'main'
            }
            steps{
                script{
                    env.GIT_COMMIT_MSG = sh(script: "git log -1 --pretty=%B ${env.GIT_COMMIT}", returnStdout: true).trim()
                    if(GIT_COMMIT_MSG.contains("version")){
                        withCredentials([gitUsernamePassword(credentialsId: "94c3e575-d774-4321-8b7b-7f3544ee446e", gitToolName: 'Default')]){
                            Ver_Calc=sh(script: "bash tag_calc.sh ${GIT_COMMIT_MSG}",returnStdout: true).trim()
                            New_tag=Ver_Calc.split("\n").last()
                            echo "${New_tag}"
                            sh  """                          
                                git tag ${New_tag}
                                git push origin ${New_tag}
                                git fetch
                                """
                        }
                    }
                }
            }
        }

        stage("Push to ECR") {
            steps {
                script{
                    env.GIT_COMMIT_MSG = sh(script: "git log -1 --pretty=%B ${env.GIT_COMMIT}", returnStdout: true).trim()
                    if(GIT_COMMIT_MSG.contains("version")){
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: "aws-jenkins",
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                        ]]) {
                            sh "aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 644435390668.dkr.ecr.eu-west-3.amazonaws.com"
                            sh "docker tag ${IMAGE_REPO_NAME} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${New_tag}"
                            sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${New_tag}"
                        }
                    }
                }
            }
        }

        stage("Deploy App") {
           steps {    
               //prod 1
               sh """
               ./transfer.sh "13.38.30.68" ${New_tag}
               """
           }
        }
    }
}