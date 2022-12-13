import time
import os

from github import Github

github_secret = os.environ['GHSECRET']
this_repo = os.environ['REPO']


def main():

    token = Github(github_secret) # FIXME
    source_repo = token.get_repo('graphics80/IssueCopy') # FIXME
    target_repo = token.get_repo(this_repo) # FIXME
    source_issues = source_repo.get_issues(state='open', sort='created', direction='asc')
    target_issues = target_repo.get_issues(state='open', sort='created', direction='asc')
    for issue in source_issues:
        if not issue_exists(target_issues, issue.title):
            target_repo.create_issue(
                issue.title,
                issue.body
            )
            print(issue.title)
            time.sleep(5)


def issue_exists(target_issues, title):
    for issue in target_issues:
        if issue.title == title:
            return True
    return False


if __name__ == '__main__':
    main()
