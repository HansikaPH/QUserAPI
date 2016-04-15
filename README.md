QUserAPI
======


An API to extract information from Quora User Profiles.

## Table of Contents

* [Features](#features)
* [Usage](#usage)
* [Todo](#todo)
* [Contributing](#contributing)

# Features

* Quora Profile Name
* Quora Profile Picture Link
* Quora Profile URL
* Number of Questions
* Number of Answers
* Number of Followers
* Number of Following
* Number of Edits

# API Usage
### API Base URL: `http://quser-api.herokuapp.com/`

Result :
```json
{
  "author": "Hansika Hewamalage", 
  "base_url": "quser-api.herokuapp.com", 
  "endpoints": {
    "Number of Answers": "/profile/number/answers/{user_name}", 
    "Number of Edits": "/profile/number/edits/{user_name}", 
    "Number of Followers": "/profile/number/followers/{user_name}", 
    "Number of Following": "/profile/number/following/{user_name}", 
    "Number of Questions": "/profile/number/questions/{user_name}", 
    "Quora Profile Name": "/profile/name/{user_name}", 
    "Quora Profile Picture Link": "/profile/picture_link/{user_name}", 
    "Quora Profile URL": "/url/{user_name}"
  }, 
  "project_issues": "https://github.com/hansika/QUserAPI/issues", 
  "project_name": "QUserAPI", 
  "project_url": "https://github.com/hansika/QUserAPI"
}
```

### GET: `/profile/name/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/name/Tapasweni-Pathak`

Example result:
```json
{
  "profile_name": "Tapasweni Pathak"
}
```

### GET: `/profile/picture_link/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/picture_link/Tapasweni-Pathak`

Example result:
```json
{
  "profile_picture_link": "https://qph.cr.quoracdn.net/main-thumb-5489960-200-betrgtobgepblvqkfadwafpzwbnbuntt.jpeg"
}
```

### GET: `/url/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/url/Tapasweni-Pathak`

Example result:
```json
{
  "url": "https://www.quora.com/profile/Tapasweni-Pathak"
}
```

### GET: `/profile/number/questions/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/number/questions/Tapasweni-Pathak`

Example result:
```json
{
  "no_of_questions": "103"
}
```

### GET: `/profile/number/answers/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/number/answers/Tapasweni-Pathak`

Example result:
```json
{
  "no_of_answers": "432"
}
```

### GET: `/profile/number/followers/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/number/followers/Tapasweni-Pathak`

Example result:
```json
{
  "no_of_followers": "3,820"
}
```

### GET: `/profile/number/following/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/number/following/Tapasweni-Pathak`

Example result:
```json
{
  "no_of_following": "190"
}
```

### GET: `/profile/number/edits/<user_name>`
#### Example
Example usage: `GET http://quser-api.herokuapp.com/profile/number/edits/Tapasweni-Pathak`

Example result:
```json
{
  "no_of_edits": "4,346"
}
```

# Todo
* Facebook Profile Link
* Twitter Link
* Wordpress Link
* LinkedIn Link


####Note : This parses [Quora](https://www.quora.com/) unofficialy.
