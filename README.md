# Sorenson Impact Data Science Workspace
Get access to critical data science tools including Jupyter Notebooks, interpreters for Julia, Python, and R, and support for useful file formats such as HDF5 at the ease of one command. [Learn more](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook) about what's included. The containers also have Git configured, to make it easy to manage source files and share between colleagues.

This workspace comes with a sample World database configured. A PostgreSQL DBMS is used to interact with this database in the notebook container as seen in the `main.py` file. To use a different database, see the section about Connecting a Database.

## Using the data science workspace
1. Install Docker for your machine: https://www.docker.com/get-started
2. Clone this repository
3. Open up a terminal and change the working directory to the directory that contains `docker-compose.yml`
4. OPEN UP the `docker-compose.yml` file and find where it says **######** in the password field for the database. Replace that with **docker**
5. Run `docker-compose up` command
6. Attach the notebook container to Visual Studio Code or start working in the browser.

---
### Working in the browser
- Aftering following steps 1-4 from "Using the data science workspace", browse to http://localhost:3000 in your favorite browser
- You will be prompted for a Password or Token like this:

<img width="1440" alt="image" src="https://user-images.githubusercontent.com/29434974/157102473-422c9c0e-f2be-4e79-81ff-6f64b6d16763.png">

- A token will be provided in the terminal when you spun up the containers. To find it, look for the following lines in the terminal:
<img alt="image" src="https://user-images.githubusercontent.com/29434974/157102946-a373068f-89b9-49f2-a384-c2ed7ea948bf.png">

- Enter that token into the text box and hit Log In.
- You will be taken to the digital workspace.
- You can browse through the filesystem on the left side of the page and create new files with the building blocks provided on the right.
---
### Attaching notebook container to Visual Studio Code
- If you prefer working in an IDE environment instead of the browser, you can use Visual Studio Code.
- VS Code comes with native Docker integrations and is very helpful due to its extensions.
- First, install the `Docker` extension in VS Code:
```
  Name: Docker
  Id: ms-azuretools.vscode-docker
  Description: Makes it easy to create, manage, and debug containerized applications.
  Version: 1.20.0
  Publisher: Microsoft
  VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
```
- Next, install the `Remote - Containers` extension in VS Code:
```
Name: Remote - Containers
Id: ms-vscode-remote.remote-containers
Description: Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's full feature set.
Version: 0.224.2
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
```
- Restart VS Code
- Open up the cloned repo folder and a terminal that has its working directory set to that folder
- Click the green icon in the bottom-left corner of VS Code
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/29434974/157105378-b9a8b9c6-0bd4-4800-9f91-0d7620eebde2.png">

- Select "Attach to a Running Container" and pick the Notebook container (`docker-compose up` to start container)
- VS Code will attach itself to the container and you can use VS Code just like normal inside the container
- If you wish to install additional extensions for syntax highlighting, source/version control etc., you will need to do so inside the container - even if they are already installed on the host!
---

## Connecting a Database
- Currently, the application is configured to connect to a sample "World" database. To connect to a different database, it must be configurable in PostgreSQL. 
- You also must have the `Username`, and `Password` properties of the database to connect to it.
- Provide these values in the Environment variables in the `docker-compose.yml` file to connect an external database. Make sure you delete the `World.sql` file in the `db` directory. Do ***not*** share this file as it has private authentication information.
- Then, to create the database you desire, you must provide instructions in a `.sql` file. Create or copy a new `.sql` file that defines your database in the `db` directory.
- Now, when you run `docker compose-up` your Notebook will be connected to the database you specified.
- Any changes you make to this database will be persisted across containers with the use of a bind mount which has already been configured. The `db` directory will contain the database that persists. 
- If you wish to connect a local database (that's already set up) to the Docker container, that is a complex process and requires extra configurations. The following two links will be of help:
- [Troubleshooting Local Database Connection with PostgreSQL Container](https://forums.docker.com/t/unable-to-connect-to-external-postgresql-database-from-a-application-docker-container/89185)
- [The `pg_hba.conf` File](https://www.postgresql.org/docs/9.2/auth-pg-hba-conf.html)

### Exit application
- Once you are finished with your task, press `Ctrl+C` in the terminal with the server running. 
- Then, type in `docker-compose down` to remove the containers. 
- Optionally, you can additionally delete the image by opening up the Docker application (the one you installed) and clicking on Images > Datascience Workspace Image > Remove

## Important Notes
- Any modifications/deletions/insertions you make to the Notebook files will be reflected on your local machine in the `notebook` folder so that your source code is easily shareable.
- Once you have the Jupyter server running in the browser, or you have attached VS Code to the container, you will see a `main.py` file. Executing this file will return the first 10 rows of the sample `World` database.

## Issues & Feature Requests
Contact: aakash.kulkarni@sorensonimpact.com
