# notifications API


=== "GET Get a thread subscription for the authenticated user"

    This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://developer.github.com/v3/activity/watching/#get-a-repository-subscription).

Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:thread_id` | `string` | Yes | (Required) thread_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "created_at": "2012-10-06T21:34:12Z",
  "ignored": false,
  "reason": null,
  "subscribed": true,
  "thread_url": "https://api.github.com/notifications/threads/1",
  "url": "https://api.github.com/notifications/threads/1/subscription"
}
    ```

    


=== "PUT Set a thread subscription"

    If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.

You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.

Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://developer.github.com/v3/activity/notifications/#delete-a-thread-subscription) endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:thread_id` | `string` | Yes | (Required) thread_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "ignored": false
}
    ```
    

    #### Response Example
    
    ```json
    {
  "created_at": "2012-10-06T21:34:12Z",
  "ignored": false,
  "reason": null,
  "subscribed": true,
  "thread_url": "https://api.github.com/notifications/threads/1",
  "url": "https://api.github.com/notifications/threads/1/subscription"
}
    ```

    


=== "DELETE Delete a thread subscription"

    Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://developer.github.com/v3/activity/notifications/#set-a-thread-subscription) endpoint and set `ignore` to `true`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:thread_id` | `string` | Yes | (Required) thread_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get a thread"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:thread_id` | `string` | Yes | (Required) thread_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "id": "1",
  "last_read_at": "2014-11-07T22:01:45Z",
  "reason": "subscribed",
  "repository": {
    "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
    "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
    "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
    "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
    "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
    "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
    "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
    "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
    "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
    "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
    "description": "This your first repo!",
    "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
    "fork": false,
    "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
    "full_name": "octocat/Hello-World",
    "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
    "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
    "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
    "git_url": "git:github.com/octocat/Hello-World.git",
    "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
    "html_url": "https://github.com/octocat/Hello-World",
    "id": 1296269,
    "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
    "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
    "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
    "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
    "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
    "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
    "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
    "name": "Hello-World",
    "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
    "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
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
    "private": false,
    "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
    "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
    "ssh_url": "git@github.com:octocat/Hello-World.git",
    "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
    "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
    "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
    "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
    "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
    "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
    "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
    "url": "https://api.github.com/repos/octocat/Hello-World"
  },
  "subject": {
    "latest_comment_url": "https://api.github.com/repos/octokit/octokit.rb/issues/comments/123",
    "title": "Greetings",
    "type": "Issue",
    "url": "https://api.github.com/repos/octokit/octokit.rb/issues/123"
  },
  "unread": true,
  "updated_at": "2014-11-07T22:01:45Z",
  "url": "https://api.github.com/notifications/threads/1"
}
    ```

    


=== "PATCH Mark a thread as read"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:thread_id` | `string` | Yes | (Required) thread_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List notifications for the authenticated user"

    List all notifications for the current user, sorted by most recently updated.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `all` | `string` | Yes | If `true`, show notifications marked as read. | `false` |
    | `participating` | `string` | Yes | If `true`, only shows notifications in which the user is directly participating or mentioned. | `false` |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `before` | `string` | Yes | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "id": "1",
    "last_read_at": "2014-11-07T22:01:45Z",
    "reason": "subscribed",
    "repository": {
      "archive_url": "https://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
      "assignees_url": "https://api.github.com/repos/octocat/Hello-World/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/octocat/Hello-World/branches{/branch}",
      "collaborators_url": "https://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/octocat/Hello-World/comments{/number}",
      "commits_url": "https://api.github.com/repos/octocat/Hello-World/commits{/sha}",
      "compare_url": "https://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/octocat/Hello-World/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/octocat/Hello-World/contributors",
      "deployments_url": "https://api.github.com/repos/octocat/Hello-World/deployments",
      "description": "This your first repo!",
      "downloads_url": "https://api.github.com/repos/octocat/Hello-World/downloads",
      "events_url": "https://api.github.com/repos/octocat/Hello-World/events",
      "fork": false,
      "forks_url": "https://api.github.com/repos/octocat/Hello-World/forks",
      "full_name": "octocat/Hello-World",
      "git_commits_url": "https://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
      "git_url": "git:github.com/octocat/Hello-World.git",
      "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
      "html_url": "https://github.com/octocat/Hello-World",
      "id": 1296269,
      "issue_comment_url": "https://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/octocat/Hello-World/issues{/number}",
      "keys_url": "https://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/octocat/Hello-World/labels{/name}",
      "languages_url": "https://api.github.com/repos/octocat/Hello-World/languages",
      "merges_url": "https://api.github.com/repos/octocat/Hello-World/merges",
      "milestones_url": "https://api.github.com/repos/octocat/Hello-World/milestones{/number}",
      "name": "Hello-World",
      "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
      "notifications_url": "https://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
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
      "private": false,
      "pulls_url": "https://api.github.com/repos/octocat/Hello-World/pulls{/number}",
      "releases_url": "https://api.github.com/repos/octocat/Hello-World/releases{/id}",
      "ssh_url": "git@github.com:octocat/Hello-World.git",
      "stargazers_url": "https://api.github.com/repos/octocat/Hello-World/stargazers",
      "statuses_url": "https://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/octocat/Hello-World/subscribers",
      "subscription_url": "https://api.github.com/repos/octocat/Hello-World/subscription",
      "tags_url": "https://api.github.com/repos/octocat/Hello-World/tags",
      "teams_url": "https://api.github.com/repos/octocat/Hello-World/teams",
      "trees_url": "https://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
      "url": "https://api.github.com/repos/octocat/Hello-World"
    },
    "subject": {
      "latest_comment_url": "https://api.github.com/repos/octokit/octokit.rb/issues/comments/123",
      "title": "Greetings",
      "type": "Issue",
      "url": "https://api.github.com/repos/octokit/octokit.rb/issues/123"
    },
    "unread": true,
    "updated_at": "2014-11-07T22:01:45Z",
    "url": "https://api.github.com/notifications/threads/1"
  }
]
    ```

    


=== "PUT Mark notifications as read"

    Marks all notifications as "read" removes it from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://developer.github.com/v3/activity/notifications/#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.

    

    
    #### Request Body
    
    ```json
    {
  "last_read_at": "\u003cdateTime\u003e",
  "read": "\u003cboolean\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    

