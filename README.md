# Proxy Voting Mechanisms
[![Foundry](https://badgen.net/badge/Selenium/4.1.2/yellow)](https://www.selenium.dev/)
[![Solidity](https://badgen.net/badge/BS4/4.11.1/purple)](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
> Web Scraper for DeepDAO

<div align="center">
  <img src="https://giphy.com/gifs/Giflytics-gif-jazminantoinette-giflytics-xT9C25UNTwfZuk85WP/giphy.gif" width="480" height="360" allowFullScreen></img>
  
  <br/>
  <em>Source: <a>https://giphy.com/gifs/season-20-the-simpsons-20x4-3o6MbdY9Nc9G51by5G<a/></em>
</div> 

## Table of Contents
- [Proxy Voting Mechanisms](#proxy-voting-mechanisms)
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Technologies Used](#technologies-used)
  - [Documentation](#documentation)
  - [Setup](#setup)
    - [Requirements](#requirements)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Project Status](#project-status)
  - [Future Work](#future-work)
  - [Acknowledgements](#acknowledgements)

## General Information
- Repo was created to develop delegate voting mechanisms that work with the majority of DAO voting implementations
- Initial version works for:
  - OpenZeppelin's ERC20Votes implementation 
  - Compound's Governor Alpha

## Technologies Used
- Solidity - version 0.8.15
- Foundry - version 0.2.0

## Documentation 
- Full documentation is present [here](https://honeysuckle-allspice-948.notion.site/ca4e6b04886e4b6bbd5537515a434ff6?v=9f192a654c5f49de91b942089df0cd20)

## Setup
### Requirements 
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Foundry/Forge](https://github.com/foundry-rs/foundry#installation)
  - Should be able to run `forge --version` if done correctly
### Installation
`git clone https://github.com/ArcStreetCapital/governance-contracts.git`\
`cd governance-contracts`
`forge install` - this installs all necessary dependencies. 


## Usage

- To run all tests use:\
`forge test`

- To run one specific testing contract use:\
`forge test --match-contract <contract name>`

- To run one specific test use:\
`forge test --match-test <function name>`

(In case of function name clashes you can be more specific)
- To run one specific test found in a contract use:\
`forge test --match-contract <contract name> --match-test <function name>`

To increase verbosity of tests use the `-v` flag (up to 5).

Refer to the [foundry book](https://book.getfoundry.sh/), for more commands.


## Project Status
Project is: _in progress_

## Future Work

To do:
- Include more voting mechanisms


## Acknowledgements
The following is the list of resources used in this repo:
- Tests were written with the help of the [foundry book](https://book.getfoundry.sh/)
- Thanks to the development team [@ArcStCapital](https://github.com/ArcStreetCapital) for all the help!