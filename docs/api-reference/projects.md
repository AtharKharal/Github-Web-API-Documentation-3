# projects API


=== "GET Get a project card"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:card_id` | `string` | Yes | (Required) card_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/cards/1478",
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "created_at": "2016-09-05T14:21:06Z",
  "updated_at": "2016-09-05T14:20:22Z",
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "project_url": "https://api.github.com/projects/120"
}
    ```

    


=== "PATCH Update an existing project card"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:card_id` | `string` | Yes | (Required) card_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "note": "<string>",
  "archived": "<boolean>"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/cards/1478",
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "created_at": "2016-09-05T14:21:06Z",
  "updated_at": "2016-09-05T14:20:22Z",
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "project_url": "https://api.github.com/projects/120"
}
    ```

    


=== "DELETE Delete a project card"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:card_id` | `string` | Yes | (Required) card_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "POST Move a project card"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:card_id` | `string` | Yes | (Required) card_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "position": "<string>",
  "column_id": "<integer>"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List project cards"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `archived_state` | `string` | Yes | Filters the project cards that are returned by the card's state. Can be one of `all`,`archived`, or `not_archived`. | `not_archived` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "url": "https://api.github.com/projects/columns/cards/1478",
    "id": 1478,
    "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
    "note": "Add payload for delete Project column",
    "creator": {
      "login": "octocat",
      "id": 1,
      "node_id": "MDQ6VXNlcjE=",
      "avatar_url": "https://github.com/images/error/octocat_happy.gif",
      "gravatar_id": "",
      "url": "https://api.github.com/users/octocat",
      "html_url": "https://github.com/octocat",
      "followers_url": "https://api.github.com/users/octocat/followers",
      "following_url": "https://api.github.com/users/octocat/following{/other_user}",
      "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
      "organizations_url": "https://api.github.com/users/octocat/orgs",
      "repos_url": "https://api.github.com/users/octocat/repos",
      "events_url": "https://api.github.com/users/octocat/events{/privacy}",
      "received_events_url": "https://api.github.com/users/octocat/received_events",
      "type": "User",
      "site_admin": false
    },
    "created_at": "2016-09-05T14:21:06Z",
    "updated_at": "2016-09-05T14:20:22Z",
    "archived": false,
    "column_url": "https://api.github.com/projects/columns/367",
    "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
    "project_url": "https://api.github.com/projects/120"
  }
]
    ```

    


=== "POST Create a project card"

    **Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key.

Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://developer.github.com/v3/pulls/#list-pull-requests)" endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "note": "<string>"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/cards/1478",
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "created_at": "2016-09-05T14:21:06Z",
  "updated_at": "2016-09-05T14:20:22Z",
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "project_url": "https://api.github.com/projects/120"
}
    ```

    


=== "GET Get a project column"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/367",
  "project_url": "https://api.github.com/projects/120",
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "id": 367,
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "name": "To Do",
  "created_at": "2016-09-05T14:18:44Z",
  "updated_at": "2016-09-05T14:22:28Z"
}
    ```

    


=== "PATCH Update an existing project column"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "name": "<string>"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/367",
  "project_url": "https://api.github.com/projects/120",
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "id": 367,
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "name": "To Do",
  "created_at": "2016-09-05T14:18:44Z",
  "updated_at": "2016-09-05T14:22:28Z"
}
    ```

    


=== "DELETE Delete a project column"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "POST Move a project column"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:column_id` | `string` | Yes | (Required) column_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "position": "<string>"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "PUT Add project collaborator"

    Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project `admin` to add a collaborator.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "permission": "write"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove user as a collaborator"

    Removes a collaborator from an organization project. You must be an organization owner or a project `admin` to remove a collaborator.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get project permission for a user"

    Returns the collaborator's permission level for an organization project. Possible values for the `permission` key: `admin`, `write`, `read`, `none`. You must be an organization owner or a project `admin` to review a user's permission level.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "permission": "admin",
  "user": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
}
    ```

    


=== "GET List project collaborators"

    Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `affiliation` | `string` | Yes | Filters the collaborators by their affiliation. Can be one of:  
\* `outside`: Outside collaborators of a project that are not a member of the project's organization.  
\* `direct`: Collaborators with permissions to a project, regardless of organization membership status.  
\* `all`: All collaborators the authenticated user can see. | `all` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
]
    ```

    


=== "GET List project columns"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "url": "https://api.github.com/projects/columns/367",
    "project_url": "https://api.github.com/projects/120",
    "cards_url": "https://api.github.com/projects/columns/367/cards",
    "id": 367,
    "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
    "name": "To Do",
    "created_at": "2016-09-05T14:18:44Z",
    "updated_at": "2016-09-05T14:22:28Z"
  }
]
    ```

    


=== "POST Create a project column"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "name": "<string>"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "url": "https://api.github.com/projects/columns/367",
  "project_url": "https://api.github.com/projects/120",
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "id": 367,
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "name": "To Do",
  "created_at": "2016-09-05T14:18:44Z",
  "updated_at": "2016-09-05T14:22:28Z"
}
    ```

    


=== "GET Get a project"

    Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "owner_url": "https://api.github.com/repos/api-playground/projects-test",
  "url": "https://api.github.com/projects/1002604",
  "html_url": "https://github.com/api-playground/projects-test/projects/1",
  "columns_url": "https://api.github.com/projects/1002604/columns",
  "id": 1002604,
  "node_id": "MDc6UHJvamVjdDEwMDI2MDQ=",
  "name": "Projects Documentation",
  "body": "Developer documentation project for the developer site.",
  "number": 1,
  "state": "open",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "created_at": "2011-04-10T20:09:31Z",
  "updated_at": "2014-03-03T18:58:10Z"
}
    ```

    


=== "PATCH Update a project"

    Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "name": "<string>",
  "body": "<string>",
  "state": "<string>",
  "organization_permission": "<string>",
  "private": "<boolean>"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "owner_url": "https://api.github.com/repos/api-playground/projects-test",
  "url": "https://api.github.com/projects/1002604",
  "html_url": "https://github.com/api-playground/projects-test/projects/1",
  "columns_url": "https://api.github.com/projects/1002604/columns",
  "id": 1002604,
  "node_id": "MDc6UHJvamVjdDEwMDI2MDQ=",
  "name": "Projects Documentation",
  "body": "Developer documentation project for the developer site.",
  "number": 1,
  "state": "open",
  "creator": {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  },
  "created_at": "2011-04-10T20:09:31Z",
  "updated_at": "2014-03-03T18:58:10Z"
}
    ```

    


=== "DELETE Delete a project"

    Deletes a project board. Returns a `404 Not Found` status if projects are disabled.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    

