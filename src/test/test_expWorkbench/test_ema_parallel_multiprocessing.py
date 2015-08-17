'''
Created on 28 sep. 2011

.. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
'''
import mock
import unittest


from expWorkbench import ModelStructureInterface, ema_parallel_multiprocessing


class MockMSI(ModelStructureInterface):

    def run_model(self, case):
        ModelStructureInterface.run_model(self, case)

    def model_init(self, policy, kwargs):
        ModelStructureInterface.model_init(self, policy, kwargs)

class EMAParallelTestCase(unittest.TestCase):
    
    @mock.patch('expWorkbench.ema_parallel_multiprocessing.os')
    @mock.patch('expWorkbench.ema_parallel_multiprocessing.shutil')
    @mock.patch.object(ema_parallel_multiprocessing.CalculatorPool, '_get_worker_name')
    def test_init(self, mock_get_worker_name, mock_shutil, mock_os):
        
        mockMSI = mock.Mock(spec=MockMSI)
        mockMSI.name = 'test'

        # set some proper return values on mocked methods and functions
        mock_get_worker_name.return_value = "workername"
        mockMSI.working_directory = '.'
        mock_os.path.abspath.return_value = '/Domain/model'
        mock_os.path.dirname.return_value = '/Domain'
        
        # instantiate the pool
        pool = ema_parallel_multiprocessing.CalculatorPool([mockMSI], processes=2)
        
        
        # assert whether the init is functioning correctly
        self.assertEqual(len(pool._pool), 2, "nr. processes not correct")
        self.assertEqual(mock_os.path.dirname.call_count, 1,
                         "os.dirname called too frequent")
        
        mock_os.path.join.assert_called_with("/Domain", "workernametest")

# worker

# CalculatorPool

# EMAApplyResults

# SubProcessLogHandler

# LogQueueReader

# LoggingProcess


if __name__ == '__main__':
    unittest.main()
    