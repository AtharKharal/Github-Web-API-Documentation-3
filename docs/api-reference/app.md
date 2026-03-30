# app API


=== "PUT Suspend an app installation"

    **Note:** Suspending a GitHub App installation is currently in beta and subject to change. Before you can suspend a GitHub App, the app owner must enable suspending installations for the app by opting-in to the beta. For more information, see "[Suspending a GitHub App installation](https://developer.github.com/apps/managing-github-apps/suspending-a-github-app-installation/)."

Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.

To suspend a GitHub App, you must be an account owner or have admin permissions in the repository or organization where the app is installed.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:installation_id` | `string` | Yes | (Required) installation_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Unsuspend an app installation"

    **Note:** Suspending a GitHub App installation is currently in beta and subject to change. Before you can suspend a GitHub App, the app owner must enable suspending installations for the app by opting-in to the beta. For more information, see "[Suspending a GitHub App installation](https://developer.github.com/apps/managing-github-apps/suspending-a-github-app-installation/)."

Removes a GitHub App installation suspension.

To unsuspend a GitHub App, you must be an account owner or have admin permissions in the repository or organization where the app is installed and suspended.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:installation_id` | `string` | Yes | (Required) installation_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get an installation for the authenticated app"

    Enables an authenticated GitHub App to find an installation's information using the installation id. The installation's account type (`target_type`) will be either an organization or a user account, depending which account the repository belongs to.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:installation_id` | `string` | Yes | (Required) installation_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "access_tokens_url": "https://api.github.com/installations/1/access_tokens",
  "account": {
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
  "app_id": 1,
  "app_slug": "github-actions",
  "created_at": "2017-07-08T16:18:44-04:00",
  "events": [
    "push",
    "pull_request"
  ],
  "html_url": "https://github.com/organizations/github/settings/installations/1",
  "id": 1,
  "permissions": {
    "checks": "write",
    "contents": "read",
    "metadata": "read"
  },
  "repositories_url": "https://api.github.com/installation/repositories",
  "repository_selection": "selected",
  "single_file_name": "config.yml",
  "target_id": 1,
  "target_type": "Organization",
  "updated_at": "2017-07-08T16:18:44-04:00"
}
    ```

    


=== "DELETE Delete an installation for the authenticated app"

    Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://developer.github.com/v3/apps/#suspend-an-app-installation)" endpoint.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:installation_id` | `string` | Yes | (Required) installation_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "POST Create an installation access token for an app"

    Creates an installation access token that enables a GitHub App to make authenticated API requests for the app's installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of `401 - Unauthorized`, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the `repository_ids` when creating the token. When you omit `repository_ids`, the response does not contain the `repositories` key.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:installation_id` | `string` | Yes | (Required) installation_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "permissions": {
    "contents": "\u003cstring\u003e",
    "def_not_a_repo": "\u003cstring\u003e",
    "deployments": "\u003cstring\u003e",
    "issues": "\u003cstring\u003e",
    "single_file": "\u003cstring\u003e"
  },
  "repositories": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "repository_ids": [
    "\u003cinteger\u003e",
    "\u003cinteger\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "expires_at": "2016-07-11T22:14:10Z",
  "permissions": {
    "contents": "read",
    "issues": "write"
  },
  "repositories": [
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
        "html_url": "https://github.com/licenses/mit",
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
  ],
  "repository_selection": "selected",
  "token": "v1.1f699f1069f60xxx"
}
    ```

    


=== "GET List installations for the authenticated app"

    You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

The permissions the installation has are included under the `permissions` key.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `outdated` | `string` | Yes | No description. | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "access_tokens_url": "https://api.github.com/installations/1/access_tokens",
    "account": {
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
    "app_id": 1,
    "app_slug": "github-actions",
    "created_at": "2017-07-08T16:18:44-04:00",
    "events": [
      "push",
      "pull_request"
    ],
    "html_url": "https://github.com/organizations/github/settings/installations/1",
    "id": 1,
    "permissions": {
      "checks": "write",
      "contents": "read",
      "metadata": "read"
    },
    "repositories_url": "https://api.github.com/installation/repositories",
    "repository_selection": "selected",
    "single_file_name": "config.yml",
    "target_id": 1,
    "target_type": "Organization",
    "updated_at": "2017-07-08T16:18:44-04:00"
  }
]
    ```

    


=== "GET Get the authenticated app"

    Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the `installations_count` in the response. For more details about your app's installations, see the "[List installations for the authenticated app](https://developer.github.com/v3/apps/#list-installations-for-the-authenticated-app)" endpoint.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    

    

    #### Response Example
    
    ```json
    {
  "created_at": "2017-07-08T16:18:44-04:00",
  "description": "",
  "events": [
    "push",
    "pull_request"
  ],
  "external_url": "https://example.com",
  "html_url": "https://github.com/apps/octoapp",
  "id": 1,
  "name": "Octocat App",
  "node_id": "MDExOkludGVncmF0aW9uMQ==",
  "owner": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "events_url": "https://api.github.com/orgs/github/events",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/octocat",
    "id": 1,
    "login": "github",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "site_admin": true,
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "type": "User",
    "url": "https://api.github.com/orgs/github"
  },
  "permissions": {
    "contents": "read",
    "issues": "write",
    "metadata": "read",
    "single_file": "write"
  },
  "slug": "octoapp",
  "updated_at": "2017-07-08T16:18:44-04:00"
}
    ```

    

