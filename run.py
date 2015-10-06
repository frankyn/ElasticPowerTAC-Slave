#!/usr/bin/python
from DigitalOceanAPIv2.docean import DOcean
import subprocess
import json
import time
import os

'''
	main.py
		* Start simulation
		* Delete Droplet after Completion

'''


class ElasticPowerTAC_Slave:
    # constructor
    def __init__(self):
        self._config = None

        # Load config
        self.load_config()

        # store master ip
        self._docean = DOcean(self._config['api-key'])

    # load_config
    def load_config(self):
        # load from "config.json"
        try:
            config_file = "config.json"
            self._config = None
            with open(config_file, 'r') as f:
                self._config = f.read()

            self._config = json.loads(self._config)
        except:
            print('config.json must be defined.')
            exit()

    # setup slave environment
    def setup_slave_simulations(self):
        print("Slaves have been initialized!")

    # start simulation scenarios
    def start_slave_simulations(self):
        # start simulation runner
        os.chdir('/home/log/ElasticPowerTAC-Simulation')
        run_cmd = ['su', 'log', '-c', 'python simulation.py']
        subprocess.call(run_cmd)
        os.chdir('/root/ElasticPowerTAC-Slave')

    # destroy slave :)
    def clean_up(self):
        # start simulation cleanup
        # delete this slave
        print("goodbye....")
        self._docean.request_delete(self._config['droplet_id'])

if __name__ == "__main__":
    # Initialize Setup
    elastic_powertac_slave = ElasticPowerTAC_Slave()

    # Setup Simulation Environment
    elastic_powertac_slave.setup_slave_simulations()

    # Start Simulations
    elastic_powertac_slave.start_slave_simulations()

    elastic_powertac_slave.clean_up()
