#!/usr/bin/env python
#
#    Copyright 2008 Jeffrey William Scudder
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import sys
import os.path
import getpass
import sippycode.twitter.core as twitter
import sippycode.auth.core as auth
import base64


def get_credentialed_client():
  if os.path.exists('.twitter.creds'):
    credential_file = open('.twitter.creds', 'r')
    client = twitter.TwitterClient('', '')
    credentials = auth.BasicAuth('', '')
    credentials.basic_cookie = credential_file.read()
    client._credentials = credentials
    credential_file.close()
    return client
  else:
    return None


if __name__ == '__main__':
  client = get_credentialed_client()
  if client:
    message = ' '.join(sys.argv[1:])
    if message:
      print 'Tweeting: %s' % message
      choice = raw_input('Tweet this as %s? (y): ' % base64.decodestring(
          client._credentials.basic_cookie).split(':')[0])
      if choice.startswith('n') or choice.startswith('N'):
        print 'nevermind'
      else:
        client.update(message)
        print 'posted'
  else:
    print 'No credentials found, run login.py'
