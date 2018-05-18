pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''cd OpenCppCoverageDemo/cmake

./build.sh
cd x64/debug
make'''
      }
    }
  }
}