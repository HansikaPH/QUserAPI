from flask import Flask, jsonify
from scrape_quora import Scrape_Quora

app = Flask(__name__)


############################################
# Index
############################################

@app.route('/', methods=['GET'])
def index_route():
    return jsonify({
        'author': 'Hansika Hewamalage',
        'base_url': 'quser-api.herokuapp.com',
        'project_name': 'QUserAPI',
        'project_url': 'https://github.com/hansika/QUserAPI',
        'project_issues': 'https://github.com/hansika/QUserAPI/issues',
        'endpoints': {
            'Quora Profile Name': '/profile/name/{user_name}',
            'Quora Profile Picture Link': '/profile/picture_link/{user_name}',
            'Quora Profile URL': '/url/{user_name}',
            'Number of Questions': '/profile/number/questions/{user_name}',
            'Number of Answers': '/profile/number/answers/{user_name}',
            'Number of Followers': '/profile/number/followers/{user_name}',
            'Number of Following': '/profile/number/following/{user_name}',
            'Number of Edits': '/profile/number/edits/{user_name}'
        }
    })


############################################
# Profile Name & Profile Picture Link
###########################################

#Profile Name
@app.route('/profile/name/<user_name>', methods=['GET'])
def profile_name_route(user_name):
    result = Scrape_Quora.get_name(user_name)
    return jsonify(
        profile_name = result
    )

#Profile Picture Link
@app.route('/profile/picture_link/<user_name>', methods=['GET'])
def profile_picture_link_route(user_name):
    result = Scrape_Quora.get_profile_picture_link(user_name)
    return jsonify(
        profile_picture_link = result
    )

############################################
# URL
###########################################

@app.route('/url/<user_name>', methods=['GET'])
def url_route(user_name):
    result = Scrape_Quora.get_url(user_name)
    return jsonify(
        url = result
    )

############################################
# Numbers
###########################################

#Number of Questions
@app.route('/profile/number/questions/<user_name>', methods=['GET'])
def no_of_questions_route(user_name):
    result = Scrape_Quora.get_no_of_questions(user_name)
    return jsonify(
        no_of_questions = result
    )

#Number of Answers
@app.route('/profile/number/answers/<user_name>', methods=['GET'])
def no_of_answers_route(user_name):
    result = Scrape_Quora.get_no_of_answers(user_name)
    return jsonify(
        no_of_answers = result
    )

#Number of Followers
@app.route('/profile/number/followers/<user_name>', methods=['GET'])
def no_of_followers_route(user_name):
    result = Scrape_Quora.get_no_of_followers(user_name)
    return jsonify(
        no_of_followers = result
    )

#Number of Following
@app.route('/profile/number/following/<user_name>', methods=['GET'])
def no_of_questions_following(user_name):
    result = Scrape_Quora.get_no_of_following(user_name)
    return jsonify(
        no_of_following = result
    )

#Number of Edits
@app.route('/profile/number/edits/<user_name>', methods=['GET'])
def no_of_edits_route(user_name):
    result = Scrape_Quora.get_no_of_edits(user_name)
    return jsonify(
        no_of_edits = result
    )

###########################################
# Start Flask
###########################################

if __name__ == "__main__":
    app.run()