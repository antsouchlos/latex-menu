# Menu

A latex template resembling a generic restaurant menu.

## Build

### Build manually

```bash
$ make
```

### Build using docker

1. Build docker image
   ```bash
   $ docker build -f Dockerfile . -t menu
   ```
1. Build examples
   ```bash
   $ docker run --rm -v $PWD:$PWD -w $PWD -u `id -u`:`id -g` menu make
   ```

