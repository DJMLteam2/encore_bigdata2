# encore_bigdata2
This package is for the practice of Encore MLOps and Bigdata education course in October 2023. The package consists of six different modules, each of which contains a single function. The following part of this document describes how to install, develope, test, and deploy the package, and instructions to run each functions.

## Install
```Bash
$ pip install hello-pysatellite
```
## Dev.
```Bash
$ git clone ...
$ cd encore_bigdata2
$ pdm venv create
$ source .venv/bin/activate
(encore_bigdata-3.8) $ pdm install
```

## Test
```Bash
$ pdm add -dG test pytest pytest-cov
$ pytest
$ pytest -s
$ pytest --cov
```

## Deploy
```Bash
$ pdm publish
```

## Contributing

## Instructions for each module
This section refers to the instructions for each modules and their own functions.  
Remember, while the one can use these functions through importing the modules and functions in Python environment, you can also run these functions individually by the specific command which can be found in each section of functions.  
### `app_8trider.py`
#### `randomMember()`
This function prints the name of randomly selected member of the group. There are six group members in this group.
```Python
from encore_bigdata2.app_8trider import randomMember
```  
```Bash
$ whosbuy
```

#### `menuRecommend()`
This function helps select a menu for lunch time. There are 13 menus in the menu list in the function, which includes "굶기"(it means **"starve"** in Korean...). May the God protect them...
```Python
from encore_bigdata2.app_8trider import menuRecommend
```  
```Bash
$ menu
```

### `app_doxgxxn.py`
#### `coin_game(num)`
The function for the game at drink party. As the user runs the function, it flips two coins. If the two coins show the tail samely, the user must drink the beverage as a penalty.
> Note: This function is not working properly yet, and probably will be fixed in near future.  


```Python
from encore_bigdata2.app_doxgxxn import coin_game
```  
```Bash
$ coin_game
```

### `app_felicette.py`
#### `today_felicette()`
This function simply prints what day it is today. The units of the today's date is from year to microsecond.
```Python
from encore_bigdata2.app_felicette import today_felicette
```  
```Bash
$ today_datetime
```

### `app_jiug.py`
#### `play_card_game()`
The card game this function refers to is 'black jack'. If you are not familiar with the rules of black jack, the player who gets the score the nearest to the number 21 wins. If the player's score gets higher than 21, the player immediately lose the game. If the score is exactly 21, the player wins the game immediately. Or else, the players calculate the score based on the number on the cards they hold.
```Python
from encore_bigdata2.app_jiug import play_card_game
```  
```Bash
$ black_jack
```

### `app_tjkpolisher.py`
#### `samsung_price()`
This function prints the stock price of Samsung Electronics(stock code: 005930) in Korean stock market. As the stock market opens at 09:00 KST and closes at 15:30, when the user runs this code at the time when the market is still open, it continuously prints the changing price at the very current timestamp. Otherwise, the function will print the latest close price of the stock.
```Python
from encore_bigdata2.app_tjkpolisher import samsung_price
```  
```Bash
$ samsung_price
```