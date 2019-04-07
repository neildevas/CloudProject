# CloudProject

A minimal "cloud" to run commands in containers and automatically perform scaling and load balancing

## Dependencies

- `python3.5`
- `virtualenv`
- `docker`
- `etcd`
- `nginx`

## Load balancing

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
