# Weather history collector

The CLI tool to download weather history information from meta weather api (https://www.metaweather.com/api/)


### System requirements

The solution can be deployed with usual python3 dev tools and should have virtualenv installed. By running the following command from the solution directory will create the virtualenv and install dependencies. The shebang line can be adjusted according to the distro used for deployment.

```$ source setup.sh```

More details about the package dependencies are in ```requirements.txt```


### Usage

It contains two tools, ```solution01.py``` is to download historical weather informatio based on the names of the cities. The following command can be used to run the tool while environment is set. Default values are assumed when parameters are not set.

```(renv) $ python solution01.py --cities='london berlin paris amsterdam' -o download_dir```

Here, the ```-o``` or ```--output``` option sets the directory name where the weather information would be downloaded.


The second solution ```solution02.py``` takes 'years' range as parameters and downloads weather information for each year for Rio and London and saves the temperature differences for all possible years. The following command can be used,

```(renv) $ python solution02.py 2014 2018 --output=weatherinfo```

The first two arguments specify the range of years, and the ```--output``` option can be used to specify a directory. Default values are assumed when parameters are not set. To view the more details on usage the following command can be used,

```(renv) $ python solution01.py --help```
```(renv) $ python solution02.py --help```

### Setup a cronjob

To setup a cronjob the following line can be used to run it silently with a 4 hour period,

```0 */4 * * * <absolute_path>/renv/bin/python <absolute_path>/solution01.py --cities='london berlin paris amsterdam' -o download_dir  > /dev/null 2>&1```

```0 */4 * * * <absolute_path>/renv/bin/python <absolute_path>/solution02.py 2014 2018 --output=weatherinfo  > /dev/null 2>&1```

The ```<absolute_path>``` should be replaced with absolute path based on deployment location.

### Contact

Abdullah Al Zakir Hossain

- aazhbd@conveylive.com


