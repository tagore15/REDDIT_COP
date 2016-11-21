# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

class MainPage(webapp2.RequestHandler):
    #page = "<html> <body> <form method=\"post\">REDDIT COP<br> Type keyword to search <br><input type=\"text\" name=\"search\"> </form> </body> </html>"
    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
#        self.response.write('Hello, World!')
# create forms 
        self.response.headers['Content-Type'] = 'text/html'
        #keyword = self.request.get('search')
	#print(keyword)
	import glob
	#path =r'H:\\REDDIT\\DATA\\reddit-top-2.5-million\\data\\' # use your path
	path =r'data' # use your path
	fileList = glob.glob(path + "/*.csv")
        self.response.write(str(len(fileList)))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
