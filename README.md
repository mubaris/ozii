# Ozii

Generating **PulseGraphs** from text.

Checkout [this blog post](https://mubaris.com/2017-10-04/project-ozii) for more info.

## Usage

When the program is executed directly from the terminal it accepts the following arguments:

1. ```-t, --text```: string, mandatory. Input sentence from which to generate the graph.
2. ```-s, --size```: int, optional with default value 500. Size in pixel value.
3. ```-d, --dir```: string, optional with default value "output". Directory where the output image will be saved.

By calling: ```python ozii.py -h``` the help will show up in the terminal.

Usage examples:
- ```python ozii.py -t Hello world```
- ```python ozii.py -t Hello world -s 650```
- ```python ozii.py -t Hello world -d Testing```
- ```python ozii.py -t Hello world -s 650 -d Testing```

## Examples

#### ozii

![ozii](https://i.imgur.com/OdY8DbM.png)

#### Time

![Time](https://i.imgur.com/7rFdrBq.png)

#### There is no linear time

![There is no linear time](https://i.imgur.com/kgP2lWK.png)

#### Batman

![Batman](https://i.imgur.com/Ypj5K3Q.png)

#### I am Batman

![I am Batman](https://i.imgur.com/Y6Lfuw5.png)

#### Human

![Human](https://i.imgur.com/fnob73l.png)

#### Humanity

![Humanity](https://i.imgur.com/KqCpsPi.png)

Checkout `examples` for more example PulseGraphs.