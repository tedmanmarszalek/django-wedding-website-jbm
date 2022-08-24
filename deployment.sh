# Run application using gunicorn
gunicorn bigday.wsgi

# Scale if web process is down
heroku ps:scale web=1 -a django-wedding

# Check app server logs
heroku logs --tail -a django-wedding
