# Listx

A directory listing service that lists a directory's contents and the size of it's contents. Result is ordered by size

It includes 
- a cli for running it via the command prompt
- a flask app that exposes an api endpoint and
- a react application

## Setup

1. Clone repository
2. Setup a python virtualenv

### CLI
- Run the cli on a directory
```sh
python ./listx.py /User/<username>/Downloads
```

### API
- Install python dependences (this project uses [Poetry](https://python-poetry.org/) for managing dependences)
```sh 
poetry install 
```

- Start application
```sh
flask run
```

- Navigate to `http://localhost:5000/api/listx?path=/Users/<username>/Downloads`

### React
- Make sure the api is running see [API Section](#API)

- Ensure you have the latest LTS node is installed as well as [yarn](https://classic.yarnpkg.com/lang/en/)

- Navigate to app and install node modules
```sh
yarn install
``` 

- Start the application
```sh
yarn dev
```

## Pending
- [ ] Containerize application (using docker or kubernters :))
- [ ] Install a production server for backend / frontend
- [ ] Add more checks to catch errors 
- [ ] Paginate response
- [ ] Add tests
