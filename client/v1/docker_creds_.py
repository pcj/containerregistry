# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This package exposes credentials for talking to a Docker registry."""



from containerregistry.client import docker_creds


class Token(docker_creds.SchemeProvider):
  """Implementation for providing a transaction's X-Docker-Token as creds."""

  def __init__(self, token):
    super(Token, self).__init__('access_token')
    self._token = token

  @property
  def suffix(self):
    return self._token
