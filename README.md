# car-repo-site
Project for cs2300

Standard Git Procedure:
1. Checkout your own branch and code on your own personal branch.
2. Once you are done coding and ready to share commit and push your changes to your branch.
3. Checkout development branch.
4. Pull down other changes that others have committed before sharing your changes.
5. Merge your branch into development branch.
6. Resolve merge conflicts, if any.
7. Next use Ctrl+Shift+K to push your changes up on development branch.
8. Switch back to your own branch.
9. Merge development branch onto your own branch to pick up other peoples changes without merge conflicts.

Useful PyCharm Commands:
1. Use Ctrl+Shift+U to reverse the case of every letter in a word. Useful for making constants.
2. Use Ctrl+F to open a search window to find certain terms in a file.  Use Ctrl+Shift+F to search throughout the project.
3. Use Ctrl+R to find and replace a term in a file.  Use Ctrl+Shift+R to replace terms throughout the project.
4. Use Alt+Click to produce multiple cursors.  Alt+Click+Drag will produce one huge multiple line cursor.
5. Use Ctrl+Y to delete an entire line.
6. Use Ctrl+/ to comment a highlighted section of code.
7. Use Ctrl+Shift+K to push your committed code to git.
8. Use del to delete files automatically and safely.

Useful Terminal Commands:
1. Use <code>python manage.py makemigrations</code> to tell Django your model changes and get them ready to integrate into the database.
2. Use <code>python manage.py migrate</code> to integrate all changes recorded in the <code>makemigrations</code> command into our database.
3. Use <code>python manage.py runserver</code> to start a localhost:8000 server that will run the current projects code.
4. Use <code>python manage.py test</code> to run any automated tests that have been written in the project.
5. Use <code>python manage.py createsuperuser</code> to create an admin account that can help create database objects very quickly.
6. Use <code>python manage.py startapp <app_name></code> to start a new app with its name being equivalent to <app_name>
7. Use tab to autocomplete file names.
8. You can do most of the above commands on one app if you like instead of the whole project.
9. Use <code>pip install <package_name></code> to install a package of a given name.
10. Use <code>pip install -r requirements.txt</code> to install packages in the requirements.txt file.
11. Add the <code>-U</code> flag to the command in #9 to upgrade a package.
12. Use <code>pip uninstall <package_name></code> to uninstall a given package.

Coding Conventions:
1. Use single quotes for all strings, unless the string has a single quote in it.  It is then okay to use a double quote for strings.
2. Use a doc string to document all files and functions.  Doc strings are denoted with three double quotes.
3. Follow PEP-8 guidelines.  Pretty much fix the weak warnings PyCharm will throw in our code.
4. Use <code>import ipdb; ipdb.set_trace()</code> in your code to debug.

Jinja Templating:
1. You can do everything that you can do in a normal HTML5 file, but there are a few useful things extra with Jinja.
2. Use <code>{{ }}</code> to reference a variable passed to the HTML from the context in a render function.
3. Use <code>{% %}</code> to use python like logic in the HTML.

Useful Links:
1. PEP-8 Guidelines: <a>https://www.python.org/dev/peps/pep-0008/</a>
2. Django Docs: <a>https://docs.djangoproject.com/en/2.0/</a>
3. Python Docs: <a>https://docs.python.org/3/</a>
