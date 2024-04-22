from dotenv import load_dotenv
from datetime import datetime
import os
import git

load_dotenv()
path = os.getenv('REPO')

repo = git.Repo(path)
origin = repo.remote(name='origin')

origin.pull()