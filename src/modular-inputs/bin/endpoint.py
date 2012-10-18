import splunk.rest
import pprint

class HelloHandler(splunk.rest.BaseRestHandler):
    def handle_GET(self):
        self.response.setStatus(200)
        self.response.write("This is a test.")
        self.response.write(self.response.toXml())





