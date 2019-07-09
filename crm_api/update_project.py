import os, sys

old_name = 'django_starter'
new_name = sys.argv[1]


# update manage.py
try:
    with open('manage.py') as f:
        newText=f.read()
        newText=newText.replace(old_name, new_name)
    with open('manage.py', "w") as f:
        f.write(newText)
except:
    pass



# update wsgi.py
try:
    with open('django_starter/wsgi.py') as f:
        newText=f.read()
        newText=newText.replace(old_name, new_name)
    with open('django_starter/wsgi.py', "w") as f:
        f.write(newText)
except:
    pass


# update settings/base.py
try:
    with open('django_starter/settings/base.py') as f:
        newText=f.read()
        newText=newText.replace(old_name, new_name)
    with open('django_starter/settings/base.py', "w") as f:
        f.write(newText)
except:
    pass



# update folder
try:
  os.rename(old_name, new_name)
except:
  pass


print('successfully updated')