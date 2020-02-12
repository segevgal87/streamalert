"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
from streamalert.streamquery import __version__ as streamquery_version

parameters = {
    'command_name': 'StreamQuery (Lambda) v{}'.format(streamquery_version),

    'aws_region': os.environ['REGION'],

    # Configure Logger
    'log_level': 'INFO',  # Change to DEBUG for additional verbosity

    # Configure Athena
    'athena_database': os.environ['ATHENA_DATABASE'],
    'athena_results_bucket': os.environ['ATHENA_RESULTS_BUCKET'],

    # Configure Kinesis
    'kinesis_stream': os.environ['KINESIS_STREAM'],
}
