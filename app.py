from kam import app, create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
############################################################
# START localhost virtual environment ######################
# pip install virtualenv
# virtualenv venv for python 2.7 and Windows
# python3 -m venv venv for python 3+ Mac
# source venv/bin/activate for Mac
# .\venv\Scripts\activate for Windows
# pip install -r requirements.txt for setup
# pip freeze > requirements.txt for update after pip install
# python3 app.py
############################################################

############################################################
# Flask DB commands after pip3 install migrate workflow ####
# 1) flask db init / flask db stamp head
# 2) flask db migrate -m "first migration"
# 3) flask db upgrade
# to push migrations
# 4) python3 app.py
############################################################
