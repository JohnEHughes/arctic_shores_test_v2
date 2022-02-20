<h2>Arctic SHores Tech Test v2</h2>
This is my second version to answer the tech test. In this version I have set up a Django REST framework and created two endpoints:
create-candidate
create-score

Using these endpoints, a user can GET and POST candidate records to the database.

<h3>create-candidate</h3>
This endpoint has two fields:

Candidate name 
A character field with a max length of 60

Candidate Ref
A character field with max length of 8, has to be unique and is validated with validator_ref()
The validator checks if the length is exactly 8 - if not it will return a ValidationError.
It then checks to make sure the string is only made up of letters and numbers - if not a ValidationError is raised.



<h3>create-score</h3>
This endpoint has two fields:

Candidate Ref
A character field with max length of 8, has to be unique and is validated with validator_ref()
The validator checks if the length is exactly 8 - if not it will return a ValidationError.
It then checks to make sure the string is only made up of letters and numbers - if not a ValidationError is raised.

Candidate Score
A Float Field
validate_score() is used to check the score is between 0 and 100 inclusive. If not, a ValidationError is raised.

