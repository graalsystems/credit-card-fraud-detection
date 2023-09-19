# Credit card fraud detection

## Aim

The primary objective here is to develop a robust use case designed to identify and prevent fraudulent online transactions, a challenge frequently encountered by both retailers and digital-only businesses (pure players). This use case holds significant relevance for the PMU framework, particularly concerning wallet transactions involving reloading of funds.

Our overarching goal is to establish a framework capable of swiftly and accurately detecting fraudulent banking transactions using the available datasets. To achieve this, we will construct a model that assesses each transaction by assigning it a fraud indicator. The implementation of this model will be facilitated through the use of Graal's comprehensive suite of services, encompassing its workspaces and low-code engine.

To outline our approach for this use case, we will begin by initiating a low-code data integration job, allowing us to seamlessly amalgamate the available data sources. Following this, we will delve into an exploration of the data, meticulously examining its attributes and characteristics to uncover potential insights and opportunities. Subsequently, we will embark on the creation of a low-code job aimed at modelling fraudulent activities. This model will then undergo refinement and optimization, ultimately culminating in its deployment and exposure for efficient fraud detection and prevention.

## Data integration

The fraud data is composed of 3 datasets : `transaction.csv` (description of the transactions), `geo.csv` (information of IP per country) and `provider.csv` (name of the provider for each IP range). The dataset columns are described below.

### Transaction dataset :credit_card:

|  Column name 	  |    Description        	     |  Type  	  |   Example     	    |
|:---------------:|:---------------------------:|:---------:|:------------------:|
| `CN`          	 | Card number               	 | Integer 	 | 6011636165535360 	 |
| `date`        	 | Date of the transaction   	 |  Date  	  | 2022-02-01       	 |
| `montant`     	 | Transaction amount        	 | Integer 	 | 13595            	 |
| `ip`          	 | IP address                	 | String  	 | 6.200.204.63     	 |
| `ip_range`   	  | Range of the IP address   	 | String  	 | 6.0.0.0/8        	 |
| `is_valid`    	 | Is the transaction valid? 	 | Boolean 	 | True             	 |

### Geographic dataset :world_map:

|  Column name          	  | Description           	 | Type             	 | Example       	 |
|:------------------------:|:-----------------------:|:------------------:|:---------------:|
| `ip_range`             	 | Range of IP addresses 	 | String           	 | 163.10.0.0/16 	 |
| `country_name`         	 | Country name          	 | String           	 | Argentina     	 |
| `continent_name`       	 | Continent name        	 | String           	 | South America 	 |
| `continent_code`       	 | Continent code        	 | String           	 | SA            	 |
| `is_in_european_union` 	 | Is the country in EU? 	 | Integer (0 or 1) 	 | 0             	 |

### Provider dataset :globe_with_meridians:

|  Column name 	  |   Description      	    | Type  	  |   Example    	   |
|:---------------:|:-----------------------:|:--------:|:----------------:|
| `ip_range`    	 | Range of IP addresses 	 | String 	 | 101.144.0.0/12 	 |
| `provider`    	 | IP provider           	 | String 	 | CyberGhost     	 |
