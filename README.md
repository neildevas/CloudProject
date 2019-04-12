# CloudProject

A minimal 'cloud' which runs commands in containers and scales and load-balances them

### Dependencies

- `python3.5` / `pip`
- `docker`
- `etcd`
- `nginx`

### Installation

Slight configuration is needed:

- `python3 -m pip install -r requirements.txt` 
- the user running the scripts will need permission to use docker and nginx

### Running It

In one terminal, do `./manager` to run the 'cloud manager server'

Then, in another, do `./mycloud <command> <args>` for each command you'd like to issue to the 'cloud' being operated by the 'cloud manager server'

### More Information

#### Load balancing internals

Load balancing works by manipulating the `nginx` config file at `/etc/nginx/nginx.conf`.

For example, to load-balance incoming port 80 traffic to 3 servers listening on 9000,9001, and 9002, respectively, we add the following to the `nginx` config file and run `nginx -s reload`:

```
stream {

    ...
    [more server-upstream pairs]
    ...

    server {
        listen 80;
        proxy_pass server_group_name;
    }

    upstream server_group_name {
        server localhost:9000;
        server localhost:9001;
        server localhost:9002;
    }
}
```
