# Pylint Disabled Checks

In this file, certain pylint checks have been disabled for specific reasons:

- Pylint throws import errors when importing the module import 'LiveLite'. These have been disabled.
    > pylint: disable=import-error

- To accommodate test cases requiring the full path to mock, the Pylint - line length limitation has been disabled on respective test files.
    > pylint: disable=line-too-long

- Due to numerous user inputs, each test case needing individual mocking, the limitation on the number of arguments has been disabled on respective test files.
    > pylint: disable=too-many-arguments

- Few functions are being mocked with a fixed return value while defining the patch to avoid explicitly mentioning the return value. Consequently, the limitation on unused arguments has been disabled on those respective test files.
    > pylint: disable=unused-argument
