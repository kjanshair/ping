## Ping

`hello` and `world` are 2 simple Microservices written in Python and Go respectively.

`hello` communicates with `world` to print the complete `hello world`.

### For `hello`

Set Environment Variables `WORLD_ADDR` and `WORLD_PORT` for defining the complete address of service `world`.

### For `world`

Set Environment Variable `WORLD_PORT` for setting up `world` service port.