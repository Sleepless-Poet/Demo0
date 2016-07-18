import tornado.ioloop
import tornado.web
from tornado.web import url
import tornado
from tornado import httpclient


def _deco(path=''):
	def _test(func):

		def __test(*args,**kw):
			print 'path %s is visited!\n' % path
			if path == '':
				print path
			else:
				return func(*args,**kw)
		return __test
	return _test




class MainHandler(tornado.web.RequestHandler):

	class _deco1(object):

		def __init__(self):
			self.route_map = {}

		def init(self):
			pass

		def __call__(self, path, func):
			def func_wrapper(self, func):
				print 'Path %s is visited.' % path
				self.route_map[path] = func
				return func
			return func_wrapper

	deco = _deco1()

	def get(self):
		print type(self.request.headers)
		print self.request.headers
		self.write("Welcome to page /reg")


class testHandler(MainHandler):

	def __init(self):
		pass

	@MainHandler._deco1('/reg/login1')
	def test1(self):
		print "I'm /reg/login1 !"

	@MainHandler._deco1('/reg/login2')
	def test1(self):
		print "I'm /reg/login2 !"

	@MainHandler._deco1('/reg/login3')
	def test1(self):
		print "I'm /reg/login3 !"


def make_app():
    return tornado.web.Application([
        (r"/reg/login1", testHandler),
        (r"/reg/login2", testHandler),
        (r"/reg/login3", testHandler),
    ])

		

if __name__ == "__main__":
	app = make_app()
	app.listen(8892)
	tornado.ioloop.IOLoop.current().start()
