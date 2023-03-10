from common.base_test import BaseTest
from dojot.api import DojotAPI as Api
import json
from common.testutils import *
from dojotTester import ROOT_DIR


class GetCredentialsWithoutBody(BaseTest): 
    """
    Get credentials without body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default values')
        rc, res = Api.get_credentials_without_body(self.jwt, "application/json")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")
        

class GetCredentialsPermissionReadOnly(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission read-only')

        data = {
            "permission": "read-only",
            "pathPrefixMatch": "*",
            "expiration": 900
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class GetCredentialsPermissionWriteOnly(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission write-only')

        data = {
            "permission": "write-only",
            "pathPrefixMatch": "/devices/*",
            "expiration": 1800
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class GetCredentialsPermissionReadWrite(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...permission read-write')
 
        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")



class GetCredentialsInvalidPermission(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid permission')

        data = {
            "permission": "all",
            "pathPrefixMatch": "*",
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


class GetCredentialsEmptyPermission(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...empty permission')

        data = {
            "permission": "",
            "pathPrefixMatch": "*",
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")

class GetCredentialsDefaultPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "Error in Status Code")


class GetCredentialsValidPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...valid pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/devices/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsPathSizeZero(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch size zero')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsPathDefaultMaximumSize(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch default maximum size (100)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2abcdefghi3abcdefghi4abcdefghi5abcdefghi6abcdefghi7abcdefghi8abcdefghi9abcdefg/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsPathMaximumSize(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch maximum size (25)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2ab/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsPathSizeGreaterMaximum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...pathPrefixMatch maximum size (30)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "/abcdefghi1abcdefghi2abcdefg/*",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

#AQUI
class GetCredentialsInvalidPath(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid pathPrefixMatch')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "-",
            "expiration": 600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsDefaultExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...default expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 900
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")



class GetCredentialsValidExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...valid expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 3600
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")

class GetCredentialsMaximumExpirationValue(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...maximum expiration value')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 31536000
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 200, "codigo inesperado")


class GetCredentialsExpirationValueLessMinimum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (899)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 899
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsExpirationValueGreaterMaximum(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (31536001)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 31536001
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")


class GetCredentialsExpirationValueText(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration value (text)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": "texto"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsExpirationValueZero(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid expiration (zero)')

        data = {
            "permission": "read-write",
            "pathPrefixMatch": "*",
            "expiration": 0
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "codigo inesperado")

class GetCredentialsUnsupportedMediaType(BaseTest): 
    """
    Request credentials with unsupported media type.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...unsupported media type (octet-stream)')
        rc, res = Api.get_credentials_without_body(self.jwt, "application/octet-stream")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 415, "codigo inesperado")

        self.logger.info('Executing test...unsupported media type (multipart/form-data)')
        rc, res = Api.get_credentials_without_body(self.jwt, "multipart/form-data")
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 415, "codigo inesperado")

class GetCredentialsInvalidSchema(BaseTest): 
    """
    Get credentials with body included.
    """

    def runTest(self):
        self.jwt = Api.get_jwt()
        self.logger.info("JWT = " + self.jwt)
        self.assertTrue(self.jwt is not None, "** FAILED ASSERTION: failure to get JWT **")
        self.logger.info('Executing test...invalid schema')

        data = {
            "permission": "read-write"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")

        data = {
           "pathPrefixMatch": "*"
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")


        data = {
            "expiration": 300
            }
        rc, res = Api.get_credentials(self.jwt, json.dumps(data))
        self.logger.info('Result: ' + str(res))
        self.assertTrue(int(rc) == 400, "Error in Status Code")



