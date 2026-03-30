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
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "created_at": "2016-09-05T14:21:06Z",
  "creator": {
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
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:20:22Z",
  "url": "https://api.github.com/projects/columns/cards/1478"
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
  "archived": "\u003cboolean\u003e",
  "note": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "created_at": "2016-09-05T14:21:06Z",
  "creator": {
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
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:20:22Z",
  "url": "https://api.github.com/projects/columns/cards/1478"
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
  "column_id": "\u003cinteger\u003e",
  "position": "\u003cstring\u003e"
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
    "archived": false,
    "column_url": "https://api.github.com/projects/columns/367",
    "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
    "created_at": "2016-09-05T14:21:06Z",
    "creator": {
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
    "id": 1478,
    "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
    "note": "Add payload for delete Project column",
    "project_url": "https://api.github.com/projects/120",
    "updated_at": "2016-09-05T14:20:22Z",
    "url": "https://api.github.com/projects/columns/cards/1478"
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
  "note": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "archived": false,
  "column_url": "https://api.github.com/projects/columns/367",
  "content_url": "https://api.github.com/repos/api-playground/projects-test/issues/3",
  "created_at": "2016-09-05T14:21:06Z",
  "creator": {
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
  "id": 1478,
  "node_id": "MDExOlByb2plY3RDYXJkMTQ3OA==",
  "note": "Add payload for delete Project column",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:20:22Z",
  "url": "https://api.github.com/projects/columns/cards/1478"
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
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "created_at": "2016-09-05T14:18:44Z",
  "id": 367,
  "name": "To Do",
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:22:28Z",
  "url": "https://api.github.com/projects/columns/367"
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
  "name": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "created_at": "2016-09-05T14:18:44Z",
  "id": 367,
  "name": "To Do",
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:22:28Z",
  "url": "https://api.github.com/projects/columns/367"
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
  "position": "\u003cstring\u003e"
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
    "cards_url": "https://api.github.com/projects/columns/367/cards",
    "created_at": "2016-09-05T14:18:44Z",
    "id": 367,
    "name": "To Do",
    "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
    "project_url": "https://api.github.com/projects/120",
    "updated_at": "2016-09-05T14:22:28Z",
    "url": "https://api.github.com/projects/columns/367"
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
  "name": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "cards_url": "https://api.github.com/projects/columns/367/cards",
  "created_at": "2016-09-05T14:18:44Z",
  "id": 367,
  "name": "To Do",
  "node_id": "MDEzOlByb2plY3RDb2x1bW4zNjc=",
  "project_url": "https://api.github.com/projects/120",
  "updated_at": "2016-09-05T14:22:28Z",
  "url": "https://api.github.com/projects/columns/367"
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
  "body": "Developer documentation project for the developer site.",
  "columns_url": "https://api.github.com/projects/1002604/columns",
  "created_at": "2011-04-10T20:09:31Z",
  "creator": {
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
  "html_url": "https://github.com/api-playground/projects-test/projects/1",
  "id": 1002604,
  "name": "Projects Documentation",
  "node_id": "MDc6UHJvamVjdDEwMDI2MDQ=",
  "number": 1,
  "owner_url": "https://api.github.com/repos/api-playground/projects-test",
  "state": "open",
  "updated_at": "2014-03-03T18:58:10Z",
  "url": "https://api.github.com/projects/1002604"
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
  "body": "\u003cstring\u003e",
  "name": "\u003cstring\u003e",
  "organization_permission": "\u003cstring\u003e",
  "private": "\u003cboolean\u003e",
  "state": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "body": "Developer documentation project for the developer site.",
  "columns_url": "https://api.github.com/projects/1002604/columns",
  "created_at": "2011-04-10T20:09:31Z",
  "creator": {
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
  "html_url": "https://github.com/api-playground/projects-test/projects/1",
  "id": 1002604,
  "name": "Projects Documentation",
  "node_id": "MDc6UHJvamVjdDEwMDI2MDQ=",
  "number": 1,
  "owner_url": "https://api.github.com/repos/api-playground/projects-test",
  "state": "open",
  "updated_at": "2014-03-03T18:58:10Z",
  "url": "https://api.github.com/projects/1002604"
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

    

