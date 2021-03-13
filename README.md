MongoDB was used as the database server.
[MongoDB link](https://www.mongodb.com/try/download/community?tck=docs_server)

## Audio Types:
* Song
* Podcast
* AudioBook


## Response Type:
* Action is successful: 200 OK
* The request is invalid: 400 bad request (Any client url issue)
* Any error: 500 internal server error (unexpected error)


LocalHost Port number: 9000


## Parameter Format:
- name           - Mandatory Parameter. Should not be null or empty, less than 100 characters. "name" will act as the "title" for the audiobook.
- id             - Mandatory Parameter. Should not be null or empty, positive integer.
- duration       - Mandatory Parameter. Should not be null or empty, positive integer.
- uptime         - Mandatory Parameter. Should not be in the past/null/empty. Should be in the format - {YYYY-MM-DD}.
- author         - Mandatory Parameter and applicable only for audiobook.Should not be null or empty, positive integer.
- narrator       - Mandatory Parameter and applicable only for audiobook.Should not be null or empty, positive integer.
- host           - Mandatory Parameter and applicable only for Podcast. Should not be null or empty, less than 100 character
- participants   - Applicable for podcast and an optional parameter. Parameter type is list. If provided, should not be null or empty, less than 100 characters.Maximum of 10 participants can be passed.

>Note: In case of any validation failure, 400 bad request response will be thrown. 



## Request Url Format


  - Create:
      - Create Song : 
            ```http://localhost:9000/song/create?name=<name>&id=<id>&duration=<duration>&uptime=<uptime>```
      - Create AudioBook : 
            ```http://localhost:9000/audiobook/create?name=<name>&id=<id>&duration=<duration>&uptime=<uptime>&author=<author>&narrator=<narrator>```
      - Create Podcast:
            ```http://localhost:9000/podcast/create?name=<name>&id=<id>&duration=<duration>&uptime=<uptime>&host=<host>&participants=<participant1>&participants=<participant2>```
            
  - Get:
      - Get All Record song/Audiobook/Podcast:```http://localhost:9000/<audioFileType>```
      - Get any one Record song/Audiobook/Podcast:```http://localhost:9000/<audioFileType>/<audioFileId>/get```

  - Update:
      - Update Song : 
        ```http://localhost:9000/song/<audioFileId>/update?name=<name>&duration=<duration>&uptime=<uptime>```
      - Update Audiobook:
        ```http://localhost:9000/audiobook/<audioFileId>/update?name=<name>&duration=<duration>&uptime=<uptime>&author=<author>&narrator=<narrator>```
      - Update Podcast:
        ```http://localhost:9000/podcast/<audioFileId>/update?name=<name>&duration=<duration>&uptime=<uptime>&host=<host>&participants=<participant1>&participants=<participant2>```
  
  - Delete:
      - Delete song/Audiobook/Podcast: ```http://localhost:9000/<audioFileType>/<audioFileId>/delete```

