from dotenv import load_dotenv
from datetime import datetime
import os
import git

today = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

load_dotenv()
path = os.getenv('REPO')

repo = git.Repo(path)
origin = repo.remote(name='origin')

message_commit = '[UPDATES] ' + today

repo.git.add('--all')
repo.index.commit(message_commit)

origin.push()