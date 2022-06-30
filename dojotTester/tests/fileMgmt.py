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
        messageError = "{'message': 'Unauthorized'}"
        self.assertEquals(str(res),messageError) 

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
        messageError = "{'message': 'Unauthorized'}"
        self.assertEquals(str(res),messageError)    


class UploadFileDocumentTwo(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "docs/documento_2.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses                 
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
        #Calling method for remove of file    
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileDocumentThree(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "docs/documento_3.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for upload of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        #Validation of responses 
        self.assertTrue(int(rc) == 201, "Error in Status Code")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileDocumentOne(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "docs/documento_1.txt"

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for upload of file
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


class UploadSeveralFiles(BaseTest):

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

class RemoveSeveralFiles(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Setup executed!')

        #Putting file path
        file = ROOT_DIR + "/" + "resources/files/teste.mp4"

        self.logger.info('file: ' + str(file))

        self.path = "arquivos/arquivo.txt"


    def runTest(self):
        self.logger.info('Executing test...removing stored file')
        
        #Calling method for remove of file
        rc, res = Api.remove_stored_file(self.jwt, self.path)
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

class DeleteFilePathWithTokenInvalid(BaseTest):

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
    
        self.logger.info('path: ' + str(self.path))
        self.jwt = 'eyJ0eXjlIjoiYWRtaW4ifQ.bX1UHckm-fcwTFh7ixLbjKKWUbh-9eFLCRHbal86cAS' 
        
        #Calling method for remove of file 
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses
        self.assertTrue(int(rc) == 401, "Error in Status Code")
        self.logger.info('Teardown executed!')
        super().tearDown()

class DeleteFilePathWithoutToken(BaseTest):

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
    
        self.logger.info('path: ' + str(self.path))
        self.jwt = '' 
        #Calling method for remove of file    
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))

        #Validation of responses  
        self.assertTrue(int(rc) == 401, "Error in Status Code")
        messageError = "{'message': 'Unauthorized'}"
        self.assertEquals(str(res),messageError)
        self.logger.info('Teardown executed!')
        super().tearDown()

class UploadFileWithPathLess(BaseTest):

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

        messageError = "{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field must be between 3 and 100 characters.'}"
        self.assertEquals(str(res),messageError)

class UploadFileWithPathLarger(BaseTest):

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

        messageError = "{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field must be between 3 and 100 characters.'}"
        self.assertEquals(str(res),messageError)

class UploadFileWithInvalidPath(BaseTest):

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
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field is reserved.'}"
        self.assertEquals(str(res),messageError)

class DeleteFileWithPathInvalid(BaseTest):

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
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field is reserved.'}"
        self.assertEquals(str(res),messageError)

        self.path = "arquivos/arquivo.txt"
        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(rc == 200, "** WARNING: TEAR DOWN FAILED: Unexpected result code (" + str(rc) +
                        ") while deleting file " + str(self.path))

        self.logger.info('Teardown executed!')
        super().tearDown()

class DeleteFileSizePathLess(BaseTest):

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
        messageError = "{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field must be between 3 and 100 characters.'}"
        self.assertEquals(str(res),messageError)


    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DeleteFilePathGreterOneHundread(BaseTest):

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
        messageError = "{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field must be between 3 and 100 characters.'}"
        self.assertEquals(str(res),messageError)


    def tearDown(self):
        """
        This method will only be called if the setUp() succeeds.
        This method is called immediately after the test method has been called and the result recorded.
        This is called even if the test method raised an exception.
         """

        self.logger.info('path: ' + str(self.path))
        self.logger.info('Teardown executed!')
        super().tearDown()

class DeleteFilePathNotExist(BaseTest):

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
        messageError ="{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}"
        self.assertEquals(str(res) ,messageError)


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
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)

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
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file    
        rc, res = Api.remove_stored_file_parameter(self.jwt, 'remove?pathDelete=arquivos/arquivo.txt')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)

        self.logger.info('Teardown executed!')
        super().tearDown()


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
        #Calling method for search of file
        rc = Api.download_file(self.jwt, self.filename, self.path)

        self.logger.info('Result: ' + str(rc))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))

        #Calling method for remove of file  
        rc, res = Api.remove_stored_file_parameter(self.jwt, 'remove')
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)

        self.logger.info('Teardown executed!')
        super().tearDown()

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
        file = ROOT_DIR + "/" + "resources/files/musica3.mp3"

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

class GetFileLimitTwo(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload of file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 2)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'length': 2", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileLimitTen(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file
        rc, res = Api.list_stored_files(self.jwt, 10)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileLimitThree(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 3)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileParameterValueInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=midia&path=docs/documento_3.txt')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"alt"+"\""+" param is invalid', 'detail': 'The value of the "+"\""+"alt"+"\""+" parameter must be "+"\""+"media"+"\""+" or "+"\""+"url"+"\""+".'}"
        self.assertEquals(str(res),messageError)

        #Calling method for remove of file 
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()


class GetFileWithoutJwtInvalid(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 401, "Error in Status Code")

class GetFilePathNonexistent(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url&path=xxx/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        self.assertTrue(int(rc) == 404, "Error in Status Code")
        messageError ="{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}"
        self.assertEquals(str(res) ,messageError)


class GetWithoutFileInTheBucket(BaseTest): 
    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

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

        self.path = "arquivos/arquivo10.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        
        #Calling method for list of file 
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "Error in Status Code")
        self.assertIn('uploaded successfully.', str(res))

    def tearDown(self):

        self.logger.info('path: ' + str(self.path))
         #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn('removed successfully.', str(res))

        self.logger.info('Teardown executed!')
        super().tearDown()

class RemoveFileOne(BaseTest):

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Setup executed!')

        #Putting file path
        self.file = ROOT_DIR + "/" + "resources/files/arquivo.txt"

        self.logger.info('file: ' + str(self.file))

        self.path = "arquivos/arquivo10.txt"

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...removing stored file')

        #Calling method for search of file
        rc, res = Api.upload_file(self.jwt, self.file, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 201, "codigo inesperado")

        #Calling method for remove of file   
        rc, res = Api.remove_stored_file(self.jwt, self.path)
        self.logger.info('Result: ' + str(res) + ', ' + str(rc))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn('removed successfully.', str(res))
   

class GetUrlExternalFile(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()
        
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...')

        #Calling method for list of file
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url&path=docs/arquivo3.txt')
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.logger.info('Result: ' + str(res))

        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileLimitAll(BaseTest): 
 
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
        rc, res = Api.list_stored_files(self.jwt, 5)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class GetFileLimitTwenty(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 20)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileTextWithValue(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, "list?limit=10&pathPrefix=/docs/arquivo3.txt")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'files': [{'name': 'docs/arquivo3.txt'", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()
        




class GetFileVideoByPrefix(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for upload of file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, "list?limit=10&pathPrefix=/videos")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'files': [{'name': 'videos/teste.mp4'", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()


class GetFileJpgPath(BaseTest):

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


class GetFileMp4Path(BaseTest):

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

class GetFileSoundPath(BaseTest):

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


      
class GetFileFilterLimit(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5&pathPrefix=/docs')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'name': 'docs/arquivo.txt'", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()


class GetFileStartAfter(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()
        
        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&startAfter=/docs/arquivo1.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'name': 'docs/arquivo2.txt'", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileAllFilters(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&pathPrefix=/docs&startAfter=/docs/arquivo2.txt')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()



class GetLastFileOfList(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=2&startAfter=videos/teste.mp4')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        self.assertIn("'length': 0", str(res))

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetNoFileInBucket(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()   

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=5')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

class GetFileParameterInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'download?attr=media&path=docs/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"alt"+"\""+" param is required', 'detail': 'The "+"\""+"alt"+"\""+" param is required'}"
        self.assertEquals(str(res),messageError)


class GetFileParameterValueInvalid(BaseTest): 

    def setUp(self):
        super().setUp() 
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...permission read-only')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=midia&path=docs/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"alt"+"\""+" param is invalid', 'detail': 'The value of the "+"\""+"alt"+"\""+" parameter must be "+"\""+"media"+"\""+" or "+"\""+"url"+"\""+".'}"
        self.assertEquals(str(res),messageError)


class GetFileWithoutParameterAlt(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?path=docs/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"alt"+"\""+" param is required', 'detail': 'The "+"\""+"alt"+"\""+" param is required'}"
        self.assertEquals(str(res),messageError)


class GetFileWithoutParameterPath(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)




class GetFileWithoutToken(BaseTest): 

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
        rc, res = Api.list_stored_files_without_token(self.jwt, 'download?alt=media&path=docs/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 401, "Error in Status Code")
        self.assertTrue(str(res) == "{'message': 'Unauthorized'}", "Error in Text Response")



class GetFileNotExist(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path="/docs/testeees.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        self.assertTrue(str(res) == "{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}", "Error in Text Response")




class GetFilePathInvalid(BaseTest): 
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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path="/xxx/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        self.assertTrue(str(res) == "{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}", "Error in Text Response")


class GetFilePathIncomplete(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path="documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        self.assertTrue(str(res) == "{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}", "Error in Text Response")



class GetFilePathSmaller(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path="ab')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "Error in Status Code")



class GetFilePathLarger(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path=abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi10"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError = "{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field must be between 3 and 100 characters.'}"
        self.assertEquals(str(res),messageError)



class GetFileNotExist(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path=abc"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        self.assertTrue(str(res) == "{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}", "Error in Text Response")

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path=abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefghi1"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code") 



class GetFileWordReserved(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=media&path=/.tmp/"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is invalid.', 'detail': 'The value in the "+"\""+"path"+"\""+" field is reserved.'}"
        self.assertEquals(str(res),messageError)



class GetFileNameParameterInvalid(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url&caminho=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)


class GetFileParameterAltInvalid(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=xxx&path=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 
        messageError ="{'error': 'The " + "\""+"alt"+"\""+" param is invalid', 'detail': 'The value of the "+"\""+"alt"+"\""+" parameter must be "+"\""+"media"+"\""+" or "+"\""+"url"+"\""+".'}"
        self.assertEquals(str(res),messageError)


       
class GetFileIncompleteCommand(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code") 
        messageError ="{'error': 'The " + "\""+"path"+"\""+" field is required.', 'detail': 'The "+"\""+"path"+"\""+" field is required.'}"
        self.assertEquals(str(res),messageError)

class GetFileWithoutTokenJwt(BaseTest): 

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
        rc, res = Api.list_stored_files_without_token(self.jwt, 'download?alt=url&path=/images/lucerne.jpg"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 401, "Error in Status Code") 
        messageError ="{'message': 'Unauthorized'}"
        self.assertEquals(str(res),messageError) 

class GetFileNonexistent(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url&path=/docs/teste.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        messageError ="{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}"
        self.assertEquals(str(res) ,messageError)



class GetFilePathNonexistent(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'download?alt=url&path=xxx/documento_3.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 404, "Error in Status Code")
        messageError ="{'error': 'The file does not exist.', 'detail': 'The file does not exist.'}"
        self.assertEquals(str(res) ,messageError)


class GetFileLimitTenFiles(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_stored_files(self.jwt, 10)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

    

class GetFileSoundMp3(BaseTest):

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
        self.assertIn("File sounds/musica1.mp3 uploaded successfully.", str(res))


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
        self.assertIn("File sounds/musica1.mp3 removed successfully.", str(res))

        self.logger.info('Teardown executed!')
        super().tearDown()




class GetFileLimitThreeFiles(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')
        
        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file
        rc, res = Api.list_stored_files(self.jwt, 3)
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()

class GetFileFilterPathPrefixInvalid(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'list?pathPrefix=/docs')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)


class GetFileFilterStartAfterInvalid(BaseTest): 

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
        rc, res = Api.list_files_with_path(self.jwt, 'list?startAfter=/docs/documento_2.txt')
        self.logger.info('Result: ' + str(res))

        #Validation of responses  
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)



class GetFileLimitEmpty(BaseTest): 

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
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)


class GetFileLimitZero(BaseTest): 

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
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)




class GetFileLimitLessThanZero(BaseTest): 

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
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)


class GetFileLimitPrefixInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.get_file_parameter_list(self.jwt, 'list?limit=3&pathPrefix=/teste')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file        
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()



class GetFileLimitNotInteger(BaseTest): 

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
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)



class GetFileLimitWithDoubleValue(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3.1')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 400, "Error in Status Code")
        messageError ="{'error': 'The limit param is invalid or undefined.', 'detail': 'The limit param is required and must be a positive integer.'}"
        self.assertEquals(str(res),messageError)


class GetFileThereIsNotData(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...')
        
        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3&pathPrefix=/automacao"')
        self.logger.info('Result: ' + str(res))

        #Validation of responses   
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        messageError ="{'files': [], 'length': 0, 'nextPageStartsAfter': None}"
        self.assertEquals(str(res),messageError)

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()



class GetStartFileDoesNotExist(BaseTest): 

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
        messageError ="{'files': [], 'length': 0, 'nextPageStartsAfter': None}"
        self.assertEquals(str(res),messageError)




class GetFileInvalidName(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.logger.info('Executing test...')

        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&startAfter=docs%2Farquivo1"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        
        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=1&startAfter=docs%2Farquivo1.txt"')
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()


class GetFileJWTInvalid(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = 'eyJ0eXAiOiJKV1QoRaGNZa'
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):

        self.logger.info('Executing test...')
        #Calling method for upload several file
        classUpload = UploadSeveralFiles()
        classUpload.setUp()
        classUpload.runTest()

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3"')
        self.logger.info('Result: ' + str(res))
        #Validation of responses   
        self.assertTrue(int(rc) == 401, "Error in Status Code")

        #Calling method for remove several file
        classRemove = RemoveSeveralFiles()
        classRemove.setUp()
        classRemove.runTest()



class GetFileTokenJWTEmpty(BaseTest): 

    def setUp(self):
        super().setUp()
        #Get token 
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")

        self.logger.info('Setup executed!')

    def runTest(self):
        self.jwt = ''
        self.logger.info('Executing test...')

        #Calling method for list of file 
        rc, res = Api.list_files_with_path(self.jwt, 'list?limit=3"')
        self.logger.info('Result: ' + str(res))
        
        #Validation of responses  
        self.assertTrue(int(rc) == 401, "Error in Status Code")
        messageError ="{'message': 'Unauthorized'}"
        self.assertEquals(str(res) ,messageError)



class GetWithoutFileInTheBucket(BaseTest): 
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
        self.assertIn("'length': 0", str(res))

