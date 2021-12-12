# extract-course-sentiment

## Use and Development
### Create Conda environment:
> $ conda env create -f environment.yml 

### For active development:
> $ conda activate mlexps

## Req. Running Services:
MongoDB on Docker
```
docker pull mongo  
docker run -d -v [PWD]:/home \ 
-p 27017-27019:27017-27019 \
--name mongodb mongo:latest \ 
docker exec -it mongodb bash
```

CoreNLPServer
```
lsof -t -i:9000
kill -9 $(lsof -t -i:9000)
cd stanford-corenlp-4.2.2
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```
