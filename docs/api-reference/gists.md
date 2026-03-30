# gists API


=== "GET Get a gist comment"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    | `:comment_id` | `string` | Yes | (Required) comment_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "author_association": "collaborator",
  "body": "Just commenting for the sake of commenting",
  "created_at": "2011-04-18T23:23:56Z",
  "id": 1,
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "updated_at": "2011-04-18T23:23:56Z",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "user": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "node_id": "MDQ6VXNlcjE=",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/octocat"
  }
}
    ```

    


=== "PATCH Update a gist comment"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    | `:comment_id` | `string` | Yes | (Required) comment_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author_association": "collaborator",
  "body": "Just commenting for the sake of commenting",
  "created_at": "2011-04-18T23:23:56Z",
  "id": 1,
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "updated_at": "2011-04-18T23:23:56Z",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "user": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "node_id": "MDQ6VXNlcjE=",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/octocat"
  }
}
    ```

    


=== "DELETE Delete a gist comment"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    | `:comment_id` | `string` | Yes | (Required) comment_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List gist comments"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "author_association": "collaborator",
    "body": "Just commenting for the sake of commenting",
    "created_at": "2011-04-18T23:23:56Z",
    "id": 1,
    "node_id": "MDExOkdpc3RDb21tZW50MQ==",
    "updated_at": "2011-04-18T23:23:56Z",
    "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
    "user": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    }
  }
]
    ```

    


=== "POST Create a gist comment"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author_association": "collaborator",
  "body": "Just commenting for the sake of commenting",
  "created_at": "2011-04-18T23:23:56Z",
  "id": 1,
  "node_id": "MDExOkdpc3RDb21tZW50MQ==",
  "updated_at": "2011-04-18T23:23:56Z",
  "url": "https://api.github.com/gists/a6db0bec360bb87e9418/comments/1",
  "user": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "node_id": "MDQ6VXNlcjE=",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/octocat"
  }
}
    ```

    


=== "GET List gist forks"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "created_at": "2011-04-14T16:00:49Z",
    "id": "dee9c42e4998ce2ea439",
    "updated_at": "2011-04-14T16:00:49Z",
    "url": "https://api.github.com/gists/dee9c42e4998ce2ea439"
  }
]
    ```

    


=== "POST Fork a gist"

    **Note**: This was previously `/gists/:gist_id/fork`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "comments": 0,
  "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
  "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
  "created_at": "2010-04-14T02:15:15Z",
  "description": "Hello World Examples",
  "files": {
    "hello_world.rb": {
      "filename": "hello_world.rb",
      "language": "Ruby",
      "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
      "size": 167,
      "type": "application/x-ruby"
    }
  },
  "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
  "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
  "id": "aa5a315d61ae9438b18d",
  "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
  "owner": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "octocat",
    "node_id": "MDQ6VXNlcjE=",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/users/octocat"
  },
  "public": true,
  "truncated": false,
  "updated_at": "2011-06-20T11:34:15Z",
  "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
  "user": null
}
    ```

    


=== "GET Check if a gist is starred"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "PUT Star a gist"

    Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://developer.github.com/v3/#http-verbs)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Unstar a gist"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get a gist"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "comments": 0,
  "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
  "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
  "created_at": "2010-04-14T02:15:15Z",
  "description": "Hello World Examples",
  "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
  "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
  "id": "aa5a315d61ae9438b18d",
  "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
  "updated_at": "2011-06-20T11:34:15Z",
  "url": "https://api.github.com/gists/aa5a315d61ae9438b18d"
}
    ```

    


=== "PATCH Update a gist"

    Allows you to update or delete a gist file and rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    "schema type not provided"
    ```
    

    #### Response Example
    
    ```json
    {
  "comments": 0,
  "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
  "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
  "created_at": "2010-04-14T02:15:15Z",
  "description": "Hello World Examples",
  "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
  "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
  "id": "aa5a315d61ae9438b18d",
  "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
  "updated_at": "2011-06-20T11:34:15Z",
  "url": "https://api.github.com/gists/aa5a315d61ae9438b18d"
}
    ```

    


=== "DELETE Delete a gist"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List gist commits"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "change_status": {
      "additions": 180,
      "deletions": 0,
      "total": 180
    },
    "committed_at": "2010-04-14T02:15:15Z",
    "url": "https://api.github.com/gists/aa5a315d61ae9438b18d/57a7f021a713b1c5a6a199b54cc514735d2d462f",
    "user": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "version": "57a7f021a713b1c5a6a199b54cc514735d2d462f"
  }
]
    ```

    


=== "GET Get a gist revision"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:gist_id` | `string` | Yes | (Required) gist_id parameter | `<string>` |
    | `:sha` | `string` | Yes | (Required) sha parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "comments": 0,
  "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
  "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
  "created_at": "2010-04-14T02:15:15Z",
  "description": "Hello World Examples",
  "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
  "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
  "id": "aa5a315d61ae9438b18d",
  "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
  "updated_at": "2011-06-20T11:34:15Z",
  "url": "https://api.github.com/gists/aa5a315d61ae9438b18d/57a7f021a713b1c5a6a199b54cc514735d2d462f"
}
    ```

    


=== "GET List gists for the authenticated user"

    Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists:

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "comments": 0,
    "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
    "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
    "created_at": "2010-04-14T02:15:15Z",
    "description": "Hello World Examples",
    "files": {
      "hello_world.rb": {
        "filename": "hello_world.rb",
        "language": "Ruby",
        "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
        "size": 167,
        "type": "application/x-ruby"
      }
    },
    "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
    "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
    "id": "aa5a315d61ae9438b18d",
    "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "public": true,
    "truncated": false,
    "updated_at": "2011-06-20T11:34:15Z",
    "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
    "user": null
  }
]
    ```

    


=== "POST Create a gist"

    Allows you to add a new gist with one or more files.

**Note:** Don't name your files "gistfile" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

    

    
    #### Request Body
    
    ```json
    {
  "description": "\u003cstring\u003e",
  "files": "\u003cobject\u003e",
  "public": false
}
    ```
    

    #### Response Example
    
    ```json
    {
  "comments": 0,
  "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
  "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
  "created_at": "2010-04-14T02:15:15Z",
  "description": "Hello World Examples",
  "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
  "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
  "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
  "id": "aa5a315d61ae9438b18d",
  "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
  "updated_at": "2011-06-20T11:34:15Z",
  "url": "https://api.github.com/gists/aa5a315d61ae9438b18d"
}
    ```

    


=== "GET List public gists"

    List public gists sorted by most recently updated to least recently updated.

Note: With [pagination](https://developer.github.com/v3/#pagination), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "comments": 0,
    "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
    "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
    "created_at": "2010-04-14T02:15:15Z",
    "description": "Hello World Examples",
    "files": {
      "hello_world.rb": {
        "filename": "hello_world.rb",
        "language": "Ruby",
        "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
        "size": 167,
        "type": "application/x-ruby"
      }
    },
    "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
    "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
    "id": "aa5a315d61ae9438b18d",
    "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "public": true,
    "truncated": false,
    "updated_at": "2011-06-20T11:34:15Z",
    "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
    "user": null
  }
]
    ```

    


=== "GET List starred gists"

    List the authenticated user's starred gists:

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "comments": 0,
    "comments_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/comments/",
    "commits_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/commits",
    "created_at": "2010-04-14T02:15:15Z",
    "description": "Hello World Examples",
    "files": {
      "hello_world.rb": {
        "filename": "hello_world.rb",
        "language": "Ruby",
        "raw_url": "https://gist.githubusercontent.com/octocat/6cad326836d38bd3a7ae/raw/db9c55113504e46fa076e7df3a04ce592e2e86d8/hello_world.rb",
        "size": 167,
        "type": "application/x-ruby"
      }
    },
    "forks_url": "https://api.github.com/gists/aa5a315d61ae9438b18d/forks",
    "git_pull_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "git_push_url": "https://gist.github.com/aa5a315d61ae9438b18d.git",
    "html_url": "https://gist.github.com/aa5a315d61ae9438b18d",
    "id": "aa5a315d61ae9438b18d",
    "node_id": "MDQ6R2lzdGFhNWEzMTVkNjFhZTk0MzhiMThk",
    "owner": {
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/octocat",
      "id": 1,
      "login": "octocat",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/octocat"
    },
    "public": true,
    "truncated": false,
    "updated_at": "2011-06-20T11:34:15Z",
    "url": "https://api.github.com/gists/aa5a315d61ae9438b18d",
    "user": null
  }
]
    ```

    

