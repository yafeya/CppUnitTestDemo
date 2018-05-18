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

    stage('UnitTest') {
      steps {
        sh '''cd OpenCppCoverageDemo/cmake/x64/debug/UnitTestConsole/bin
	      ./UnitTestConsole
'''
      }
    }

  }
}
