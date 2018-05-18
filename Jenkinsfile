pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''cd OpenCppCoverageDemo/cmake
              chmod 777 build.sh

./build.sh
cd x64/debug
make'''
      }
    }
  }
}
