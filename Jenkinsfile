pipeline {
    // Defines where the pipeline runs. 'any' uses any available Jenkins agent.
    agent any

    // Optional: Sets environment variables for the build
    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from the specific branch that triggered the build
                checkout scm
            }
        }

        stage('Install Dependencies') {
                    steps {
                        echo 'Setting up virtual environment and installing libraries...'
                        sh '''
                        # Create a virtual environment named 'venv'
                        python3 -m venv venv

                        # Activate it and install requirements
                        source venv/bin/activate
                        # pip install -r requirements.txt
                        pip install pytest
                        '''
                    }
                }

        stage('Run Automated Tests') {
            steps {
                echo 'Executing test suite...'
                sh '''
                # Must activate the venv again in each new 'sh' block
                source venv/bin/activate
                pytest tests/ --junitxml=test-results/results.xml
                '''
            }
        }
    }

    // The post block defines actions taken after all stages complete
    post {
        always {
            // Parses the test results so you can view them in the Jenkins UI
            junit(testResults: 'test-results/*.xml', allowEmptyResults: true)
        }
        success {
            echo '✅ Pipeline succeeded. All tests passed!'
        }
        failure {
            echo '❌ Pipeline failed. One or more tests did not pass.'
        }
    }
}