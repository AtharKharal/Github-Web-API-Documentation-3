# teams/{team id} API


=== "GET List reactions for a team discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion comment`](https://developer.github.com/v3/reactions/#list-reactions-for-a-team-discussion-comment) endpoint.

List the reactions to a [team discussion comment](https://developer.github.com/v3/teams/discussion_comments/). OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `content` | `string` | Yes | Returns a single [reaction type](https://developer.github.com/v3/reactions/#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z",
    "id": 1,
    "node_id": "MDg6UmVhY3Rpb24x",
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

    


=== "POST Create reaction for a team discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create reaction for a team discussion comment`](https://developer.github.com/v3/reactions/#create-reaction-for-a-team-discussion-comment) endpoint.

Create a reaction to a [team discussion comment](https://developer.github.com/v3/teams/discussion_comments/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with a `Status: 200 OK` means that you already added the reaction type to this team discussion comment.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "content": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z",
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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

    


=== "GET Get a discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://developer.github.com/v3/teams/discussion_comments/#get-a-discussion-comment) endpoint.

Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Do you like apples?",
  "body_html": "\u003cp\u003eDo you like apples?\u003c/p\u003e",
  "body_version": "5eb32b219cdc6a5a9b29ba5d6caa9c51",
  "created_at": "2018-01-15T23:53:58Z",
  "discussion_url": "https://api.github.com/teams/2403582/discussions/1",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1",
  "last_edited_at": null,
  "node_id": "MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=",
  "number": 1,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2403582/discussions/1/reactions"
  },
  "updated_at": "2018-01-15T23:53:58Z",
  "url": "https://api.github.com/teams/2403582/discussions/1/comments/1"
}
    ```

    


=== "PATCH Update a discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion comment](https://developer.github.com/v3/teams/discussion_comments/#update-a-discussion-comment) endpoint.

Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Do you like pineapples?",
  "body_html": "\u003cp\u003eDo you like pineapples?\u003c/p\u003e",
  "body_version": "e6907b24d9c93cc0c5024a7af5888116",
  "created_at": "2018-01-15T23:53:58Z",
  "discussion_url": "https://api.github.com/teams/2403582/discussions/1",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1",
  "last_edited_at": "2018-01-26T18:22:20Z",
  "node_id": "MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=",
  "number": 1,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2403582/discussions/1/reactions"
  },
  "updated_at": "2018-01-26T18:22:20Z",
  "url": "https://api.github.com/teams/2403582/discussions/1/comments/1"
}
    ```

    


=== "DELETE Delete a discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a discussion comment](https://developer.github.com/v3/teams/discussion_comments/#delete-a-discussion-comment) endpoint.

Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List discussion comments (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://developer.github.com/v3/teams/discussion_comments/#list-discussion-comments) endpoint.

List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `direction` | `string` | Yes | One of `asc` (ascending) or `desc` (descending). | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "author": {
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
    "body": "Do you like apples?",
    "body_html": "\u003cp\u003eDo you like apples?\u003c/p\u003e",
    "body_version": "5eb32b219cdc6a5a9b29ba5d6caa9c51",
    "created_at": "2018-01-15T23:53:58Z",
    "discussion_url": "https://api.github.com/teams/2403582/discussions/1",
    "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1",
    "last_edited_at": null,
    "node_id": "MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=",
    "number": 1,
    "reactions": {
      "+1": 3,
      "-1": 1,
      "confused": 0,
      "eyes": 1,
      "heart": 1,
      "hooray": 0,
      "laugh": 0,
      "rocket": 1,
      "total_count": 5,
      "url": "https://api.github.com/teams/2403582/discussions/1/reactions"
    },
    "updated_at": "2018-01-15T23:53:58Z",
    "url": "https://api.github.com/teams/2403582/discussions/1/comments/1"
  }
]
    ```

    


=== "POST Create a discussion comment (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Create a discussion comment](https://developer.github.com/v3/teams/discussion_comments/#create-a-discussion-comment) endpoint.

Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Do you like apples?",
  "body_html": "\u003cp\u003eDo you like apples?\u003c/p\u003e",
  "body_version": "5eb32b219cdc6a5a9b29ba5d6caa9c51",
  "created_at": "2018-01-15T23:53:58Z",
  "discussion_url": "https://api.github.com/teams/2403582/discussions/1",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1/comments/1",
  "last_edited_at": null,
  "node_id": "MDIxOlRlYW1EaXNjdXNzaW9uQ29tbWVudDE=",
  "number": 1,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2403582/discussions/1/reactions"
  },
  "updated_at": "2018-01-15T23:53:58Z",
  "url": "https://api.github.com/teams/2403582/discussions/1/comments/1"
}
    ```

    


=== "GET List reactions for a team discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion`](https://developer.github.com/v3/reactions/#list-reactions-for-a-team-discussion) endpoint.

List the reactions to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `content` | `string` | Yes | Returns a single [reaction type](https://developer.github.com/v3/reactions/#reaction-types). Omit this parameter to list all reactions to a team discussion. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "content": "heart",
    "created_at": "2016-05-20T20:09:31Z",
    "id": 1,
    "node_id": "MDg6UmVhY3Rpb24x",
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

    


=== "POST Create reaction for a team discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create reaction for a team discussion`](https://developer.github.com/v3/reactions/#create-reaction-for-a-team-discussion) endpoint.

Create a reaction to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with a `Status: 200 OK` means that you already added the reaction type to this team discussion.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "content": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "content": "heart",
  "created_at": "2016-05-20T20:09:31Z",
  "id": 1,
  "node_id": "MDg6UmVhY3Rpb24x",
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

    


=== "GET Get a discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://developer.github.com/v3/teams/discussions/#get-a-discussion) endpoint.

Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Hi! This is an area for us to collaborate as a team.",
  "body_html": "\u003cp\u003eHi! This is an area for us to collaborate as a team\u003c/p\u003e",
  "body_version": "0d495416a700fb06133c612575d92bfb",
  "comments_count": 0,
  "comments_url": "https://api.github.com/teams/2343027/discussions/1/comments",
  "created_at": "2018-01-25T18:56:31Z",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1",
  "last_edited_at": null,
  "node_id": "MDE0OlRlYW1EaXNjdXNzaW9uMQ==",
  "number": 1,
  "pinned": false,
  "private": false,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2343027/discussions/1/reactions"
  },
  "team_url": "https://api.github.com/teams/2343027",
  "title": "Our first team post",
  "updated_at": "2018-01-25T18:56:31Z",
  "url": "https://api.github.com/teams/2343027/discussions/1"
}
    ```

    


=== "PATCH Update a discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://developer.github.com/v3/teams/discussions/#update-a-discussion) endpoint.

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e",
  "title": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Hi! This is an area for us to collaborate as a team.",
  "body_html": "\u003cp\u003eHi! This is an area for us to collaborate as a team\u003c/p\u003e",
  "body_version": "0d495416a700fb06133c612575d92bfb",
  "comments_count": 1,
  "comments_url": "https://api.github.com/teams/2343027/discussions/1/comments",
  "created_at": "2018-01-25T18:56:31Z",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1",
  "last_edited_at": "2018-01-26T18:22:20Z",
  "node_id": "MDE0OlRlYW1EaXNjdXNzaW9uMQ==",
  "number": 1,
  "pinned": false,
  "private": false,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2343027/discussions/1/reactions"
  },
  "team_url": "https://api.github.com/teams/2343027",
  "title": "Welcome to our first team post",
  "updated_at": "2018-01-26T18:22:20Z",
  "url": "https://api.github.com/teams/2343027/discussions/1"
}
    ```

    


=== "DELETE Delete a discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Delete a discussion`](https://developer.github.com/v3/teams/discussions/#delete-a-discussion) endpoint.

Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List discussions (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://developer.github.com/v3/teams/discussions/#list-discussions) endpoint.

List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `direction` | `string` | Yes | One of `asc` (ascending) or `desc` (descending). | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "author": {
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
    "body": "Hi! This is an area for us to collaborate as a team.",
    "body_html": "\u003cp\u003eHi! This is an area for us to collaborate as a team\u003c/p\u003e",
    "body_version": "0d495416a700fb06133c612575d92bfb",
    "comments_count": 0,
    "comments_url": "https://api.github.com/teams/2343027/discussions/1/comments",
    "created_at": "2018-01-25T18:56:31Z",
    "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1",
    "last_edited_at": null,
    "node_id": "MDE0OlRlYW1EaXNjdXNzaW9uMQ==",
    "number": 1,
    "pinned": false,
    "private": false,
    "reactions": {
      "+1": 3,
      "-1": 1,
      "confused": 0,
      "eyes": 1,
      "heart": 1,
      "hooray": 0,
      "laugh": 0,
      "rocket": 1,
      "total_count": 5,
      "url": "https://api.github.com/teams/2343027/discussions/1/reactions"
    },
    "team_url": "https://api.github.com/teams/2343027",
    "title": "Our first team post",
    "updated_at": "2018-01-25T18:56:31Z",
    "url": "https://api.github.com/teams/2343027/discussions/1"
  }
]
    ```

    


=== "POST Create a discussion (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create a discussion`](https://developer.github.com/v3/teams/discussions/#create-a-discussion) endpoint.

Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e",
  "private": false,
  "title": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "author": {
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
  "body": "Hi! This is an area for us to collaborate as a team.",
  "body_html": "\u003cp\u003eHi! This is an area for us to collaborate as a team\u003c/p\u003e",
  "body_version": "0d495416a700fb06133c612575d92bfb",
  "comments_count": 0,
  "comments_url": "https://api.github.com/teams/2343027/discussions/1/comments",
  "created_at": "2018-01-25T18:56:31Z",
  "html_url": "https://github.com/orgs/github/teams/justice-league/discussions/1",
  "last_edited_at": null,
  "node_id": "MDE0OlRlYW1EaXNjdXNzaW9uMQ==",
  "number": 1,
  "pinned": false,
  "private": false,
  "reactions": {
    "+1": 3,
    "-1": 1,
    "confused": 0,
    "eyes": 1,
    "heart": 1,
    "hooray": 0,
    "laugh": 0,
    "rocket": 1,
    "total_count": 5,
    "url": "https://api.github.com/teams/2343027/discussions/1/reactions"
  },
  "team_url": "https://api.github.com/teams/2343027",
  "title": "Our first team post",
  "updated_at": "2018-01-25T18:56:31Z",
  "url": "https://api.github.com/teams/2343027/discussions/1"
}
    ```

    


=== "GET Get team member (Legacy)"

    The "Get team member" endpoint (described below) is deprecated.

We recommend using the [Get team membership for a user](https://developer.github.com/v3/teams/members/#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.

To list members in a team, the team must be visible to the authenticated user.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "PUT Add team member (Legacy)"

    The "Add team member" endpoint (described below) is deprecated.

We recommend using the [Add or update team membership for a user](https://developer.github.com/v3/teams/members/#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they're changing. The person being added to the team must be a member of the team's organization.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://developer.github.com/v3/#http-verbs)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove team member (Legacy)"

    The "Remove team member" endpoint (described below) is deprecated.

We recommend using the [Remove team membership for a user](https://developer.github.com/v3/teams/members/#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a team member, the authenticated user must have 'admin' permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List team members (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team members`](https://developer.github.com/v3/teams/members/#list-team-members) endpoint.

Team members will include the members of child teams.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `role` | `string` | Yes | Filters members returned by their role in the team. Can be one of:  
\* `member` - normal members of the team.  
\* `maintainer` - team maintainers.  
\* `all` - all members of the team. | `all` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

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

    


=== "GET Get team membership for a user (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://developer.github.com/v3/teams/members/#get-team-membership-for-a-user) endpoint.

Team members will include the members of child teams.

To get a user's membership with a team, the team must be visible to the authenticated user.

**Note:** The `role` for organization owners returns as `maintainer`. For more information about `maintainer` roles, see [Create a team](https://developer.github.com/v3/teams/#create-a-team).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "role": "member",
  "state": "active",
  "url": "https://api.github.com/teams/1/memberships/octocat"
}
    ```

    


=== "PUT Add or update team membership for a user (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team membership for a user](https://developer.github.com/v3/teams/members/#add-or-update-team-membership-for-a-user) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

If the user is already a member of the team's organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

If the user is unaffiliated with the team's organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the "pending" state until the user accepts the invitation, at which point the membership will transition to the "active" state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.

If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "role": "member"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "role": "member",
  "state": "active",
  "url": "https://api.github.com/teams/1/memberships/octocat"
}
    ```

    


=== "DELETE Remove team membership for a user (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove team membership for a user](https://developer.github.com/v3/teams/members/#remove-team-membership-for-a-user) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Check team permissions for a project (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://developer.github.com/v3/teams/#check-team-permissions-for-a-project) endpoint.

Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "body": "High-level roadmap for the upcoming year.",
  "columns_url": "https://api.github.com/projects/1002605/columns",
  "created_at": "2011-04-11T20:09:31Z",
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
  "html_url": "https://github.com/orgs/api-playground/projects/1",
  "id": 1002605,
  "name": "Organization Roadmap",
  "node_id": "MDc6UHJvamVjdDEwMDI2MDU=",
  "number": 1,
  "organization_permission": "write",
  "owner_url": "https://api.github.com/orgs/octocat",
  "permissions": {
    "admin": false,
    "read": true,
    "write": true
  },
  "private": false,
  "state": "open",
  "updated_at": "2014-03-04T18:58:10Z",
  "url": "https://api.github.com/projects/1002605"
}
    ```

    


=== "PUT Add or update team project permissions (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://developer.github.com/v3/teams/#add-or-update-team-project-permissions) endpoint.

Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "permission": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove a project from a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://developer.github.com/v3/teams/#remove-a-project-from-a-team) endpoint.

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List team projects (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://developer.github.com/v3/teams/#list-team-projects) endpoint.

Lists the organization projects for a team.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "body": "High-level roadmap for the upcoming year.",
    "columns_url": "https://api.github.com/projects/1002605/columns",
    "created_at": "2011-04-11T20:09:31Z",
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
    "html_url": "https://github.com/orgs/api-playground/projects/1",
    "id": 1002605,
    "name": "Organization Roadmap",
    "node_id": "MDc6UHJvamVjdDEwMDI2MDU=",
    "number": 1,
    "organization_permission": "write",
    "owner_url": "https://api.github.com/orgs/octocat",
    "permissions": {
      "admin": false,
      "read": true,
      "write": true
    },
    "private": false,
    "state": "open",
    "updated_at": "2014-03-04T18:58:10Z",
    "url": "https://api.github.com/projects/1002605"
  }
]
    ```

    


=== "GET Check team permissions for a repository (Legacy)"

    **Note**: Repositories inherited through a parent team will also be checked.

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://developer.github.com/v3/teams/#check-team-permissions-for-a-repository) endpoint.

You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://developer.github.com/v3/media/) via the `Accept` header:

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:owner` | `string` | Yes | (Required)  | `<string>` |
    | `:repo` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "allow_merge_commit": true,
  "allow_rebase_merge": true,
  "allow_squash_merge": true,
  "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
  "archived": false,
  "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
  "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
  "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
  "clone_url": "https://github.com/octocat/Hello-World.git",
  "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
  "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
  "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
  "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
  "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
  "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
  "created_at": "2011-01-26T19:01:12Z",
  "default_branch": "master",
  "delete_branch_on_merge": true,
  "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
  "description": "This your first repo!",
  "disabled": false,
  "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
  "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
  "fork": false,
  "forks": 1,
  "forks_count": 9,
  "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
  "full_name": "octocat/Hello-World",
  "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
  "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
  "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
  "git_url": "git:github.com/octocat/Hello-World.git",
  "has_downloads": true,
  "has_issues": true,
  "has_pages": false,
  "has_projects": true,
  "has_wiki": true,
  "homepage": "https://github.com",
  "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
  "html_url": "https://github.com/octocat/Hello-World",
  "id": 1296269,
  "is_template": true,
  "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
  "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
  "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
  "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
  "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
  "language": null,
  "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
  "license": {
    "html_url": "https://api.github.com/licenses/mit",
    "key": "mit",
    "name": "MIT License",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "MIT",
    "url": "https://api.github.com/licenses/mit"
  },
  "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
  "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
  "mirror_url": "git:git.example.com/octocat/Hello-World",
  "name": "Hello-World",
  "network_count": 0,
  "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
  "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
  "open_issues": 1,
  "open_issues_count": 0,
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
  "permissions": {
    "admin": false,
    "pull": true,
    "push": false
  },
  "private": false,
  "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
  "pushed_at": "2011-01-26T19:06:43Z",
  "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
  "size": 108,
  "ssh_url": "git@github.com:octocat/Hello-World.git",
  "stargazers_count": 80,
  "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
  "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
  "subscribers_count": 42,
  "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
  "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
  "svn_url": "https://svn.github.com/octocat/Hello-World",
  "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
  "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
  "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
  "template_repository": null,
  "topics": [
    "octocat",
    "atom",
    "electron",
    "api"
  ],
  "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
  "updated_at": "2011-01-26T19:14:43Z",
  "url": "https://api.github.com/repos/octocat/Hello-World",
  "visibility": "public",
  "watchers": 1,
  "watchers_count": 80
}
    ```

    


=== "PUT Add or update team repository permissions (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team repository permissions](https://developer.github.com/v3/teams/#add-or-update-team-repository-permissions) endpoint.

To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.

Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://developer.github.com/v3/#http-verbs)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:owner` | `string` | Yes | (Required)  | `<string>` |
    | `:repo` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "permission": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove a repository from a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://developer.github.com/v3/teams/#remove-a-repository-from-a-team) endpoint.

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    | `:owner` | `string` | Yes | (Required)  | `<string>` |
    | `:repo` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List team repositories (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://developer.github.com/v3/teams/#list-team-repositories) endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "archived": false,
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "clone_url": "https://github.com/octocat/Hello-World.git",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "created_at": "2011-01-26T19:01:12Z",
    "default_branch": "master",
    "delete_branch_on_merge": true,
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "description": "This your first repo!",
    "disabled": false,
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "fork": false,
    "forks_count": 9,
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "full_name": "octocat/Hello-World",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "has_downloads": true,
    "has_issues": true,
    "has_pages": false,
    "has_projects": true,
    "has_wiki": true,
    "homepage": "https://github.com",
    "hooks_url": "https://api.github.com/repos/octocat/Hello-World/hooks",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "is_template": true,
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "language": null,
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "license": {
      "key": "mit",
      "name": "MIT License",
      "node_id": "MDc6TGljZW5zZW1pdA==",
      "spdx_id": "MIT",
      "url": "https://api.github.com/licenses/mit"
    },
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "mirror_url": "git:git.example.com/octocat/Hello-World",
    "name": "Hello-World",
    "network_count": 0,
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
    "open_issues_count": 0,
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
    "permissions": {
      "admin": false,
      "pull": true,
      "push": false
    },
    "private": false,
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "pushed_at": "2011-01-26T19:06:43Z",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "size": 108,
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_count": 80,
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_count": 42,
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "svn_url": "https://svn.github.com/octocat/Hello-World",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "temp_clone_token": "ABTLWHOULUVAXGTRYU7OC2876QJ2O",
    "template_repository": "octocat/template",
    "topics": [
      "octocat",
      "atom",
      "electron",
      "api"
    ],
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "updated_at": "2011-01-26T19:14:43Z",
    "url": "https://api.github.com/repos/octocat/Hello-World",
    "visibility": "public",
    "watchers_count": 80
  }
]
    ```

    


=== "GET List IdP groups for a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List IdP groups for a team`](https://developer.github.com/v3/teams/team_sync/#list-idp-groups-for-a-team) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

List IdP groups connected to a team on GitHub.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "groups": [
    {
      "group_description": "The people who configure your octoworld.",
      "group_id": "123",
      "group_name": "Octocat admins"
    },
    {
      "group_description": "The people who make your octoworld come to life.",
      "group_id": "456",
      "group_name": "Octocat docs members"
    }
  ]
}
    ```

    


=== "PATCH Create or update IdP group connections (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create or update IdP group connections`](https://developer.github.com/v3/teams/team_sync/#create-or-update-idp-group-connections) endpoint.

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Creates, updates, or removes a connection between a team and an IdP group. When adding groups to a team, you must include all new and existing groups to avoid replacing existing groups with the new ones. Specifying an empty `groups` array will remove all connections for a team.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "groups": [
    {
      "description": "\u003cstring\u003e",
      "group_description": "\u003cstring\u003e",
      "group_id": "\u003cstring\u003e",
      "group_name": "\u003cstring\u003e",
      "id": "\u003cstring\u003e",
      "name": "\u003cstring\u003e"
    },
    {
      "description": "\u003cstring\u003e",
      "group_description": "\u003cstring\u003e",
      "group_id": "\u003cstring\u003e",
      "group_name": "\u003cstring\u003e",
      "id": "\u003cstring\u003e",
      "name": "\u003cstring\u003e"
    }
  ],
  "synced_at": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "groups": [
    {
      "group_description": "The people who configure your octoworld.",
      "group_id": "123",
      "group_name": "Octocat admins"
    }
  ]
}
    ```

    


=== "GET Get a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://developer.github.com/v3/teams/#get-a-team-by-name) endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "created_at": "2017-07-14T16:53:42Z",
  "description": "A great team.",
  "html_url": "https://api.github.com/teams/justice-league",
  "id": 1,
  "members_count": 3,
  "members_url": "https://api.github.com/teams/1/members{/member}",
  "name": "Justice League",
  "node_id": "MDQ6VGVhbTE=",
  "organization": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "blog": "https://github.com/blog",
    "company": "GitHub",
    "created_at": "2008-01-14T04:33:35Z",
    "description": "A great organization",
    "email": "octocat@github.com",
    "events_url": "https://api.github.com/orgs/github/events",
    "followers": 20,
    "following": 0,
    "has_organization_projects": true,
    "has_repository_projects": true,
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "is_verified": true,
    "issues_url": "https://api.github.com/orgs/github/issues",
    "location": "San Francisco",
    "login": "github",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "name": "github",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "public_gists": 1,
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "public_repos": 2,
    "repos_url": "https://api.github.com/orgs/github/repos",
    "type": "Organization",
    "updated_at": "2017-08-17T12:37:15Z",
    "url": "https://api.github.com/orgs/github"
  },
  "parent": null,
  "permission": "admin",
  "privacy": "closed",
  "repos_count": 10,
  "repositories_url": "https://api.github.com/teams/1/repos",
  "slug": "justice-league",
  "updated_at": "2017-08-17T12:37:15Z",
  "url": "https://api.github.com/teams/1"
}
    ```

    


=== "PATCH Update a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://developer.github.com/v3/teams/#update-a-team) endpoint.

To edit a team, the authenticated user must either be an organization owner or a team maintainer.

**Note:** With nested teams, the `privacy` for parent teams cannot be `secret`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "description": "\u003cstring\u003e",
  "name": "\u003cstring\u003e",
  "parent_team_id": "\u003cinteger\u003e",
  "permission": "pull",
  "privacy": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "created_at": "2017-07-14T16:53:42Z",
  "description": "A great team.",
  "html_url": "https://api.github.com/teams/justice-league",
  "id": 1,
  "members_count": 3,
  "members_url": "https://api.github.com/teams/1/members{/member}",
  "name": "Justice League",
  "node_id": "MDQ6VGVhbTE=",
  "organization": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "blog": "https://github.com/blog",
    "company": "GitHub",
    "created_at": "2008-01-14T04:33:35Z",
    "description": "A great organization",
    "email": "octocat@github.com",
    "events_url": "https://api.github.com/orgs/github/events",
    "followers": 20,
    "following": 0,
    "has_organization_projects": true,
    "has_repository_projects": true,
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "is_verified": true,
    "issues_url": "https://api.github.com/orgs/github/issues",
    "location": "San Francisco",
    "login": "github",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "name": "github",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "public_gists": 1,
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "public_repos": 2,
    "repos_url": "https://api.github.com/orgs/github/repos",
    "type": "Organization",
    "updated_at": "2017-08-17T12:37:15Z",
    "url": "https://api.github.com/orgs/github"
  },
  "parent": null,
  "permission": "admin",
  "privacy": "closed",
  "repos_count": 10,
  "repositories_url": "https://api.github.com/teams/1/repos",
  "slug": "justice-league",
  "updated_at": "2017-08-17T12:37:15Z",
  "url": "https://api.github.com/teams/1"
}
    ```

    


=== "DELETE Delete a team (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://developer.github.com/v3/teams/#delete-a-team) endpoint.

To delete a team, the authenticated user must be an organization owner or team maintainer.

If you are an organization owner, deleting a parent team will delete all of its child teams as well.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List pending team invitations (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List pending team invitations`](https://developer.github.com/v3/teams/members/#list-pending-team-invitations) endpoint.

The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "created_at": "2016-11-30T06:46:10-08:00",
    "email": "octocat@github.com",
    "id": 1,
    "invitation_team_url": "https://api.github.com/organizations/2/invitations/1/teams",
    "inviter": {
      "avatar_url": "https://github.com/images/error/other_user_happy.gif",
      "events_url": "https://api.github.com/users/other_user/events{/privacy}",
      "followers_url": "https://api.github.com/users/other_user/followers",
      "following_url": "https://api.github.com/users/other_user/following{/other_user}",
      "gists_url": "https://api.github.com/users/other_user/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/other_user",
      "id": 1,
      "login": "other_user",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/other_user/orgs",
      "received_events_url": "https://api.github.com/users/other_user/received_events",
      "repos_url": "https://api.github.com/users/other_user/repos",
      "site_admin": false,
      "starred_url": "https://api.github.com/users/other_user/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/other_user/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/other_user"
    },
    "login": "monalisa",
    "role": "direct_member",
    "team_count": 2
  }
]
    ```

    


=== "GET List child teams (Legacy)"

    **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://developer.github.com/v3/teams/#list-child-teams) endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:team_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "description": "Started it all.",
    "html_url": "https://github.com/orgs/rails/teams/core",
    "id": 2,
    "members_url": "https://api.github.com/teams/2/members{/member}",
    "name": "Original Roster",
    "node_id": "MDQ6VGVhbTI=",
    "parent": {
      "description": "A great team.",
      "html_url": "https://api.github.com/teams/justice-league",
      "id": 1,
      "members_url": "https://api.github.com/teams/1/members{/member}",
      "name": "Justice League",
      "node_id": "MDQ6VGVhbTE=",
      "permission": "admin",
      "privacy": "closed",
      "repositories_url": "https://api.github.com/teams/1/repos",
      "slug": "justice-league",
      "url": "https://api.github.com/teams/1"
    },
    "permission": "admin",
    "privacy": "closed",
    "repositories_url": "https://api.github.com/teams/2/repos",
    "slug": "original-roster",
    "url": "https://api.github.com/teams/2"
  }
]
    ```

    

