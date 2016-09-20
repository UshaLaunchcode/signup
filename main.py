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
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
   return not email or EMAIL_RE.match(email)

user_input="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    <body>
    <h1>Signup</h1>
        <form action="/formdata" method="post">
            <label for="username">Username</label>
            <input name="username" type="text">
            <br>
            <label for="password">Password</label>
                <input name="password" type="password" >
                <br>
            <label for="verify">Verify Password</label>
                <input name="verify" type="password" >
                <br>
            <label for="email">Email (optional)</label>
                <input name="email" type="text" value="" optional>
                <br>
            <input type="submit">
        </form>
    </body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(user_input)


class verification(webapp2.RequestHandler):
    #def get(self):
        #self.response.write(user_input)
        #username=self.request.get('username')
        #def post()
    def post(self):
        #have_error = False
        #username = self.request.get('username')
        have_error = False

        input_username = self.request.get('username')
        input_password = self.request.get('password')
        input_verify = self.request.get('verify')
        input_email = self.request.get('email')
        #self.response.out.write("Hello " + username +"!")
        user_username = valid_username(input_username)
        user_password = valid_password(input_password)
        user_verify =  valid_password(input_verify)
        user_email = valid_email(input_email)
        #    welcome_message = "Welcome, " +user_username+ "!"
        #    self.response.write(welcome_message)
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        if not user_username:
            error_username = "Please enter a valid username"
            have_error = True
        if not user_password:
            error_password = "Please enter a valid password"
            have_error = True
        if input_password != input_verify:
            error_verify = "Your passwords do not match"
            have_error = True
        if not user_email:
            error_email = "Please enter a valid email"
            have_error = True

        if have_error:

            user_input="""
            <!DOCTYPE html>
            <html>
                <head>
               </head>
               <body>
               <h1>Signup</h1>
                   <form action="/formdata" method="post">
                       <label for="username">Username</label>
                       <input name="username" type="text" value="{0}">{1}
                       <br>
                       <label for="password">Password</label>
                           <input name="password" type="password" >{2}
                           <br>
                       <label for="verify">Verify Password</label>
                           <input name="verify" type="password" >{3}
                           <br>
                       <label for="email">Email (optional)</label>
                           <input name="email" type="text" value="" optional>{4}
                           <br>
                       <input type="submit">
                   </form>
               </body>
            </html>
            """.format(input_username,error_username, error_password, error_verify, error_email)
            self.response.write(user_input)

        else:
            self.response.out.write("Welcome, " +str(input_username)+ "!")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/formdata', verification)
], debug=True)
