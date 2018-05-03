from bs4 import BeautifulSoup
import requests
import pickle
from time import sleep

class Coin():
	def __init__(self,name,code,market,active):
		self.name = name
		self.code = code
		self.market = market
		self.active = active
		self.github = ""
		self.website =""
		self.explorer1 = ""
		self.explorer2 = ""
		self.forum = ""
		self.announcement = ""
		self.commits = ""
		self.branches = ""	
		self.releases = ""
		self.contributors = ""
		self.opened_issues = ""
		self.closed_issues = ""


	def url_item(self):
		return f"{self.code}/{self.market}"

	def set_github(self,github):
		self.github = github

	def set_website(self,website):
		self.website = website

	def set_explore1(self,explorer1):
		self.explorer1 = explorer1

	def set_explore2(self,explorer2):
		self.explorer2 = explorer2

	def set_forum(self,forum):
		self.forum = forum

	def set_announcement(self,announcement):
		self.announcement = announcement

	def set_branches(self, branches):
		self.branches = branches

	def set_commits(self,commits):
		self.commits = commits

	def set_releases(self,releases):
		self.releases = releases

	def set_contributors(self,contributors):
		self.contributors = contributors

	def set_github_info(self,commits,branches,releases,contributors):
		self.commits = commits
		self.branches = branches
		self.releases = releases
		self.contributors = contributors

	def set_github_issue_info(self,opened_issues,closed_issues):
		self.opened_issues = opened_issues
		self.closed_issues = closed_issues

	def __str__(self):
		return "\t".join(list(self.__dict__.values()))