## Traveller

##### A character generator for the tabletop game Travellers



## UI
### Dependencies
- Nodejs
- npm
### Local Startup
Working directory ./ui

- `yarn start` runs a development version of the UI

Use `localhost:3000` to view the ui

## API
### Dependencies
- docker (or python)

### Local Startup
Working directory ./app

- `docker build -t traveller_app:local .` Builds a dev version of the traveller api docker container
- `docker run -p 5000:5000 traveller_app:local` Runs the dev api and opens up port 5000 on the host.

Use `localhost:5000` to reach the service.

### Specifications
With the api running, go to `localhost:5000/api/` to get a user friendly swagger ui view.

`localhost:5000/api/specs` will give you the swagger.json file