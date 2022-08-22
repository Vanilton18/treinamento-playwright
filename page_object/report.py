import unittest

from HTMLTestRunner.runner import HTMLTestRunner
from test.user import UserTest

test1 = unittest.TestLoader().loadTestsFromTestCase(UserTest)
suite = unittest.TestSuite([test1])

style = """
    .heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
    border-style:ridge;
    color:white;
    background-color:gray;
    font-weight:bold;
    }
"""
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                        open_in_browser=True, description="Testes da Aplicação XPTO", tested_by="Vanilton Pinheiro",
                        add_traceback=True, style=style)
runner.run(suite)