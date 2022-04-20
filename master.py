import requests,os,json,urllib
from anticaptchaofficial.hcaptchaproxyless import *
from capmonster_python import HCaptchaTask
from random import randint
from time import sleep
from colorama import Fore

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")

settings = open('config.json')
config = json.load(settings)

if config['proxy'] != "":
	proxies = { "https": f"http://{config['proxy']}" }
else:
	proxies = None

tokens_type = "token"

if tokens_type.lower() != "combo":
    tokens = open("tokens.txt", 'r').read().splitlines()
    total_token = len(tokens)
else:
    tokens = open("tokens.txt", "r").read()
    total_token = len(tokens.splitlines())

headers = {
	"x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
	"sec-fetch-dest": "empty",
	"x-debug-options": "bugReporterEnabled",
	"sec-fetch-mode": "cors",
	"sec-fetch-site": "same-origin",
	"accept": "*/*",
	"accept-language": "en-GB",
	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	"TE": "trailers"
}

headers_reg = {
    "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"
}

def request_cookie():
	response1 = requests.get("https://discord.com")
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	return cookie

def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg).json()
	fingerprint = response2["fingerprint"]
	return fingerprint

def captcha_bypass(url, key):
	if config['captcha_type'] == "capmonster":
		capmonster = HCaptchaTask(config["capmonster"])
		task_id = capmonster.create_task(url, key)
		result = capmonster.join_task_result(task_id)
		response = result.get("gRecaptchaResponse")
		print(f"{Fore.LIGHTGREEN_EX} [+] Captcha solved {Fore.LIGHTBLACK_EX}({response[-32:]}){Fore.RESET}")
		return response
	else:
		solver = hCaptchaProxyless()
		solver.set_key(config["anticap"])
		solver.set_website_url(url)
		solver.set_website_key(key)
		g_response = solver.solve_and_return_solution()
		if g_response != 0:
			print(f"{Fore.LIGHTGREEN_EX} [+] Captcha bypassed {Fore.LIGHTBLACK_EX}({g_response[-32:]}){Fore.RESET}")
			return g_response

print(f'''{Fore.RED}

░░░░░██╗░█████╗░██╗███╗░░██╗███████╗██████╗░
░░░░░██║██╔══██╗██║████╗░██║██╔════╝██╔══██╗
░░░░░██║██║░░██║██║██╔██╗██║█████╗░░██████╔╝
██╗░░██║██║░░██║██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║██║░╚███║███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝{Fore.CYAN}\tMade By Tokens404.com{Fore.RESET}\n''')

invite_code = input(f"{Fore.GREEN} Please Input The Invite Code | Example: In https://discord.gg/ex404 Only Add ex404 As Input: {Fore.RESET}")
min_timeout = int(input(f"{Fore.GREEN} Random Timeout From: {Fore.RESET}"))
max_timeout = int(input(f"{Fore.GREEN} Random Timeout To: {Fore.RESET}"))
emoji_bypass = input(f"{Fore.LIGHTBLUE_EX}Would You Like To Bypass Emoji Verification? | yes/no: {Fore.RESET}")

if emoji_bypass == "yes":
	channel_id = int(input(f"{Fore.LIGHTBLUE_EX} Channel ID For Emoji Verification: {Fore.RESET}"))
	message_id = int(input(f"{Fore.LIGHTBLUE_EX} Message ID For Emoji Verification: {Fore.RESET}"))
	emoji_type = input(f"{Fore.LIGHTBLUE_EX} Emoji type (discord/nitro): {Fore.RESET}")

	if emoji_type == "discord":
		emoji_converted = input(f"{Fore.LIGHTBLUE_EX} Emoji (https://emojis.wiki/discord/) (https://www.urlencoder.io/): {Fore.RESET}")
	elif emoji_type == "nitro":
		emoji = input(f"{Fore.LIGHTBLUE_EX} Nitro (emojiname:data-id) {Fore.RESET}")
		emoji_converted = urllib.parse.quote_plus(emoji)

print(f"{Fore.YELLOW}\n [!] Loaded {total_token} Tokens.\n")

join = 0

while join < total_token:
	try:

		if tokens_type.lower() != "combo":
			token = tokens[join]
		else:
			token = tokens.split()[join].split(':')[2]

		headers["authorization"] = token
		headers["x-fingerprint"] = request_fingerprint()
		response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
		if response.status_code == 400:
			print(f"{Fore.YELLOW} [!] Captcha {token[:50]}****** detected! Solving.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{response.json()['captcha_sitekey']}{Fore.RESET})")
			response_captcha = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", json={"captcha_key": captcha_bypass("https://discord.com", f"{response.json()['captcha_sitekey']}")}, headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
			if response_captcha.status_code == 200:
				print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{invite_code}{Fore.RESET})")
				body = response_captcha.json()
				guild_id = body['guild']['id']
				if 'show_verification_form' in body:
					get_rules = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20).json()
					response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", headers=headers, cookies=request_cookie(), json=get_rules, proxies=proxies, timeout=20)
					if response2.status_code == 201 or response2.status_code == 204:
						print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** accepted the rules!{Fore.RESET}")
					else:
						print(f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not accepted the rules! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response2.content}{Fore.RESET})")
				if emoji_bypass == "yes":
					response3 = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
					if response3.status_code == 201 or response3.status_code == 204:
						print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** reacted to the emoji!{Fore.RESET}")
					else:
						print(f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** can't reacted to the emoji! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response3.content}{Fore.RESET})")

		elif response.status_code == 200:
			print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{invite_code}{Fore.RESET})")
			body = response.json()
			guild_id = body['guild']['id']
			if 'show_verification_form' in body:
				get_rules = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20).json()
				response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", headers=headers, cookies=request_cookie(), json=get_rules, proxies=proxies, timeout=20)
				if response2.status_code == 201 or response2.status_code == 204:
					print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** accepted the rules!{Fore.RESET}")
				else:
					print(f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not accepted the rules! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response2.content}{Fore.RESET})")
			if emoji_bypass == "yes":
				response3 = requests.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me", headers=headers, cookies=request_cookie(), proxies=proxies, timeout=20)
				if response3.status_code == 201 or response3.status_code == 204:
					print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** reacted to the emoji!{Fore.RESET}")
				else:
					print(f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** can't reacted to the emoji! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response3.content}{Fore.RESET})")
		else:
			print(f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response.content}{Fore.RESET})")
		time = randint(min_timeout, max_timeout)
		print(f"{Fore.LIGHTBLUE_EX} [!] Sleeping for {time} seconds.{Fore.RESET}")
		sleep(time)
		join += 1

	except Exception as err:
		print(f"{Fore.YELLOW} [!] {token[:50]}****** retrying.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{err}{Fore.RESET})")
		join = join - 1
		pass

input(f"\n{Fore.BLUE} Done! {Fore.RESET}")

# Not By Social404