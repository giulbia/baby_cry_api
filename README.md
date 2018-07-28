# Baby cry detection - API

... TODO

[Flask 1.0 doc](http://flask.pocoo.org/docs/1.0/)

[HELLO WORLD](http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application)

[localhost 404](https://stackoverflow.com/questions/46127005/why-does-localhost5000-not-work-in-flask?rq=1)

[flask app on GCP](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env)

#### Environment variable
```
export FLASK_APP = /path/to/baby_cry_api.py
```

Then

```
flask run
```

#### Following GCP tutorial

Having trouble [setting up the virtual environment with virtualenv on MacOS](https://github.com/conda/conda/issues/1367)

The work around that worked is `conda install virtualenv`.

```
virtualenv gcp_baby_cry
source gcp_baby_cry/bin/activate
```
