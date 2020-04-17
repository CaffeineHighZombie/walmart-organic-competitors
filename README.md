# Walmart Organic Competitors
Challenge description: [Walmart Organic Competitors Coding Challenge](./Walmart%20Organic%20Competitors%20Coding%20Challenge.pdf)
## Instructions for environment setup 
### Creating and setting up python virtual environment with required python modules
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
## Instructions for running the tool
Start Flask server
```bash
$ flask run
```
## productId Lookup API
ProductId Lookup API looks up specific product on Walmart and returns the ranking of competitors.
### Example Queries
Lookup for item id 54518466
```
http://localhost:5000//api/v1/lookup?productId=54518466
```
### Query Parameters
| Param Name    | Description           | Required/Optional |
| :------------ | :-------------------- | :---------------- |
| productId     | Product ID to lookup.	|Required           |
### Sample Response
```
{
  "competitors": {
    "1": {
      "productId": 54518466, 
      "score": 7.0
    }, 
    "2": {
      "productId": 468473528, 
      "score": 7.4
    }, 
    "3": {
      "productId": 965386169, 
      "score": 8.1
    }, 
    "4": {
      "productId": 435795966, 
      "score": 8.3
    }, 
    "5": {
      "productId": 872885036, 
      "score": 8.3
    }, 
    "6": {
      "productId": 211674621, 
      "score": 8.3
    }, 
    "7": {
      "productId": 310945514, 
      "score": 8.7
    }, 
    "8": {
      "productId": 156946563, 
      "score": 8.8
    }, 
    "9": {
      "productId": 247182770, 
      "score": 8.9
    }, 
    "10": {
      "productId": 509890081, 
      "score": 9.0
    }, 
    "11": {
      "productId": 881416742, 
      "score": 9.0
    }, 
    "12": {
      "productId": 880157271, 
      "score": 9.1
    }, 
    "13": {
      "productId": 335796482, 
      "score": 9.1
    }, 
    "14": {
      "productId": 684861823, 
      "score": 9.1
    }, 
    "15": {
      "productId": 695552814, 
      "score": 9.2
    }, 
    "16": {
      "productId": 179807165, 
      "score": 9.2
    }, 
    "17": {
      "productId": 357155710, 
      "score": 9.2
    }, 
    "18": {
      "productId": 726338035, 
      "score": 9.2
    }, 
    "19": {
      "productId": 39783699, 
      "score": 9.2
    }, 
    "20": {
      "productId": 878359849, 
      "score": 9.3
    }, 
    "21": {
      "productId": 245545766, 
      "score": 9.3
    }, 
    "22": {
      "productId": 764847541, 
      "score": 9.3
    }, 
    "23": {
      "productId": 365033132, 
      "score": 9.3
    }, 
    "24": {
      "productId": 407506683, 
      "score": 9.3
    }, 
    "25": {
      "productId": 526975153, 
      "score": 9.3
    }, 
    "26": {
      "productId": 39783757, 
      "score": 9.3
    }, 
    "27": {
      "productId": 721831811, 
      "score": 9.4
    }, 
    "28": {
      "productId": 182745702, 
      "score": 9.4
    }, 
    "29": {
      "productId": 322570741, 
      "score": 9.4
    }, 
    "30": {
      "productId": 836683677, 
      "score": 9.4
    }, 
    "31": {
      "productId": 635709241, 
      "score": 9.4
    }, 
    "32": {
      "productId": 242045127, 
      "score": 9.4
    }, 
    "33": {
      "productId": 657087823, 
      "score": 9.5
    }, 
    "34": {
      "productId": 757124888, 
      "score": 9.5
    }, 
    "35": {
      "productId": 189164665, 
      "score": 9.5
    }, 
    "36": {
      "productId": 197424692, 
      "score": 9.5
    }, 
    "37": {
      "productId": 788533857, 
      "score": 9.5
    }, 
    "38": {
      "productId": 10629609, 
      "score": 9.5
    }, 
    "39": {
      "productId": 471842473, 
      "score": 9.6
    }, 
    "40": {
      "productId": 218463820, 
      "score": 9.6
    }, 
    "41": {
      "productId": 452380857, 
      "score": 9.6
    }, 
    "42": {
      "productId": 584873797, 
      "score": 9.6
    }, 
    "43": {
      "productId": 516578359, 
      "score": 9.6
    }, 
    "44": {
      "productId": 682311408, 
      "score": 9.6
    }, 
    "45": {
      "productId": 441405265, 
      "score": 9.6
    }, 
    "46": {
      "productId": 215470481, 
      "score": 9.6
    }, 
    "47": {
      "productId": 426465073, 
      "score": 9.6
    }, 
    "48": {
      "productId": 662873910, 
      "score": 9.7
    }, 
    "49": {
      "productId": 125215746, 
      "score": 9.7
    }, 
    "50": {
      "productId": 881859481, 
      "score": 9.7
    }, 
    "51": {
      "productId": 348763879, 
      "score": 9.7
    }, 
    "52": {
      "productId": 360116938, 
      "score": 9.7
    }, 
    "53": {
      "productId": 837223094, 
      "score": 9.7
    }, 
    "54": {
      "productId": 204057283, 
      "score": 9.7
    }, 
    "55": {
      "productId": 256333191, 
      "score": 9.8
    }, 
    "56": {
      "productId": 700011839, 
      "score": 9.8
    }, 
    "57": {
      "productId": 469889031, 
      "score": 9.8
    }, 
    "58": {
      "productId": 56147311, 
      "score": 9.8
    }, 
    "59": {
      "productId": 694070227, 
      "score": 9.8
    }, 
    "60": {
      "productId": 517355615, 
      "score": 9.9
    }, 
    "61": {
      "productId": 273186587, 
      "score": 9.9
    }, 
    "62": {
      "productId": 52051887, 
      "score": 9.9
    }, 
    "63": {
      "productId": 878896338, 
      "score": 9.9
    }, 
    "64": {
      "productId": 794543643, 
      "score": 9.9
    }, 
    "65": {
      "productId": 216229903, 
      "score": 9.9
    }
  }, 
  "productId": 54518466
}
```
