# FashionCloud-Assignment
This is to demonstrate my coding skills with assignment given by FashionCloud.

As the problem statement has 3 parts, i am deviding this repository in 3 parts.
- part 1 is coding which is named as FashionCloudProject
- part 2 is thinking, so I am putting the future developments I thought.
- Part 3 is architecture, in that I am adding some documents with diagrams.


##Part 1 : Coding
As you can see that all the coding part I have included in folder named `FashionCloudProject`.

I started with making some drawings on paper regarding how I am planning to parse the data and process them, and what I am planning to display as output.

Step 1: Plan

I am using django in this case, the reason for choosing django is as follows:
- High domain availability for choosing models, for example, there is in build django ORM, I can also configure SQLAlchemy if needs to.
- It is really flexible to look after backend pannel for django, For API purpose I would have chose FastAPI, but I thought there is no need for designning well maintained API for this task as if needed, I would have integrated graphene with models.
- For future aspects, there could be multiple deployment options for django app, like if we choose to go for serverless, we can use wsgi or asgi facility to deploy backend pannel on APIGateway with AWS lambda.

Step 2: Assumptions

- I am making an assumption that, if we will be using multiple file uploads of a same kind, the format of those file would be same, for example, all the data will be stored in single column, adn semicolon(;) is the delimeter.
- It will help me design parsing facilities for same kind of a files.
- As it is supposed to be assignment problem, building security of the app, and authentication is not required as it is mainly designed for algorithm purpose.

Step 3: Code

- I have made django app, which has models designed with inherited archietecture.
- I have created 2 parser classes for each file, for mapping file and the main data file.
- For mapping I have created two maps, named single_map and multi_map, to be specific, single map is for the fields which have value updates and include single column only, and for multi column, I have create multimap using DefaultDict, which has let say, key "EU" and as that value, I have added dictionary, which has desired value like "European size 39".
- As I have created django app, all the rendering facilities (jinja) I have used to show the query result (Not the JSON) but it inherits the idea displayed in problem statement.
- I have coded a models fot this assigment with inheritance architecture.
- code also includes some jupyter notebook files, which might show how I came up with the coded solution, file names are [demo_run.ipynb](demo_run.ipynb) and [playground.ipynb](playground.ipynb)
- all the screenshot dumps for models in django backed and the rendered outputs are dumped in dumps folder. which includes [srticles](dumps/articles_model.png), [file-upload-form](dumps/django_form_for_fileUpload.png), [product](dumps/product_model.png), [sizeMatrix](dumps/sizeMatrix_model.png) and finaly the [rendered-output](dumps/rendered_heirarchical_result.png).

Step 4: Execution

- Clone the repo
- install all the requirements mentioned in requirements.txt 
- run the migrations by running `makemigrations` and `migrate`
- create user by using command `python manage.py createsuperuser`
- run the app by `runserver` command, visit `127.0.0.1:8000/upload/` to upload given file in `problem_statement_files` folder in this project
- When submit, the heirarchy will be displayed on `result` endpoint
- Also, there was only 2 files to parse, hence I have designed the normal parsers, if more types of files are there, I would definately design `Inversion of Control` methods and `parser configuration injection` simalteniously.


##Part 2 : Thinking (FlowChart)

For part 2 of the assignment, I have created seperate document named [FashionCloud-Part2.pdf](part_2/FashionCloud-Part2.pdf) which explains how would i approach the same assignment when we think of extention.
In that file I have included a flowchart and my take on how would I do that.

In terms of further thinking, 
For Future Prospect, I would do following:
- I would definately go for generating Graphene schema, that will help creating a queries, in regards with pour expectation, we can manipulate the schema, queries, and Resolvers as well.
- I have done this assignment by the intention of getting interviewing, hence I might not be considering all the cases in terms of data validations and authorization/authentication, but for future needs, I would definately consider developing token based authorization, that works with session, for additional security hands.
- For the coding, I hahve used sqlite db, but by seeing the data, I would choose to go for NoSQL, if thinking of cloud, I would go for DynamoDB, with Reddis cache management or ElasticSearch.
- At last, I would consider to store data temporarily while processing locally, so that we can reduce the number of trips to database.


##Part 3: Architecture on AWS

For part 3 of the assignment, which asks to elaborate over AWS architecture, using different services, I have explained those things in the pdf, pasted at `part_3` folder in this repository file named [FashionCloud-Part3.pdf](part_3/FashionCloud-Part3.pdf).
I did not add the diagram here as I am facing some difficulties in creating diagram from mentioned tool in problem statement.