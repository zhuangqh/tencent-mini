from tornado.web import url
from handler.login_handler import LoginHandler, UserInfoHandler
routes = [
        url(r"/login", LoginHandler),
        #url(r"/song",SongNearHandler),
		#url(r"/story", StoryHandler, name='story'),
		#url(r"/story/([0-9]+)/up", PraiseHandler, name='praisestory'),
		#url(r"/story/([0-9]+)/comment", name='getcomment'),
        url(r"/userinfo",UserInfoHandler)
        ]
