import fake_useragent


user = fake_useragent.UserAgent().random
header = {'user-agent': user}
