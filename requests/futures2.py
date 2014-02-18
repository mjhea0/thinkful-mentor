from requests_futures.sessions import FuturesSession
import time

session = FuturesSession()
# first request is started
future_one = time.sleep(10)
# second requests is started immediately
future_two = session.get('http://httpbin.org/get?foo=bar')
# wait for the first request to complete, if it hasn't already
print "test"
# wait for the second request to complete, if it hasn't already
response_two = future_two.result()
print'response two status: {0}'.format(response_two.status_code)
print response_two.content
