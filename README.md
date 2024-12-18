# Menu

A latex template resembling a generic restaurant menu.


<img width=180 src="./doc/menu_1.svg" />
<img width=180 src="./doc/menu_2.svg" />
<img width=180 src="./doc/menu_3.svg" />
<img width=180 src="./doc/menu_4.svg" />

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

