import webapp2


"""webapp2 on Google App Engine Python 3.7

Running as a non-GAE application as described:
https://webapp2.readthedocs.io/en/latest/tutorials/quickstart.nogae.html
"""

__author__ = 'Fili Wiese'


class HelloWebapp2(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello, webapp2!')


app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)


def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
