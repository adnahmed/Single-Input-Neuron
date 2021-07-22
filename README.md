<h1>Single-Input-Neuron</h1>
<br />
<p align="center">
  <a href="https://towardsdatascience.com/the-differences-between-artificial-and-biological-neural-networks-a8b46db828b7">
    <img src="https://miro.medium.com/max/610/1*SJPacPhP4KDEB1AdhOFy_Q.png" alt="Biological Neuron and Artificial Neuron" width="400" height="350">
  </a>

  <p >
   <a href="https://github.com/adnan-repo/Single-Input-Neuron/wiki"><strong>Explore the Wiki »</strong></a>
    <br />
    <br />
    <a href="https://github.com/adnan-repo/Single-Input-Neuron/blob/main/README.md#getting-started">View Demo</a>
    ·
    <a href="https://github.com/adnan-repo/Single-Input-Neuron/issues">Report Bug</a>
    ·
    <a href="https://github.com/adnan-repo/Single-Input-Neuron/issues">Request Feature</a>
  </p>
</p>
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
A Single Input Neuron implemented in Python. 
The repo also includes a library for widely used transfer/activation functions used by the neuron. Below is a screenshot of <a href="https://pypi.org/project/nndesigndemos/">nndesigndemos</a> that implements this neuron nicely.

<p align="center">
<img src="https://github.com/adnan-repo/Single-Input-Neuron/blob/main/docs/images/Screenshot.PNG" alt="Neural Network Design Demos Screenshot" height="450" />
</p>

### Built With

* [argparse](https://docs.python.org/3/library/argparse.html)
* [random](https://docs.python.org/3/library/random.html)
* [exp](https://docs.python.org/3/library/math.html#math.exp)

<!-- GETTING STARTED -->
## Getting Started

Just clone the repo to your local machine and run 
```
python sin.py
```
or if you would like to specify parameters used by neuron manually you can use
```
python sin.py --help
```
This will provide you with information on how to change specific parameters.

### Prerequisites

A [Python 3](https://www.python.org/downloads/) installation.

<!-- USAGE EXAMPLES -->
## Usage

As specified in `sin.py --help`

```
usage: sin [-h] [--p Input] [--w Weight] [--b Bias] [--a Transfer_Func]

Neural Network Design: Single-Input Neuron

optional arguments:
  -h, --help         show this help message and exit
  --p Input          Input for Neuron
  --w Weight         Initial Weight for Neuron
  --b Bias           Initial Bias for Neuron
  --a Transfer_Func  Transfer function used for Neuron
```

_For more detailed explaination on these parameters, please refer to the [Wiki](https://github.com/adnan-repo/Single-Input-Neuron/wiki)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/adnan-repo/Single-Input-Neuron/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**.
<!-- LICENSE -->
## MIT License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Adnan Ahmed Khan - [@adnaahm](https://twitter.com/adnaahm) - mailtoadnan.ahmed@gmail.com

Project Link: [https://github.com/adnan-repo/Single-Input-Neuron](https://github.com/adnan-repo/Single-Input-Neuron)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/adnan-repo/Single-Input-Neuron/graphs/contributors
[forks-url]: https://github.com/adnan-repo/Single-Input-Neuron/network/members
[stars-url]: https://github.com/adnan-repo/Single-Input-Neuron/stargazers
[issues-url]: https://github.com/adnan-repo/Single-Input-Neuron/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/adnan-repo/Single-Input-Neuron/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/adnan-data-developer/
[product-screenshot]: docs/images/screenshot.png
