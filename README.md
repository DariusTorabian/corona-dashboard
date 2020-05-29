
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/dariustorabian/corona-dashboard">
    <img src="images/logo.png" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Corona Dashboard</h3>

  <p align="center">
    A Dashboard built with data from the JHU.
    <br />
    <br />
    <a href="https://bitly.com/coronadt">View Demo</a>
    ·
    <a href="https://github.com/dariustorabian/corona-dashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/dariustorabian/corona-dashboard/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

![Project Preview](/images/intro.gif)


In this project, I've used the publicly available Covid-19 Data from the [Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) to build a dashboard containing useful informations about the spread of the virus.

This project has been realized using AWS EC2, AWS RDS, PostgreSQL, Metabase and a bit of Python & Bash. All credit regarding the data itself belongs to the amazing people of the CSSE at JHU.



### Built With

* [Metabase](https://www.metabase.com/)
* [PostgreSQL](https://www.postgresql.org/)
* [Amazon EC2](https://aws.amazon.com/de/ec2/)
* [Amazon RDS](https://aws.amazon.com/de/rds/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

I'd advice you to create an own virtual environment for this project. I'm using [Anaconda](https://anaconda.org/).


### Installation & Usage
 
1. Clone the repo
```sh
git clone https://github.com/dariustorabian/corona-dashboard.git
```
2. Install dependencies with the requirements.txt
```sh
conda create --name <NameOfEnvironment> --file requirements.txt
```

3. Run [get_and_clean_data.py](https://github.com/dariustorabian/corona-dashboard/blob/master/src/get_and_glean_data.py). This script will fetch the newest data and output cleaned csvs with data on regional- and country-level.

4. If you'd like to push the data to your DB, please provide an environment variable in the format 

    ```DB_STRING=mysql://username:password@host/dbname```

    Then run [db_update.py](https://github.com/dariustorabian/corona-dashboard/blob/master/src/db_update.py). I've only used data on country-level, therefore this script will only push the csv with country-level data to the DB you specify.

5. Set up Metabase on your machine, connect the DB and create your own Dashboard. I've used an AWS EC2 for that and AWS RDS as the DB.

6. With the help of the included ```countries_mapping.csv``` from [DataHub.io](https://datahub.io/core/country-list) it is possible to match the data with ISO 3166-1 country codes to easily display the data on maps inside Metabase.

7. Execute the provided [corona_update.sh](https://github.com/dariustorabian/corona-dashboard/blob/master/src/corona_update.sh) once a day to get the newest data pushed into your DB. I automated this process with a cronjob.


<!-- ROADMAP -->
## Roadmap

Currently, there are no new features in planning. This could change though, so feel free to check back again.

You can also always take a look at the [open issues](https://github.com/dariustorabian/corona-dashboard/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Darius Torabian

* Feel free to contact me via [mail](mailto:darius.torabian@gmail.com).
* Here's my [linkedin profile](linkedin-url).
* My twitter-handle is:[@darius_torabian](https://twitter.com/darius_torabian).
* This is my [website](https://dariustorabian.de).

Project Link: [https://github.com/dariustorabian/corona-dashboard](https://github.com/dariustorabian/corona-dashboard)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
* [DataHub.io](https://datahub.io/core/country-list)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dariustorabian/corona-dashboard.svg?style=flat-square
[contributors-url]: https://github.com/dariustorabian/corona-dashboard/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dariustorabian/corona-dashboard.svg?style=flat-square
[forks-url]: https://github.com/dariustorabian/corona-dashboard/network/members
[stars-shield]: https://img.shields.io/github/stars/dariustorabian/corona-dashboard.svg?style=flat-square
[stars-url]: https://github.com/dariustorabian/corona-dashboard/stargazers
[issues-shield]: https://img.shields.io/github/issues/dariustorabian/corona-dashboard.svg?style=flat-square
[issues-url]: https://github.com/dariustorabian/corona-dashboard/issue
[license-shield]: https://img.shields.io/github/license/dariustorabian/corona-dashboard.svg?style=flat-square
[license-url]: https://github.com/dariustorabian/corona-dashboard/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: www.linkedin.com/in/dariustorabian
[product-screenshot]: images/screenshot.png