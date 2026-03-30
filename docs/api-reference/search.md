# search API


=== "GET Search code"

    Searches for query terms inside of a file. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for code, you can get text match metadata for the file **content** and file **path** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find the definition of the `addClass` function inside [jQuery](https://github.com/jquery/jquery) repository, your query would look something like this:

`q=addClass+in:file+language:js+repo:jquery/jquery`

This query searches for the keyword `addClass` within a file's contents. The query limits the search to files where the language is JavaScript in the `jquery/jquery` repository.

#### Considerations for code search

Due to the complexity of searching code, there are a few restrictions on how searches are performed:

*   Only the _default branch_ is considered. In most cases, this will be the `master` branch.
*   Only files smaller than 384 KB are searchable.
*   You must always include at least one search term when searching source code. For example, searching for [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ago&type=Code) is not valid, while [`amazing
language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ago&type=Code) is.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching code](https://help.github.com/articles/searching-code/)" for a detailed list of qualifiers. | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query. Can only be `indexed`, which indicates how recently a file has been indexed by the GitHub search infrastructure. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "git_url": "https://api.github.com/repositories/167174/git/blobs/d7212f9dee2dcc18f084d7df8f417b80846ded5a",
      "html_url": "https://github.com/jquery/jquery/blob/825ac3773694e0cd23ee74895fd5aeb535b27da4/src/attributes/classes.js",
      "name": "classes.js",
      "path": "src/attributes/classes.js",
      "repository": {
        "archive_url": "https://api.github.com/repos/jquery/jquery/{archive_format}{/ref}",
        "assignees_url": "https://api.github.com/repos/jquery/jquery/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/jquery/jquery/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/jquery/jquery/branches{/branch}",
        "collaborators_url": "https://api.github.com/repos/jquery/jquery/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/jquery/jquery/comments{/number}",
        "commits_url": "https://api.github.com/repos/jquery/jquery/commits{/sha}",
        "compare_url": "https://api.github.com/repos/jquery/jquery/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/jquery/jquery/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/jquery/jquery/contributors",
        "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
        "description": "jQuery JavaScript Library",
        "downloads_url": "https://api.github.com/repos/jquery/jquery/downloads",
        "events_url": "https://api.github.com/repos/jquery/jquery/events",
        "fork": false,
        "forks_url": "https://api.github.com/repos/jquery/jquery/forks",
        "full_name": "jquery/jquery",
        "git_commits_url": "https://api.github.com/repos/jquery/jquery/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/jquery/jquery/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/jquery/jquery/git/tags{/sha}",
        "hooks_url": "https://api.github.com/repos/jquery/jquery/hooks",
        "html_url": "https://github.com/jquery/jquery",
        "id": 167174,
        "issue_comment_url": "https://api.github.com/repos/jquery/jquery/issues/comments/{number}",
        "issue_events_url": "https://api.github.com/repos/jquery/jquery/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/jquery/jquery/issues{/number}",
        "keys_url": "https://api.github.com/repos/jquery/jquery/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/jquery/jquery/labels{/name}",
        "languages_url": "https://api.github.com/repos/jquery/jquery/languages",
        "merges_url": "https://api.github.com/repos/jquery/jquery/merges",
        "milestones_url": "https://api.github.com/repos/jquery/jquery/milestones{/number}",
        "name": "jquery",
        "node_id": "MDEwOlJlcG9zaXRvcnkxNjcxNzQ=",
        "notifications_url": "https://api.github.com/repos/jquery/jquery/notifications{?since,all,participating}",
        "owner": {
          "avatar_url": "https://0.gravatar.com/avatar/6906f317a4733f4379b06c32229ef02f?d=https%3A%2F%2Fidenticons.github.com%2Ff426f04f2f9813718fb806b30e0093de.png",
          "events_url": "https://api.github.com/users/jquery/events{/privacy}",
          "followers_url": "https://api.github.com/users/jquery/followers",
          "following_url": "https://api.github.com/users/jquery/following{/other_user}",
          "gists_url": "https://api.github.com/users/jquery/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/jquery",
          "id": 70142,
          "login": "jquery",
          "node_id": "MDQ6VXNlcjcwMTQy",
          "organizations_url": "https://api.github.com/users/jquery/orgs",
          "received_events_url": "https://api.github.com/users/jquery/received_events",
          "repos_url": "https://api.github.com/users/jquery/repos",
          "site_admin": false,
          "starred_url": "https://api.github.com/users/jquery/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/jquery/subscriptions",
          "type": "Organization",
          "url": "https://api.github.com/users/jquery"
        },
        "private": false,
        "pulls_url": "https://api.github.com/repos/jquery/jquery/pulls{/number}",
        "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
        "stargazers_url": "https://api.github.com/repos/jquery/jquery/stargazers",
        "statuses_url": "https://api.github.com/repos/jquery/jquery/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/jquery/jquery/subscribers",
        "subscription_url": "https://api.github.com/repos/jquery/jquery/subscription",
        "tags_url": "https://api.github.com/repos/jquery/jquery/tags",
        "teams_url": "https://api.github.com/repos/jquery/jquery/teams",
        "trees_url": "https://api.github.com/repos/jquery/jquery/git/trees{/sha}",
        "url": "https://api.github.com/repos/jquery/jquery"
      },
      "score": 1,
      "sha": "d7212f9dee2dcc18f084d7df8f417b80846ded5a",
      "url": "https://api.github.com/repositories/167174/contents/src/attributes/classes.js?ref=825ac3773694e0cd23ee74895fd5aeb535b27da4"
    }
  ],
  "total_count": 7
}
    ```

    


=== "GET Search commits"

    Find commits via various criteria on the default branch (usually `master`). This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for commits, you can get text match metadata for the **message** field when you provide the `text-match` media type. For more details about how to receive highlighted search results, see [Text match
metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find commits related to CSS in the [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your query would look something like this:

`q=repo:octocat/Spoon-Knife+css`

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching commits](https://help.github.com/articles/searching-commits/)" for a detailed list of qualifiers. | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query by `author-date` or `committer-date`. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "author": {
        "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=3",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/octocat",
        "id": 583231,
        "login": "octocat",
        "node_id": "MDQ6VXNlcjU4MzIzMQ==",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "received_events_url": "https://api.github.com/users/octocat/received_events",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/octocat"
      },
      "comments_url": "https://api.github.com/repos/octocat/Spoon-Knife/commits/bb4cc8d3b2e14b3af5df699876dd4ff3acd00b7f/comments",
      "commit": {
        "author": {
          "date": "2014-02-04T14:38:36-08:00",
          "email": "octocat@nowhere.com",
          "name": "The Octocat"
        },
        "comment_count": 8,
        "committer": {
          "date": "2014-02-12T15:18:55-08:00",
          "email": "octocat@nowhere.com",
          "name": "The Octocat"
        },
        "message": "Create styles.css and updated README",
        "tree": {
          "sha": "a639e96f9038797fba6e0469f94a4b0cc459fa68",
          "url": "https://api.github.com/repos/octocat/Spoon-Knife/git/trees/a639e96f9038797fba6e0469f94a4b0cc459fa68"
        },
        "url": "https://api.github.com/repos/octocat/Spoon-Knife/git/commits/bb4cc8d3b2e14b3af5df699876dd4ff3acd00b7f"
      },
      "committer": {},
      "html_url": "https://github.com/octocat/Spoon-Knife/commit/bb4cc8d3b2e14b3af5df699876dd4ff3acd00b7f",
      "node_id": "MDQ6VXNlcjU4MzIzMQ==",
      "parents": [
        {
          "html_url": "https://github.com/octocat/Spoon-Knife/commit/a30c19e3f13765a3b48829788bc1cb8b4e95cee4",
          "sha": "a30c19e3f13765a3b48829788bc1cb8b4e95cee4",
          "url": "https://api.github.com/repos/octocat/Spoon-Knife/commits/a30c19e3f13765a3b48829788bc1cb8b4e95cee4"
        }
      ],
      "repository": {
        "archive_url": "https://api.github.com/repos/octocat/Spoon-Knife/{archive_format}{/ref}",
        "assignees_url": "https://api.github.com/repos/octocat/Spoon-Knife/assignees{/user}",
        "blobs_url": "https://api.github.com/repos/octocat/Spoon-Knife/git/blobs{/sha}",
        "branches_url": "https://api.github.com/repos/octocat/Spoon-Knife/branches{/branch}",
        "collaborators_url": "https://api.github.com/repos/octocat/Spoon-Knife/collaborators{/collaborator}",
        "comments_url": "https://api.github.com/repos/octocat/Spoon-Knife/comments{/number}",
        "commits_url": "https://api.github.com/repos/octocat/Spoon-Knife/commits{/sha}",
        "compare_url": "https://api.github.com/repos/octocat/Spoon-Knife/compare/{base}...{head}",
        "contents_url": "https://api.github.com/repos/octocat/Spoon-Knife/contents/{+path}",
        "contributors_url": "https://api.github.com/repos/octocat/Spoon-Knife/contributors",
        "deployments_url": "https://api.github.com/repos/octocat/Spoon-Knife/deployments",
        "description": "This repo is for demonstration purposes only.",
        "downloads_url": "https://api.github.com/repos/octocat/Spoon-Knife/downloads",
        "events_url": "https://api.github.com/repos/octocat/Spoon-Knife/events",
        "fork": false,
        "forks_url": "https://api.github.com/repos/octocat/Spoon-Knife/forks",
        "full_name": "octocat/Spoon-Knife",
        "git_commits_url": "https://api.github.com/repos/octocat/Spoon-Knife/git/commits{/sha}",
        "git_refs_url": "https://api.github.com/repos/octocat/Spoon-Knife/git/refs{/sha}",
        "git_tags_url": "https://api.github.com/repos/octocat/Spoon-Knife/git/tags{/sha}",
        "hooks_url": "https://api.github.com/repos/octocat/Spoon-Knife/hooks",
        "html_url": "https://github.com/octocat/Spoon-Knife",
        "id": 1300192,
        "issue_comment_url": "https://api.github.com/repos/octocat/Spoon-Knife/issues/comments{/number}",
        "issue_events_url": "https://api.github.com/repos/octocat/Spoon-Knife/issues/events{/number}",
        "issues_url": "https://api.github.com/repos/octocat/Spoon-Knife/issues{/number}",
        "keys_url": "https://api.github.com/repos/octocat/Spoon-Knife/keys{/key_id}",
        "labels_url": "https://api.github.com/repos/octocat/Spoon-Knife/labels{/name}",
        "languages_url": "https://api.github.com/repos/octocat/Spoon-Knife/languages",
        "merges_url": "https://api.github.com/repos/octocat/Spoon-Knife/merges",
        "milestones_url": "https://api.github.com/repos/octocat/Spoon-Knife/milestones{/number}",
        "name": "Spoon-Knife",
        "node_id": "MDEwOlJlcG9zaXRvcnkxMzAwMTky",
        "notifications_url": "https://api.github.com/repos/octocat/Spoon-Knife/notifications{?since,all,participating}",
        "owner": {
          "avatar_url": "https://avatars.githubusercontent.com/u/583231?v=3",
          "events_url": "https://api.github.com/users/octocat/events{/privacy}",
          "followers_url": "https://api.github.com/users/octocat/followers",
          "following_url": "https://api.github.com/users/octocat/following{/other_user}",
          "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
          "gravatar_id": "",
          "html_url": "https://github.com/octocat",
          "id": 583231,
          "login": "octocat",
          "node_id": "MDQ6VXNlcjU4MzIzMQ==",
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
        "pulls_url": "https://api.github.com/repos/octocat/Spoon-Knife/pulls{/number}",
        "releases_url": "https://api.github.com/repos/octocat/Spoon-Knife/releases{/id}",
        "stargazers_url": "https://api.github.com/repos/octocat/Spoon-Knife/stargazers",
        "statuses_url": "https://api.github.com/repos/octocat/Spoon-Knife/statuses/{sha}",
        "subscribers_url": "https://api.github.com/repos/octocat/Spoon-Knife/subscribers",
        "subscription_url": "https://api.github.com/repos/octocat/Spoon-Knife/subscription",
        "tags_url": "https://api.github.com/repos/octocat/Spoon-Knife/tags",
        "teams_url": "https://api.github.com/repos/octocat/Spoon-Knife/teams",
        "trees_url": "https://api.github.com/repos/octocat/Spoon-Knife/git/trees{/sha}",
        "url": "https://api.github.com/repos/octocat/Spoon-Knife"
      },
      "score": 1,
      "sha": "bb4cc8d3b2e14b3af5df699876dd4ff3acd00b7f",
      "url": "https://api.github.com/repos/octocat/Spoon-Knife/commits/bb4cc8d3b2e14b3af5df699876dd4ff3acd00b7f"
    }
  ],
  "total_count": 1
}
    ```

    


=== "GET Search issues and pull requests"

    Find issues by state and keyword. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for issues, you can get text match metadata for the issue **title**, issue **body**, and issue **comment body** fields when you pass the `text-match` media type. For more details about how to receive highlighted
search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find the oldest unresolved Python bugs on Windows. Your query might look something like this.

`q=windows+label:bug+language:python+state:open&sort=created&order=asc`

This query searches for the keyword `windows`, within any open issue that is labeled as `bug`. The search runs across repositories whose primary language is Python. The results are sorted by creation date in ascending order, whick means the oldest issues appear first in the search results.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching issues and pull requests](https://help.github.com/articles/searching-issues-and-pull-requests/)" for a detailed list of qualifiers. | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query by the number of `comments`, `reactions`, `reactions-+1`, `reactions--1`, `reactions-smile`, `reactions-thinking_face`, `reactions-heart`, `reactions-tada`, or `interactions`. You can also sort results by how recently the items were `created` or `updated`, Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "assignee": null,
      "author_association": "collaborator",
      "body": "...",
      "closed_at": null,
      "comments": 15,
      "comments_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/comments",
      "created_at": "2009-07-12T20:10:41Z",
      "events_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/events",
      "html_url": "https://github.com/batterseapower/pinyin-toolkit/issues/132",
      "id": 35802,
      "labels": [
        {
          "color": "ff0000",
          "id": 4,
          "name": "bug",
          "node_id": "MDU6TGFiZWw0",
          "url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/labels/bug"
        }
      ],
      "labels_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132/labels{/name}",
      "locked": true,
      "milestone": {
        "closed_at": "2013-02-12T13:22:01Z",
        "closed_issues": 8,
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
        "description": "Tracking milestone for version 1.0",
        "due_on": "2012-10-09T23:39:01Z",
        "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
        "id": 1002604,
        "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
        "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
        "number": 1,
        "open_issues": 4,
        "state": "open",
        "title": "v1.0",
        "updated_at": "2014-03-03T18:58:10Z",
        "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1"
      },
      "node_id": "MDU6SXNzdWUzNTgwMg==",
      "number": 132,
      "pull_request": {
        "diff_url": "https://github.com/octocat/Hello-World/pull/1347.diff",
        "html_url": "https://github.com/octocat/Hello-World/pull/1347",
        "patch_url": "https://api.github.com/repos/octocat/Hello-World/pulls/1347",
        "url": "https://api/github.com/repos/octocat/Hello-World/pull/1347"
      },
      "repository_url": "https://api.github.com/repos/batterseapower/pinyin-toolkit",
      "score": 1,
      "state": "open",
      "title": "Line Number Indexes Beyond 20 Not Displayed",
      "updated_at": "2009-07-19T09:23:43Z",
      "url": "https://api.github.com/repos/batterseapower/pinyin-toolkit/issues/132",
      "user": {
        "avatar_url": "https://secure.gravatar.com/avatar/934442aadfe3b2f4630510de416c5718?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
        "events_url": "https://api.github.com/users/Nick3C/events{/privacy}",
        "followers_url": "https://api.github.com/users/Nick3C/followers",
        "following_url": "https://api.github.com/users/Nick3C/following{/other_user}",
        "gists_url": "https://api.github.com/users/Nick3C/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/Nick3C",
        "id": 90254,
        "login": "Nick3C",
        "node_id": "MDQ6VXNlcjkwMjU0",
        "organizations_url": "https://api.github.com/users/Nick3C/orgs",
        "received_events_url": "https://api.github.com/users/Nick3C/received_events",
        "repos_url": "https://api.github.com/users/Nick3C/repos",
        "site_admin": true,
        "starred_url": "https://api.github.com/users/Nick3C/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Nick3C/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/Nick3C"
      }
    }
  ],
  "total_count": 280
}
    ```

    


=== "GET Search labels"

    Find labels in a repository with names or descriptions that match search keywords. Returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for labels, you can get text match metadata for the label **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to find labels in the `linguist` repository that match `bug`, `defect`, or `enhancement`. Your query might look like this:

`q=bug+defect+enhancement&repository_id=64778136`

The labels that best match the query appear first in the search results.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `repository_id` | `string` | Yes | (Required) The id of the repository. | `<integer>` |
    | `q` | `string` | Yes | (Required) The search keywords. This endpoint does not accept qualifiers in the query. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query by when the label was `created` or `updated`. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "color": "84b6eb",
      "default": true,
      "description": "New feature or request.",
      "id": 418327088,
      "name": "enhancement",
      "node_id": "MDU6TGFiZWw0MTgzMjcwODg=",
      "score": 1,
      "url": "https://api.github.com/repos/octocat/linguist/labels/enhancement"
    },
    {
      "color": "ee0701",
      "default": true,
      "description": "Something isn\u0027t working.",
      "id": 418327086,
      "name": "bug",
      "node_id": "MDU6TGFiZWw0MTgzMjcwODY=",
      "score": 1,
      "url": "https://api.github.com/repos/octocat/linguist/labels/bug"
    }
  ],
  "total_count": 2
}
    ```

    


=== "GET Search repositories"

    Find repositories via various criteria. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for repositories, you can get text match metadata for the **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to search for popular Tetris repositories written in assembly code, your query might look like this:

`q=tetris+language:assembly&sort=stars&order=desc`

This query searches for repositories with the word `tetris` in the name, the description, or the README. The results are limited to repositories where the primary language is assembly. The results are sorted by stars in descending order, so that the most popular repositories appear first in the search results.

When you include the `mercy` preview header, you can also search for multiple topics by adding more `topic:` instances. For example, your query might look like this:

`q=topic:ruby+topic:rails`

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching for repositories](https://help.github.com/articles/searching-for-repositories/)" for a detailed list of qualifiers. | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query by number of `stars`, `forks`, or `help-wanted-issues` or how recently the items were `updated`. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "archive_url": "https://api.github.com/repos/dtrupenn/Tetris/{archive_format}{/ref}",
      "archived": true,
      "assignees_url": "https://api.github.com/repos/dtrupenn/Tetris/assignees{/user}",
      "blobs_url": "https://api.github.com/repos/dtrupenn/Tetris/git/blobs{/sha}",
      "branches_url": "https://api.github.com/repos/dtrupenn/Tetris/branches{/branch}",
      "clone_url": "https://github.com/dtrupenn/Tetris.git",
      "collaborators_url": "https://api.github.com/repos/dtrupenn/Tetris/collaborators{/collaborator}",
      "comments_url": "https://api.github.com/repos/dtrupenn/Tetris/comments{/number}",
      "commits_url": "https://api.github.com/repos/dtrupenn/Tetris/commits{/sha}",
      "compare_url": "https://api.github.com/repos/dtrupenn/Tetris/compare/{base}...{head}",
      "contents_url": "https://api.github.com/repos/dtrupenn/Tetris/contents/{+path}",
      "contributors_url": "https://api.github.com/repos/dtrupenn/Tetris/contributors",
      "created_at": "2012-01-01T00:31:50Z",
      "default_branch": "master",
      "deployments_url": "https://api.github.com/repos/dtrupenn/Tetris/deployments",
      "description": "A C implementation of Tetris using Pennsim through LC4",
      "disabled": true,
      "downloads_url": "https://api.github.com/repos/dtrupenn/Tetris/downloads",
      "events_url": "https://api.github.com/repos/dtrupenn/Tetris/events",
      "fork": false,
      "forks": 1,
      "forks_count": 0,
      "forks_url": "https://api.github.com/repos/dtrupenn/Tetris/forks",
      "full_name": "dtrupenn/Tetris",
      "git_commits_url": "https://api.github.com/repos/dtrupenn/Tetris/git/commits{/sha}",
      "git_refs_url": "https://api.github.com/repos/dtrupenn/Tetris/git/refs{/sha}",
      "git_tags_url": "https://api.github.com/repos/dtrupenn/Tetris/git/tags{/sha}",
      "git_url": "git:github.com/dtrupenn/Tetris.git",
      "has_downloads": true,
      "has_issues": true,
      "has_pages": true,
      "has_projects": true,
      "has_wiki": true,
      "homepage": "https://github.com",
      "hooks_url": "https://api.github.com/repos/dtrupenn/Tetris/hooks",
      "html_url": "https://github.com/dtrupenn/Tetris",
      "id": 3081286,
      "issue_comment_url": "https://api.github.com/repos/dtrupenn/Tetris/issues/comments{/number}",
      "issue_events_url": "https://api.github.com/repos/dtrupenn/Tetris/issues/events{/number}",
      "issues_url": "https://api.github.com/repos/dtrupenn/Tetris/issues{/number}",
      "keys_url": "https://api.github.com/repos/dtrupenn/Tetris/keys{/key_id}",
      "labels_url": "https://api.github.com/repos/dtrupenn/Tetris/labels{/name}",
      "language": "Assembly",
      "languages_url": "https://api.github.com/repos/dtrupenn/Tetris/languages",
      "license": {
        "html_url": "https://api.github.com/licenses/mit",
        "key": "mit",
        "name": "MIT License",
        "node_id": "MDc6TGljZW5zZW1pdA==",
        "spdx_id": "MIT",
        "url": "https://api.github.com/licenses/mit"
      },
      "master_branch": "master",
      "merges_url": "https://api.github.com/repos/dtrupenn/Tetris/merges",
      "milestones_url": "https://api.github.com/repos/dtrupenn/Tetris/milestones{/number}",
      "mirror_url": "git:git.example.com/dtrupenn/Tetris",
      "name": "Tetris",
      "node_id": "MDEwOlJlcG9zaXRvcnkzMDgxMjg2",
      "notifications_url": "https://api.github.com/repos/dtrupenn/Tetris/notifications{?since,all,participating}",
      "open_issues": 1,
      "open_issues_count": 0,
      "owner": {
        "avatar_url": "https://secure.gravatar.com/avatar/e7956084e75f239de85d3a31bc172ace?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
        "events_url": "https://api.github.com/users/octocat/events{/privacy}",
        "followers_url": "https://api.github.com/users/octocat/followers",
        "following_url": "https://api.github.com/users/octocat/following{/other_user}",
        "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/octocat",
        "id": 872147,
        "login": "dtrupenn",
        "node_id": "MDQ6VXNlcjg3MjE0Nw==",
        "organizations_url": "https://api.github.com/users/octocat/orgs",
        "received_events_url": "https://api.github.com/users/dtrupenn/received_events",
        "repos_url": "https://api.github.com/users/octocat/repos",
        "site_admin": true,
        "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
        "type": "User",
        "url": "https://api.github.com/users/dtrupenn"
      },
      "private": false,
      "pulls_url": "https://api.github.com/repos/dtrupenn/Tetris/pulls{/number}",
      "pushed_at": "2012-01-01T00:37:02Z",
      "releases_url": "https://api.github.com/repos/dtrupenn/Tetris/releases{/id}",
      "score": 1,
      "size": 524,
      "ssh_url": "git@github.com:dtrupenn/Tetris.git",
      "stargazers_count": 1,
      "stargazers_url": "https://api.github.com/repos/dtrupenn/Tetris/stargazers",
      "statuses_url": "https://api.github.com/repos/dtrupenn/Tetris/statuses/{sha}",
      "subscribers_url": "https://api.github.com/repos/dtrupenn/Tetris/subscribers",
      "subscription_url": "https://api.github.com/repos/dtrupenn/Tetris/subscription",
      "svn_url": "https://svn.github.com/dtrupenn/Tetris",
      "tags_url": "https://api.github.com/repos/dtrupenn/Tetris/tags",
      "teams_url": "https://api.github.com/repos/dtrupenn/Tetris/teams",
      "trees_url": "https://api.github.com/repos/dtrupenn/Tetris/git/trees{/sha}",
      "updated_at": "2013-01-05T17:58:47Z",
      "url": "https://api.github.com/repos/dtrupenn/Tetris",
      "watchers": 1,
      "watchers_count": 1
    }
  ],
  "total_count": 40
}
    ```

    


=== "GET Search topics"

    Find topics via various criteria. Results are sorted by best match. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination). See "[Searching topics](https://help.github.com/articles/searching-topics/)" for a detailed list of qualifiers.

When searching for topics, you can get text match metadata for the topic's **short\_description**, **description**, **name**, or **display\_name** field when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you want to search for topics related to Ruby that are featured on https://github.com/topics. Your query might look like this:

`q=ruby+is:featured`

This query searches for topics with the keyword `ruby` and limits the results to find only topics that are featured. The topics that are the best match for the query appear first in the search results.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "created_at": "2016-11-28T22:03:59Z",
      "created_by": "Yukihiro Matsumoto",
      "curated": true,
      "description": "Ruby was developed by\u00a0Yukihiro \"Matz\" Matsumoto\u00a0in 1995 with the intent of having an easily readable programming language. It is integrated with the Rails framework to create dynamic web-applications. Ruby\u0027s syntax is similar to that of Perl and Python.",
      "display_name": "Ruby",
      "featured": true,
      "name": "ruby",
      "released": "December 21, 1995",
      "score": 1,
      "short_description": "Ruby is a scripting language designed for simplified object-oriented programming.",
      "updated_at": "2017-10-30T18:16:32Z"
    },
    {
      "created_at": "2016-12-09T17:03:50Z",
      "created_by": "David Heinemeier Hansson",
      "curated": true,
      "description": "Ruby on Rails (Rails) is a web application framework written in Ruby. It is meant to help simplify the building of complex websites.",
      "display_name": "Rails",
      "featured": true,
      "name": "rails",
      "released": "December 13 2005",
      "score": 1,
      "short_description": "Ruby on Rails (Rails) is a web application framework written in Ruby.",
      "updated_at": "2017-10-30T16:20:19Z"
    },
    {
      "created_at": "2016-12-07T00:07:02Z",
      "created_by": "Guido van Rossum",
      "curated": true,
      "description": "Python is a dynamically typed programming language designed by Guido Van Rossum. Much like the programming language Ruby, Python was designed to be easily read by programmers. Because of its large following and many libraries, Python can be implemented and used to do anything from webpages to scientific research.",
      "display_name": "Python",
      "featured": true,
      "name": "python",
      "released": "February 20, 1991",
      "score": 1,
      "short_description": "Python is a dynamically typed programming language.",
      "updated_at": "2017-10-27T22:45:43Z"
    },
    {
      "created_at": "2016-12-16T21:53:08Z",
      "created_by": "Tom Preston-Werner",
      "curated": true,
      "description": "Jekyll is a blog-aware, site generator written in Ruby. It takes raw text files, runs it through a renderer and produces a publishable static website.",
      "display_name": "Jekyll",
      "featured": true,
      "name": "jekyll",
      "released": "2008",
      "score": 1,
      "short_description": "Jekyll is a simple, blog-aware static site generator.",
      "updated_at": "2017-10-27T19:00:24Z"
    },
    {
      "created_at": "2016-12-16T21:53:45Z",
      "created_by": "Hampton Catlin, Natalie Weizenbaum, Chris Eppstein",
      "curated": true,
      "description": "Sass is a stylesheet language with a main implementation in Ruby. It is an extension of CSS that makes improvements to the old stylesheet format, such as being able to declare variables and using a cleaner nesting syntax.",
      "display_name": "Sass",
      "featured": true,
      "name": "sass",
      "released": "November 28, 2006",
      "score": 1,
      "short_description": "Sass is a stable extension to classic CSS.",
      "updated_at": "2018-01-16T16:30:40Z"
    },
    {
      "created_at": "2016-12-17T20:30:44Z",
      "created_by": "Max Howell",
      "curated": true,
      "description": "Homebrew is a package manager for Apple\u0027s macOS operating system. It simplifies the installation of software and is popular in the Ruby on Rails community.",
      "display_name": "Homebrew",
      "featured": true,
      "name": "homebrew",
      "released": "2009",
      "score": 1,
      "short_description": "Homebrew is a package manager for macOS.",
      "updated_at": "2018-02-06T16:14:56Z"
    }
  ],
  "total_count": 6
}
    ```

    


=== "GET Search users"

    Find users via various criteria. This method returns up to 100 results [per page](https://developer.github.com/v3/#pagination).

When searching for users, you can get text match metadata for the issue **login**, **email**, and **name** fields when you pass the `text-match` media type. For more details about highlighting search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata). For more details about how to receive highlighted search results, see [Text match metadata](https://developer.github.com/v3/search/#text-match-metadata).

For example, if you're looking for a list of popular users, you might try this query:

`q=tom+repos:%3E42+followers:%3E1000`

This query searches for users with the name `tom`. The results are restricted to users with more than 42 repositories and over 1,000 followers.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `q` | `string` | Yes | (Required) The query contains one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as GitHub.com. To learn more about the format of the query, see [Constructing a search query](https://developer.github.com/v3/search/#constructing-a-search-query). See "[Searching users](https://help.github.com/articles/searching-users/)" for a detailed list of qualifiers. | `<string>` |
    | `sort` | `string` | Yes | Sorts the results of your query by number of `followers` or `repositories`, or when the person `joined` GitHub. Default: [best match](https://developer.github.com/v3/search/#ranking-search-results) | `<string>` |
    | `order` | `string` | Yes | Determines whether the first search result returned is the highest number of matches (`desc`) or lowest number of matches (`asc`). This parameter is ignored unless you provide `sort`. | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    {
  "incomplete_results": false,
  "items": [
    {
      "avatar_url": "https://secure.gravatar.com/avatar/25c7c18223fb42a4c6ae1c8db6f50f9b?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-user-420.png",
      "events_url": "https://api.github.com/users/mojombo/events{/privacy}",
      "followers_url": "https://api.github.com/users/mojombo/followers",
      "following_url": "https://api.github.com/users/mojombo/following{/other_user}",
      "gists_url": "https://api.github.com/users/mojombo/gists{/gist_id}",
      "gravatar_id": "",
      "html_url": "https://github.com/mojombo",
      "id": 1,
      "login": "mojombo",
      "node_id": "MDQ6VXNlcjE=",
      "organizations_url": "https://api.github.com/users/mojombo/orgs",
      "received_events_url": "https://api.github.com/users/mojombo/received_events",
      "repos_url": "https://api.github.com/users/mojombo/repos",
      "score": 1,
      "site_admin": true,
      "starred_url": "https://api.github.com/users/mojombo/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/mojombo/subscriptions",
      "type": "User",
      "url": "https://api.github.com/users/mojombo"
    }
  ],
  "total_count": 12
}
    ```

    

