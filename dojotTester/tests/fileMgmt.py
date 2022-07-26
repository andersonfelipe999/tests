from common.base_test import BaseTest
from dojot.api import DojotAPI as Api
import json
from common.testutils import *
from dojotTester import ROOT_DIR

class UploadFileHTML(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        
        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.html"

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileWithoutHeader(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for upload of file without header
        rc, res = Api.upload_file_without_header(self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 401, "Error in Status Code")

class UploadFileWithTokenEmpty(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):

        self.jwt=''

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses     
        self.assertTrue(int(rc) == 401, "Error in Status Code") 


class UploadUnsupportedMediaType(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file_with_contentType(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")

  

class UploadFile(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        self.logger.info('Teardown executed!')
        super().tearDown()

class RemoveFilePathWithTokenInvalid(BaseTest):

    def setUp(self):
        super().setUp()

        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('path: ' + str(self.path))
        self.jwt = 'eyJ0eXjlIjoiYWRtaW4ifQ.bX1UHckm-fcwTFh7ixLbjKKWUbh-9eFLCRHbal86cAS' 
        
        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 401, "Error in Status Code")


class RemoveFilePathWithoutToken(BaseTest):

    def setUp(self):
        super().setUp()

        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('path: ' + str(self.path))
        self.jwt = '' 
        #Calling method for remove of file    
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses  
        self.assertTrue(int(rc) == 401, "Error in Status Code")



class UploadFilePathLessThanLowerLimit(BaseTest):

    def setUp(self):
        super().setUp()

        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = "ab"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class UploadFilePathGreaterThanUpperLimit(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = "abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi10"

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class UploadFileWithNameInvalid(BaseTest):

    def setUp(self):
        super().setUp()

        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = "/.tmp/"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 400, "Error in Status Code")

class RemoveFileSizePathEquals100(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi1"

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        
		
        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))


class RemoveFileWithValueInvalid(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))
        self.path = '/.tmp/'
		
        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(rc == 400, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))

        self.path = "arquivos/arquivo.txt"
        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))

        self.logger.info('Teardown executed!')
        super().tearDown()

class RemoveFileLessThanLowerLimit(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.path = "ab"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(int(rc) == 400, "codigo inesperado")



    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class RemoveFilePathGreaterThanUpperLimit(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.path = "abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi10"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for remove of file  
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses 
        self.assertTrue(int(rc) == 400, "Error in Status Code")


    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class RemoveFileWithMinimumSize(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.path = "abc"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 404, "Error in Status Code")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()
class RemoveFileNotExistent(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.path = "naoExiste"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 404, "Error in Status Code")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileWithoutPath(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = ""

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses 
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class ListStoredFiles(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        file = ROOT_DIR + "/" + "resources/files/lana.jpg"

        self.logger.info('file: ' + str(file))

        self.path = "imagens/lana.jpg"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        self.logger.info('Setup executed!')


    def runTest(self):
        self.logger.info('Executing test...listing stored files')

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 10)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")



    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


class RemoveStoredFile(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Setup executed!')

        #Calling method for list of file 
        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "videos/teste.mp4"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...removing stored file')

        #Calling method for remove of file  
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")



class DownloadTextFile(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(file))

        self.path = "arquivos/arquivo.txt"
        self.filename = "arquivo.txt"

        #Calling method for list of file 
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")


        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


class RemoveFilePathNameInvalid(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(file))

        self.path = "arquivos/arquivo.txt"
        self.filename = "arquivo.txt"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file    
        rc, res = Api.remove_stored_file_parameter(self.jwt, 'remove?pathDelete=arquivos/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")

        self.logger.info('runTest executed!')


class RemoveFileIncompleteCommand(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(file))

        self.path = "arquivos/arquivo.txt"
        self.filename = "arquivo.txt"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file  
        rc, res = Api.remove_stored_file_parameter(self.jwt, 'remove')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class DownloadImageFile(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/lana.jpg"

        self.logger.info('file: ' + str(file))

        self.path = "images/lana.jpg"
        self.filename = "lana.jpg"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file  
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadSoundFile(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/musica1.mp3"

        self.logger.info('file: ' + str(file))

        self.path = "sounds/musica.mp3"
        self.filename = "musica.mp3"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadVideoFile(BaseTest):


    def setUp(self):
        super().setUp()
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "video/video.mp4"
        self.filename = "video.mp4"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


class ListFileLimitTen(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.list_stored_files(self.jwt, 13)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class ListFileLimitThree(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 3)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class DownloadFileParameterValueInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=teste')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class DownloadFileWithoutJwtInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        self.jwt='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJtTE8ySVMzUlNzclYzeno4Wm9LeFB1b01ENGJjaVZJaSIsImlhdCI6MTY1NTMxNDEzMSwiZXhwIjoxNjU1MzE0NTUxLCJwcm9maWxlIjoiYWRtaW4iLCJncm91cHMiOlsxXSwidXNlcmlkIjoxLCJqdGkiOiIyODFmMjYzZDMyN2JhMDkxMjhlNDA5MDI2YzkzMGIxNyIsInNlcnZpY2UiOiJhZG1pbiIsInVzZXJuYW1lIjoiYWRtaW4ifQ.FhOwpMJfa2jEYAoit9guroV8TiqN5SqeKkdsWnyRKFc'
        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=midia&path=docs/arquivo.txt')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 401, "Error in Status Code")

class DownloadFilePathNonexistent(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url&path=xxx/arquivo.txt')
        self.logger.info('Result: ' + str(res))

        self.assertTrue(int(rc) == 404, "Error in Status Code")



class Upload_FileTxt(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")


        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for list of file 
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
         #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileMd5InvalidValue(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file_with_md5(self.jwt, self.file, self.path, 'xxxd8cd98fghb204e9800998ecf8427e')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class UploadFileMd5(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file_with_md5(self.jwt, self.file, self.path, '2ad11810b5d7c6f54f139c2d53fb637e')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        self.logger.info('Teardown executed!')
        super().tearDown()


class UploadFileWithoutBody(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file_without_body(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class UploadFileMd5Empty(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file_with_md5(self.jwt, self.file, self.path, '')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        self.logger.info('Teardown executed!')
        super().tearDown()

class DownloadUrlExternalFile(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url&path=docs/arquivo3.txt')
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.logger.info('Result: ' + str(res))

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class ListFileLimitAll(BaseTest): 
 
    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"
        self.logger.info('file: ' + str(self.file))
        self.path = "arquivos/arquivo.txt"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        
        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo1.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "imagens/arquivo.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/teste.mp4"
        rc, res = Api.upload_file(self.jwt, self.file, "videos/teste.mp4")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('Setup executed!')


    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.list_stored_files(self.jwt, 5)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
    
    def tearDown(self):

        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, 'arquivos/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo1.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'imagens/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        rc, res = Api.remove_stored_file(self.jwt, 'videos/teste.mp4')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class ListFileLimitTwenty(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 20)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class ListFilesPaginateGreatThanLimit(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 9)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class ListFileTextWithValue(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, "list?limit=10&pathPrefix=/docs/arquivo1.txt")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)
        

class ListFileVideoByPrefix(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, "list?limit=10&pathPrefix=/videos")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class DownloadImagem(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/lana.jpg"

        self.logger.info('file: ' + str(file))

        self.path = "docs/lana.jpg"
        self.filename = "lana.jpg"

        #Calling method for search of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses 
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


class DownloadVideo(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "videos/teste.mp4"
        self.filename = "teste.mp4"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class ListFileSom(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()

        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/musica1.mp3"

        self.logger.info('file: ' + str(file))

        self.path = "sounds/musica1.mp3"
        self.filename = "musica1.mp3"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")


        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)
        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for list file
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=10&pathPrefix=/sounds')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code") 


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
        #Calling method for remove file
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()


      
class ListFileFilterLimit(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5&pathPrefix=/docs')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class ListFileStartAfter(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')


    def runTest(self):
        self.logger.info('Executing test...')
        
        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&startAfter=/docs/arquivo1.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")


    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class ListFileAllFilters(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&pathPrefix=/docs&startAfter=/docs/arquivo2.txt')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)



class ListLastFile(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=2&startAfter=docs/testes.txt')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class ListNoFileInBucket(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class DownloadFileParameterInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?attr=media&path=docs/arquivo.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")



class DownloadFileWithoutParameterAlt(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"
        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?path=docs/arquivo.txt')
        self.logger.info('Result: ' + str(res))


        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
    def tearDown(self):
        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        

class DownloadFileWithoutParameterPath(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class DownloadFileWithoutToken(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_stored_files_without_token(self.jwt, 'download?alt=media')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 401, "Error in Status Code")




class DownloadPathNotExist(BaseTest): 
    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path="tes')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")

class DownloadFilePathInvalid(BaseTest): 
    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path="/xxx/arquivo.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")



class DownloadFilePathIncomplete(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path="arquivo.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")



class DownloadFIlePathLessThanThree(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path="ab')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "Error in Status Code")



class DownloadFIlePathGreaterThanOneHundred(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path=abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi100"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class DownloadFileNotExist(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")

class GetFileValueInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path=abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi1"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code") 



class DownloadFileWordReserved(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=media&path=/.tmp/"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 



class DownloadFileNameParameterInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url&caminho=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 


class DownloadFileParameterAltInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=xxx&path=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 

       
class DownloadFileIncompleteCommand(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 

class DownloadFileWithoutTokenJwt(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.download_files_with_path('', 'download?alt=url&path=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 401, "Error in Status Code") 

class DownloadFileNonexistent(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        
        #Calling method for list of file 
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url&path=/docs/teste.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")


class DownloadFilePathNonexistent(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.download_files_with_path(self.jwt, 'download?alt=url&path=xxx/arquivo.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")


class ListFileLimitTenFiles(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 10)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

    

class DownloadFileSoundMp3(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/musica1.mp3"

        self.logger.info('file: ' + str(file))

        self.path = "sounds/musica1.mp3"
        self.filename = "musica1.mp3"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses   
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        


        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)
        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while retrieving file " + str(self.path))

        self.logger.info('Teardown executed!')
        super().tearDown()


class Utility(BaseTest): 

    def UploadSeveralFiles(self):
        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.txt"

        self.logger.info('Setup executed!')
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        
        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo1.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "imagens/arquivo.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/teste.mp4"
        rc, res = Api.upload_file(self.jwt, self.file, "videos/teste.mp4")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/lana.jpg"
        rc, res = Api.upload_file(self.jwt, self.file, "docs/lana.jpg")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/musica1.mp3"
        rc, res = Api.upload_file(self.jwt, self.file, "sound/musica1.mp3")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"
        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo.html")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"
        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo2.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "docs/arquivo3.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        rc, res = Api.upload_file(self.jwt, self.file, "docs/testes.txt")
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")


    def RemoveSeveralFiles(self):
        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, 'arquivos/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo1.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo2.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo3.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/testes.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/lana.jpg')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'sound/musica1.mp3')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'docs/arquivo.html')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'imagens/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        rc, res = Api.remove_stored_file(self.jwt, 'videos/teste.mp4')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class ListThreeLastFiles(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.list_stored_files(self.jwt, 3)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)

class ListFileFilterPathPrefixInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3&pathPrefix=/invalido')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class ListFileFilterStartAfterInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Upload several files
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3&startAfter=invalido')

        self.logger.info('Result: ' + str(res))

        #Validation of responses  
        self.assertTrue(int(rc) == 200, "Error in Status Code")
    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)


class ListFileLimitEmpty(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Start Testing
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")



class ListFileLimitZero(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=0')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")



class ListFileLimitLessThanZero(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=-3')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class ListFileLimitPrefixInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for list of file 
        rc, res = Api.list_file_parameter(self.jwt, 'list?limit=3&pathPrefix=/invalido')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)



class ListFileLimitNotInteger(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=X')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
 



class ListFileLimitWithDoubleValue(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3.1')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")



class ListFileThereIsNotData(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Calling method for upload of file
        Utility.UploadSeveralFiles(self)
        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for list of file
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3&pathPrefix=/automacao"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")
       

    def tearDown(self):
        #Calling method for remove several file
        Utility.RemoveSeveralFiles(self)



class ListStartFileDoesNotExist(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=2&startAfter=test%2Fsample_4.txt"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")





class ListFileInvalidName(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo.html"
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&startAfter=teste$#@!%&*"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))


class UploadFileJWTInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = 'eyJ0eXAiOiJKV1QoRaGNZa'
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        self.logger.info('Executing test...')
        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.html"

        self.logger.info('file: ' + str(self.file))
        self.path = "arquivos/arquivo.html"

        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 401, "Error in Status Code")



class ListFileTokenJWTEmpty(BaseTest): 

    def runTest(self):
        self.jwt = ''
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3"')
        self.logger.info('Result: ' + str(res))
        
        #Validation of responses  
        self.assertTrue(int(rc) == 401, "Error in Status Code")




class ListWithoutFileInTheBucket(BaseTest): 
    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self): 
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5')
        self.logger.info('Result: ' + str(res))
        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")


