### Initialise Alembic for async db.

In order to initialise Alembic you will need to run:
```commandline
alembic init -t async migrations
```
This will generate a migration folder `project/migrations`

When we firstly set up alembic we need to configure the env.py and the
alembic.ini files, but no need for this since it is already configured.

<b> Important information </b>

Under alembic.ini file we have to set the sqlalchemy.url, and currently it is set to
the following:

```
sqlalchemy.url = postgresql+asyncpg://postgres:postgres@localhost:5432/postgres
```

When we change environment we need to change the db url.

### Create and apply migrations

You can create a new migration by running the following command :
```commandline
alembic revision --autogenerate -m "NameForTheFile"
```
this will create a new file under `migrations/version/`

Then will need to run the upgrade method to apply the migration
```commandline
alembic upgrade head
```

### Downgrade

If you want to downgrade to a previous version of the db you can run
```commandline
alembic downgrade -1
```
or if you need to go back multiple migrations, run
```commandline
alembic history
```
to view a list of all the migrations in your project (from newest to oldest),
then copy and paste the identifier of the migration you want to go back to:
```commandline
alembic downgrade Identifier
```
