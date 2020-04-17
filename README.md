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
Start with Flask server
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
    "10629609": 9.5, 
    "39783699": 9.2, 
    "39783757": 9.4, 
    "52051887": 9.8, 
    "54518466": 7.7, 
    "56147311": 9.8, 
    "125215746": 9.6, 
    "156946563": 8.4, 
    "179807165": 9.7, 
    "182745702": 9.4, 
    "189164665": 8.8, 
    "197424692": 9.5, 
    "204057283": 9.8, 
    "211674621": 8.4, 
    "212182102": 9.5, 
    "215470481": 9.7, 
    "218463820": 9.5, 
    "242045127": 9.3, 
    "245545766": 9.2, 
    "247182770": 9.4, 
    "248952912": 9.2, 
    "256333191": 9.8, 
    "273186587": 9.0, 
    "310945514": 8.7, 
    "322570741": 9.6, 
    "335796482": 9.2, 
    "348763879": 9.8, 
    "357155710": 9.4, 
    "365033132": 8.6, 
    "407506683": 9.3, 
    "426465073": 9.6, 
    "431732772": 9.7, 
    "435795966": 8.9, 
    "441405265": 9.6, 
    "452380857": 9.5, 
    "468473528": 7.5, 
    "469889031": 9.9, 
    "471842473": 9.6, 
    "496825171": 9.0, 
    "509890081": 9.2, 
    "516578359": 9.5, 
    "517355615": 9.9, 
    "526975153": 9.4, 
    "577826440": 9.4, 
    "584873797": 9.7, 
    "601258379": 9.9, 
    "635709241": 9.4, 
    "657087823": 9.3, 
    "662873910": 9.7, 
    "682311408": 9.4, 
    "684861823": 9.1, 
    "694070227": 9.9, 
    "695552814": 9.1, 
    "703812878": 9.1, 
    "721831811": 9.3, 
    "726338035": 9.2, 
    "757124888": 9.8, 
    "764847541": 9.4, 
    "788533857": 9.6, 
    "792347859": 9.9, 
    "794543643": 9.9, 
    "795870301": 9.3, 
    "836683677": 9.0, 
    "837223094": 9.7, 
    "872885036": 8.6, 
    "878359849": 9.0, 
    "880157271": 9.0, 
    "881416742": 9.0, 
    "881859481": 9.9, 
    "944198509": 9.6, 
    "965386169": 8.5, 
    "975156288": 9.1, 
    "981255027": 9.7, 
    "995092780": 9.8
  }, 
  "productId": 54518466
}
```
