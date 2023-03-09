# Django Item Marketplace App
<p>This is a Django web application for a simple item marketplace, where users can browse, search, create, edit and delete items, as well as start and participate in conversations about specific items.</p>Features
<ul>
 <li>User authentication and authorization (using Django's built-in authentication system)</li>
 <li>Dashboard page that displays all items created by the currently logged-in user</li>
 <li>Items page that displays all items available for sale, with the ability to search and filter by category</li>
 <li>Item detail page that displays the details of a specific item and up to 3 related items in the same category</li>
 <li>Ability for logged-in users to create, edit and delete their own items</li>
 <li>Conversations system that allows users to start and participate in conversations about specific items</li>
 <li>Inbox page that displays all conversations involving the currently logged-in user</li>
</ul>Technologies
<ul>
 <li>Python 3.7</li>
 <li>Django 3.2</li>
 <li>PostgreSQL 12 (as the database backend)</li>
 <li>Tailwind CSS (as the CSS framework)</li>
</ul>Installation
<ol>
 <li>Clone the repository:</li>
</ol>
<pre><span></span><code>git <span>clone</span> https://github.com/username/repo.git
</code></pre>
<ol>
 <li>Install the dependencies:</li>
</ol>
<pre><code>pip install -r requirements.txt
</code></pre>
<ol>
 <li><p>Create a PostgreSQL database and update the <code>DATABASES</code> setting in <code>settings.py</code> to use your database credentials.</p></li>
 <li><p>Apply the database migrations:</p></li>
</ol>
<pre><code>python manage.py migrate
</code></pre>
<ol>
 <li>Create a superuser account:</li>
</ol>
<pre><code>python manage.py createsuperuser
</code></pre>
<ol>
 <li>Run the server:</li>
</ol>
<pre><code>python manage.py runserver
</code></pre>
<ol>
 <li>Access the web application in your browser at <code>http://localhost:8000/</code>.</li>
</ol>Usage
<ul>
 <li>To view all available items, go to the Items page (<code>/item/items/</code>).</li>
 <li>To view the details of a specific item, click on its title.</li>
 <li>To create a new item, go to the New Item page (<code>/item/new/</code>) and fill out the form.</li>
 <li>To edit or delete an existing item, go to its detail page and click on the Edit or Delete button.</li>
 <li>To view all conversations involving you, go to the Inbox page (<code>/conversation/inbox/</code>).</li>
 <li>To start a new conversation about a specific item, go to its detail page and click on the Start Conversation button.</li>
 <li>To participate in an existing conversation, go to its detail page and fill out the message form.</li>
</ul>Credits
<p>This web application was created as part of Learn Django by Building a Marketplace course with slightly modified CSS to give pages a neater look.</p>
