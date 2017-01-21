#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import random

class MainHandler(webapp2.RequestHandler):

    def getRandomFortune(self):

        fortune=["You will have a good future.","You cannot love life until you live the life you love.",
             "Your shoes will make you happy today.","A chance meeting opens new doors to success and friendship.","A dream you have will come true."
             "A very attractive person has a message for you.","Never give up. You're not a failure if you don't give up.","You can make your own happiness."
             "Now is the time to try something new.","Keep your eye out for someone special."]
        display=random.choice(fortune)
        return display

    def get(self):

        fortune = self.getRandomFortune()
        content = "<h1>Fortune of the Day</h1>"
        content += "<p>" + fortune + "</p>"
        self.response.write(content)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
