# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobConstraints(Model):
    """Specifies the execution constraints for jobs created on a schedule.

    :param max_wall_clock_time: The maximum elapsed time that the job may
     run, measured from the time the job starts. If the job does not complete
     within the time limit, the Batch service terminates it and any tasks
     that are still running.
    :type max_wall_clock_time: timedelta
    :param max_task_retry_count: The maximum number of times each task may be
     retried. The Batch service retries a task if its exit code is nonzero.
    :type max_task_retry_count: int
    """ 

    _attribute_map = {
        'max_wall_clock_time': {'key': 'maxWallClockTime', 'type': 'duration'},
        'max_task_retry_count': {'key': 'maxTaskRetryCount', 'type': 'int'},
    }

    def __init__(self, max_wall_clock_time=None, max_task_retry_count=None):
        self.max_wall_clock_time = max_wall_clock_time
        self.max_task_retry_count = max_task_retry_count
