import  unittest

from tests.test_basics import  BasicsTestCase
from tests.test_user_model import UserModelTestCase

basictest = BasicsTestCase()
usermodeltest = UserModelTestCase()

if __name__ =='__main__':
    unittest.main()