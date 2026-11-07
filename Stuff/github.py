import requests
import json

with open('github_stats.json.txt') as file:
    github = json.load(file)

def save():
    with open('github_stats.json.txt', 'w') as file:
        json.dump(github, file, indent=4)

def git():
  while True:
    username = input('What is the username? ')
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    data = response.json()
    try:
     response = requests.get(url)
     response.raise_for_status()
     data = response.json()
    except requests.exceptions.HTTPError as err:
     print(f'HTTP error occured {err}')
    except requests.exceptions.ConnectionError:
     print('failed to connect please check your internet connection!')
    except requests.exceptions.ConnectTimeout:
     print('The request timed out!')
    identification = data["id"]
    followers = data["followers"]
    email = data["email"]
    company = data["company"]
    bio = data["bio"]
    

    github[username] = {
        "identification": identification,
        "followers": followers,
        "email": email,
        "company": company,
        "bio": bio
    }
    save()
    print(f'Successfully added {username}')
    break


def view():
 while True:
   from pprint import pprint
   viewing = input('What user would you like to view? (or all) ')
   if viewing in github:
      print(f'Now viewing the profile of {viewing}:')
      pprint(github[viewing])
      break
   elif viewing.lower() == 'all':
     pprint(github)
     break
   else:
      print('Not a valid result, please try again!')
      break

def change():
 while True:
   changing = input('Would you like to (remove) or (change) a user ')
   if changing.lower() == 'change':
    changing2 = input('Which user would you like to change? ')
    if changing2 in github:
      del github[changing2]
      print('Now adding a new user!')
      git()
      break
    else:
      print('User not found!')
   elif changing.lower() == 'remove':
     changing3 = input('What user would you like to remove? ')
     if changing3 in github:
       del github[changing3]
       print(f'Successfully deleted {changing3}')
       break
     
     else:
      print('User not found')
   else:
    print('User not found')

while True:
 try:
  print("""----------------------------
===Github Profile Manager===
Would you like to (view), (change) or (add) a profile? (Or exit)
----------------------------""")
  choice = input('Please choose an option from above. ')
  if choice.lower() == 'add':
    git()
  elif choice.lower() == 'view':
    view()
  elif choice.lower() == 'change':
    change()
  elif choice.lower() == 'exit':
    print('Okay now exiting!')
    break
  else:
    print('Invalid choice!')
 except ValueError:
   print('Incorrect Choice')