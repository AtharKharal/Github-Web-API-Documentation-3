# orgs/{org} API


=== "GET Get a self-hosted runner for an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Gets a specific self-hosted runner for an organization. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:runner_id` | `string` | Yes | (Required) runner_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "id": 23,
  "name": "MBP",
  "os": "macos",
  "status": "online"
}
    ```

    


=== "DELETE Delete a self-hosted runner from an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:runner_id` | `string` | Yes | (Required) runner_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List self-hosted runners for an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Lists all self-hosted runners for an organization. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "runners": [
    {
      "id": 23,
      "name": "MBP",
      "os": "macos",
      "status": "online"
    },
    {
      "id": 24,
      "name": "iMac",
      "os": "macos",
      "status": "offline"
    }
  ],
  "total_count": 2
}
    ```

    


=== "GET List runner applications for an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.

Lists binaries for the runner application that you can download and run. You must authenticate using an access token with the `admin:org` scope to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-osx-x64-2.164.0.tar.gz",
    "filename": "actions-runner-osx-x64-2.164.0.tar.gz",
    "os": "osx"
  },
  {
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-x64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-x64-2.164.0.tar.gz",
    "os": "linux"
  },
  {
    "architecture": "arm",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm-2.164.0.tar.gz",
    "os": "linux"
  },
  {
    "architecture": "x64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-win-x64-2.164.0.zip",
    "filename": "actions-runner-win-x64-2.164.0.zip",
    "os": "win"
  },
  {
    "architecture": "arm64",
    "download_url": "https://github.com/actions/runner/releases/download/v2.164.0/actions-runner-linux-arm64-2.164.0.tar.gz",
    "filename": "actions-runner-linux-arm64-2.164.0.tar.gz",
    "os": "linux"
  }
]
    ```

    


=== "POST Create a registration token for an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.


Returns a token that you can pass to the `config` script. The token expires after one hour. You must authenticate
using an access token with the `admin:org` scope to use this endpoint.

#### Example using registration token

Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.

```
./config.sh --url https://github.com/octo-org --token TOKEN
```

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "expires_at": "2020-01-22T12:13:35.123-08:00",
  "token": "LLBF3JGZDX3P5PMEXLND6TS6FCWO6"
}
    ```

    


=== "POST Create a remove token for an organization"

    **Warning:** The self-hosted runners API for organizations is currently in public beta and subject to change.


Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The
token expires after one hour. You must authenticate using an access token with the `admin:org` scope to use this
endpoint.

#### Example using remove token

To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token provided by this
endpoint.

```
./config.sh remove --token TOKEN
```

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "expires_at": "2020-01-29T12:13:35.123-08:00",
  "token": "AABF3JGZDX3P5PMEXLND6TS6FCWO6"
}
    ```

    


=== "PUT Add selected repository to an organization secret"

    Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://developer.github.com/v3/actions/secrets/#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    | `:repository_id` | `string` | Yes | (Required) repository_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove selected repository from an organization secret"

    Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://developer.github.com/v3/actions/secrets/#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    | `:repository_id` | `string` | Yes | (Required) repository_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List selected repositories for an organization secret"

    Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "repositories": [
    {
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
    }
  ],
  "total_count": 1
}
    ```

    


=== "PUT Set selected repositories for an organization secret"

    Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://developer.github.com/v3/actions/secrets/#create-or-update-an-organization-secret). You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "selected_repository_ids": [
    "\u003cinteger\u003e",
    "\u003cinteger\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get an organization secret"

    Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "created_at": "2019-08-10T14:59:22Z",
  "name": "GH_TOKEN",
  "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/secrets/SUPER_SECRET/repositories",
  "updated_at": "2020-01-10T14:59:22Z",
  "visibility": "selected"
}
    ```

    


=== "PUT Create or update an organization secret"

    Creates or updates an organization secret with an encrypted value. Encrypt your secret using
[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access
token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to
use this endpoint.

#### Example encrypting a secret using Node.js

Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.

```
const sodium = require('tweetsodium');

const key = "base64-encoded-public-key";
const value = "plain-text-secret";

// Convert the message and key to Uint8Array's (Buffer implements that interface)
const messageBytes = Buffer.from(value);
const keyBytes = Buffer.from(key, 'base64');

// Encrypt using LibSodium.
const encryptedBytes = sodium.seal(messageBytes, keyBytes);

// Base64 the encrypted secret
const encrypted = Buffer.from(encryptedBytes).toString('base64');

console.log(encrypted);
```


#### Example encrypting a secret using Python

Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.

```
from base64 import b64encode
from nacl import encoding, public

def encrypt(public_key: str, secret_value: str) -> str:
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")
```

#### Example encrypting a secret using C#

Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.

```
var secretValue = System.Text.Encoding.UTF8.GetBytes("mySecret");
var publicKey = Convert.FromBase64String("2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU=");

var sealedPublicKeyBox = Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);

Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox));
```

#### Example encrypting a secret using Ruby

Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.

```ruby
require "rbnacl"
require "base64"

key = Base64.decode64("+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0=")
public_key = RbNaCl::PublicKey.new(key)

box = RbNaCl::Boxes::Sealed.from_public_key(public_key)
encrypted_secret = box.encrypt("my_secret")

# Print the base64 encoded secret
puts Base64.strict_encode64(encrypted_secret)
```

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "encrypted_value": "\u003cstring\u003e",
  "key_id": "\u003cstring\u003e",
  "selected_repository_ids": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "visibility": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "raw": ""
}
    ```

    


=== "DELETE Delete an organization secret"

    Deletes a secret in an organization using the secret name. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:secret_name` | `string` | Yes | (Required) secret_name parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List organization secrets"

    Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "secrets": [
    {
      "created_at": "2019-08-10T14:59:22Z",
      "name": "GIST_ID",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "private"
    },
    {
      "created_at": "2019-08-10T14:59:22Z",
      "name": "DEPLOY_TOKEN",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "all"
    },
    {
      "created_at": "2019-08-10T14:59:22Z",
      "name": "GH_TOKEN",
      "selected_repositories_url": "https://api.github.com/orgs/octo-org/actions/secrets/SUPER_SECRET/repositories",
      "updated_at": "2020-01-10T14:59:22Z",
      "visibility": "selected"
    }
  ],
  "total_count": 3
}
    ```

    


=== "GET Get an organization public key"

    Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `secrets` organization permission to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "key": "2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234",
  "key_id": "012345678912345678"
}
    ```

    


=== "GET Check if a user is blocked by an organization"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "PUT Block a user from an organization"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Unblock a user from an organization"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List users blocked by an organization"

    List the users blocked by an organization.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "GET List SAML SSO authorizations for an organization"

    Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products).

An authenticated organization owner with the `read:org` scope can list all credential authorizations for an organization that uses SAML single sign-on (SSO). The credentials are either personal access tokens or SSH keys that organization members have authorized for the organization. For more information, see [About authentication with SAML single sign-on](https://help.github.com/en/articles/about-authentication-with-saml-single-sign-on).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "credential_authorized_at": "2011-01-26T19:06:43Z",
    "credential_id": 161195,
    "credential_type": "personal access token",
    "login": "octocat",
    "scopes": [
      "user",
      "repo"
    ],
    "token_last_eight": "71c3fc11"
  },
  {
    "credential_authorized_at": "2019-03-29T19:06:43Z",
    "credential_id": 161196,
    "credential_type": "personal access token",
    "login": "hubot",
    "scopes": [
      "repo"
    ],
    "token_last_eight": "12345678"
  }
]
    ```

    


=== "DELETE Remove a SAML SSO authorization for an organization"

    Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products).

An authenticated organization owner with the `admin:org` scope can remove a credential authorization for an organization that uses SAML SSO. Once you remove someone's credential authorization, they will need to create a new personal access token or SSH key and authorize it for the organization they want to access.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:credential_id` | `string` | Yes | (Required) credential_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get an organization webhook"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:hook_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "active": true,
  "config": {
    "content_type": "json",
    "url": "http://example.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "events": [
    "push",
    "pull_request"
  ],
  "id": 1,
  "name": "web",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "type": "Organization",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/orgs/octocat/hooks/1"
}
    ```

    


=== "PATCH Update an organization webhook"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:hook_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "active": true,
  "config": {
    "content_type": "\u003cstring\u003e",
    "insecure_ssl": "\u003cstring\u003e",
    "secret": "\u003cstring\u003e",
    "url": "\u003cstring\u003e"
  },
  "events": [
    "push"
  ],
  "name": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "active": true,
  "config": {
    "content_type": "json",
    "url": "http://example.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "events": [
    "pull_request"
  ],
  "id": 1,
  "name": "web",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "type": "Organization",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/orgs/octocat/hooks/1"
}
    ```

    


=== "DELETE Delete an organization webhook"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:hook_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "POST Ping an organization webhook"

    This will trigger a [ping event](https://developer.github.com/webhooks/#ping-event) to be sent to the hook.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:hook_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List organization webhooks"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "active": true,
    "config": {
      "content_type": "json",
      "url": "http://example.com"
    },
    "created_at": "2011-09-06T17:26:27Z",
    "events": [
      "push",
      "pull_request"
    ],
    "id": 1,
    "name": "web",
    "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
    "type": "Organization",
    "updated_at": "2011-09-06T20:39:23Z",
    "url": "https://api.github.com/orgs/octocat/hooks/1"
  }
]
    ```

    


=== "POST Create an organization webhook"

    Here's how you can create a hook that posts payloads in JSON format:

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "active": true,
  "config": {
    "content_type": "\u003cstring\u003e",
    "insecure_ssl": "\u003cstring\u003e",
    "password": "\u003cstring\u003e",
    "secret": "\u003cstring\u003e",
    "url": "\u003cstring\u003e",
    "username": "\u003cstring\u003e"
  },
  "events": [
    "push"
  ],
  "name": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "active": true,
  "config": {
    "content_type": "json",
    "url": "http://example.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "events": [
    "push",
    "pull_request"
  ],
  "id": 1,
  "name": "web",
  "ping_url": "https://api.github.com/orgs/octocat/hooks/1/pings",
  "type": "Organization",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/orgs/octocat/hooks/1"
}
    ```

    


=== "GET Get interaction restrictions for an organization"

    Shows which group of GitHub users can interact with this organization and when the restriction expires. If there are no restrictions, you will see an empty response.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "expires_at": "2018-08-17T04:18:39Z",
  "limit": "collaborators_only",
  "origin": "organization"
}
    ```

    


=== "PUT Set interaction restrictions for an organization"

    Temporarily restricts interactions to certain GitHub users in any public repository in the given organization. You must be an organization owner to set these restrictions.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "limit": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "expires_at": "2018-08-17T04:18:39Z",
  "limit": "collaborators_only",
  "origin": "organization"
}
    ```

    


=== "DELETE Remove interaction restrictions for an organization"

    Removes all interaction restrictions from public repositories in the given organization. You must be an organization owner to remove restrictions.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List pending organization invitations"

    The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "POST Create an organization invitation"

    Invite people to an organization by using their GitHub user ID or their email address. In order to create invitations in an organization, the authenticated user must be an organization owner.

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "email": "\u003cstring\u003e",
  "invitee_id": "\u003cinteger\u003e",
  "role": "direct_member",
  "team_ids": [
    "\u003cinteger\u003e",
    "\u003cinteger\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
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
    ```

    


=== "GET List organization invitation teams"

    List all teams associated with an invitation. In order to see invitations in an organization, the authenticated user must be an organization owner.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:invitation_id` | `string` | Yes | (Required) invitation_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "description": "A great team.",
    "html_url": "https://api.github.com/teams/justice-league",
    "id": 1,
    "members_url": "https://api.github.com/teams/1/members{/member}",
    "name": "Justice League",
    "node_id": "MDQ6VGVhbTE=",
    "parent": null,
    "permission": "admin",
    "privacy": "closed",
    "repositories_url": "https://api.github.com/teams/1/repos",
    "slug": "justice-league",
    "url": "https://api.github.com/teams/1"
  }
]
    ```

    


=== "GET Check organization membership for a user"

    Check if a user is, publicly or privately, a member of the organization.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove an organization member"

    Removing a user from this list will remove them from all teams and they will no longer have any access to the organization's repositories.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List organization members"

    List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `filter` | `string` | Yes | Filter members returned in the list. Can be one of:  
\* `2fa_disabled` - Members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled. Available for organization owners.  
\* `all` - All members the authenticated user can see. | `all` |
    | `role` | `string` | Yes | Filter members returned by their role. Can be one of:  
\* `all` - All members of the organization, regardless of role.  
\* `admin` - Organization owners.  
\* `member` - Non-owner organization members. | `all` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "GET Get organization membership for a user"

    In order to get a user's membership with an organization, the authenticated user must be an organization member.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "organization": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "description": "A great organization",
    "events_url": "https://api.github.com/orgs/github/events",
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "id": 1,
    "issues_url": "https://api.github.com/orgs/github/issues",
    "login": "github",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "url": "https://api.github.com/orgs/github"
  },
  "organization_url": "https://api.github.com/orgs/octocat",
  "role": "admin",
  "state": "active",
  "url": "https://api.github.com/orgs/octocat/memberships/defunkt",
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

    


=== "PUT Set organization membership for a user"

    Only authenticated organization owners can add a member to the organization or update the member's role.

*   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user's [membership status](https://developer.github.com/v3/orgs/members/#get-organization-membership-for-a-user) will be `pending` until they accept the invitation.
    
*   Authenticated users can _update_ a user's membership by passing the `role` parameter. If the authenticated user changes a member's role to `admin`, the affected user will receive an email notifying them that they've been made an organization owner. If the authenticated user changes an owner's role to `member`, no email will be sent.

**Rate limits**

To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
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
  "organization": {
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "description": "A great organization",
    "events_url": "https://api.github.com/orgs/github/events",
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "id": 1,
    "issues_url": "https://api.github.com/orgs/github/issues",
    "login": "github",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "url": "https://api.github.com/orgs/github"
  },
  "organization_url": "https://api.github.com/orgs/invitocat",
  "role": "admin",
  "state": "pending",
  "url": "https://api.github.com/orgs/invitocat/memberships/defunkt",
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

    


=== "DELETE Remove organization membership for a user"

    In order to remove a user's membership with an organization, the authenticated user must be an organization owner.

If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Download an organization migration archive"

    Fetches the URL to a migration archive.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:migration_id` | `string` | Yes | (Required) migration_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Delete an organization migration archive"

    Deletes a previous migration archive. Migration archives are automatically deleted after seven days.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:migration_id` | `string` | Yes | (Required) migration_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get an organization migration status"

    Fetches the status of a migration.

The `state` of a migration can be one of the following values:

*   `pending`, which means the migration hasn't started yet.
*   `exporting`, which means the migration is in progress.
*   `exported`, which means the migration finished successfully.
*   `failed`, which means the migration failed.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:migration_id` | `string` | Yes | (Required) migration_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "created_at": "2015-07-06T15:33:38-07:00",
  "exclude_attachments": false,
  "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
  "id": 79,
  "lock_repositories": true,
  "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
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
  ],
  "state": "exported",
  "updated_at": "2015-07-06T15:33:38-07:00",
  "url": "https://api.github.com/orgs/octo-org/migrations/79"
}
    ```

    


=== "DELETE Unlock an organization repository"

    Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://developer.github.com/v3/repos/#delete-a-repository) when the migration is complete and you no longer need the source data.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:migration_id` | `string` | Yes | (Required) migration_id parameter | `<integer>` |
    | `:repo_name` | `string` | Yes | (Required) repo_name parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List repositories in an organization migration"

    List all the repositories for this organization migration.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:migration_id` | `string` | Yes | (Required) migration_id parameter | `<integer>` |
    
    

    

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

    


=== "GET List organization migrations"

    Lists the most recent migrations.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "created_at": "2015-07-06T15:33:38-07:00",
    "exclude_attachments": false,
    "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
    "id": 79,
    "lock_repositories": true,
    "node_id": "MDQ6VXNlcjE=",
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
    ],
    "state": "pending",
    "updated_at": "2015-07-06T15:33:38-07:00",
    "url": "https://api.github.com/orgs/octo-org/migrations/79"
  }
]
    ```

    


=== "POST Start an organization migration"

    Initiates the generation of a migration archive.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "exclude": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "exclude_attachments": false,
  "lock_repositories": false,
  "repositories": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "created_at": "2015-07-06T15:33:38-07:00",
  "exclude_attachments": false,
  "guid": "0b989ba4-242f-11e5-81e1-c7b6966d2516",
  "id": 79,
  "lock_repositories": true,
  "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
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
  ],
  "state": "pending",
  "updated_at": "2015-07-06T15:33:38-07:00",
  "url": "https://api.github.com/orgs/octo-org/migrations/79"
}
    ```

    


=== "PUT Convert an organization member to outside collaborator"

    When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)".

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove outside collaborator from an organization"

    Removing a user from this list will remove them from all the organization's repositories.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List outside collaborators for an organization"

    List all users who are outside collaborators of an organization.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `filter` | `string` | Yes | Filter the list of outside collaborators. Can be one of:  
\* `2fa_disabled`: Outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled.  
\* `all`: All outside collaborators. | `all` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "GET List organization projects"

    Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `state` | `string` | Yes | Indicates the state of the projects to return. Can be either `open`, `closed`, or `all`. | `open` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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
    "owner_url": "https://api.github.com/orgs/octocat",
    "state": "open",
    "updated_at": "2014-03-04T18:58:10Z",
    "url": "https://api.github.com/projects/1002605"
  }
]
    ```

    


=== "POST Create an organization project"

    Creates an organization project board. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "body": "\u003cstring\u003e",
  "name": "\u003cstring\u003e"
}
    ```
    

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
  "owner_url": "https://api.github.com/orgs/octocat",
  "state": "open",
  "updated_at": "2014-03-04T18:58:10Z",
  "url": "https://api.github.com/projects/1002605"
}
    ```

    


=== "GET Check public organization membership for a user"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "PUT Set public organization membership for the authenticated user"

    The user can publicize their own membership. (A user cannot publicize the membership for another user.)

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://developer.github.com/v3/#http-verbs)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "DELETE Remove public organization membership for the authenticated user"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List public organization members"

    Members of an organization can choose to have their membership publicized or not.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "GET List organization repositories"

    Lists repositories for the specified organization.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `type` | `string` | Yes | Specifies the types of repositories you want returned. Can be one of `all`, `public`, `private`, `forks`, `sources`, `member`, `internal`. Default: `all`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, `type` can also be `internal`. | `<string>` |
    | `sort` | `string` | Yes | Can be one of `created`, `updated`, `pushed`, `full_name`. | `created` |
    | `direction` | `string` | Yes | Can be one of `asc` or `desc`. Default: when using `full_name`: `asc`, otherwise `desc` | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    


=== "POST Create an organization repository"

    Creates a new repository in the specified organization. The authenticated user must be a member of the organization.

**OAuth scope requirements**

When using [OAuth](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:

*   `public_repo` scope or `repo` scope to create a public repository
*   `repo` scope to create a private repository

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "allow_merge_commit": true,
  "allow_rebase_merge": true,
  "allow_squash_merge": true,
  "auto_init": false,
  "delete_branch_on_merge": false,
  "description": "\u003cstring\u003e",
  "gitignore_template": "\u003cstring\u003e",
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true,
  "homepage": "\u003cstring\u003e",
  "is_template": false,
  "license_template": "\u003cstring\u003e",
  "name": "\u003cstring\u003e",
  "private": false,
  "team_id": "\u003cinteger\u003e",
  "visibility": "\u003cstring\u003e"
}
    ```
    

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
  "forks": 9,
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
  "open_issues": 0,
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
  "watchers": 80,
  "watchers_count": 80
}
    ```

    


=== "GET Get GitHub Actions billing for an organization"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the summary of the free and paid GitHub Actions minutes used.

Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

Access tokens must have the `read:org` scope.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "included_minutes": 3000,
  "minutes_used_breakdown": {
    "MACOS": 10,
    "UBUNTU": 205,
    "WINDOWS": 90
  },
  "total_minutes_used": 305,
  "total_paid_minutes_used": 0
}
    ```

    


=== "GET Get GitHub Packages billing for an organization"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the free and paid storage usued for GitHub Packages in gigabytes.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

Access tokens must have the `read:org` scope.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "included_gigabytes_bandwidth": 10,
  "total_gigabytes_bandwidth_used": 50,
  "total_paid_gigabytes_bandwidth_used": 40
}
    ```

    


=== "GET Get shared storage billing for an organization"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the estimated paid and estimated total storage used for GitHub Actions and Github Packages.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

Access tokens must have the `read:org` scope.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "days_left_in_billing_cycle": 20,
  "estimated_paid_storage_for_month": 15,
  "estimated_storage_for_month": 40
}
    ```

    


=== "GET List reactions for a team discussion comment"

    List the reactions to a [team discussion comment](https://developer.github.com/v3/teams/discussion_comments/). OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `content` | `string` | Yes | Returns a single [reaction type](https://developer.github.com/v3/reactions/#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "POST Create reaction for a team discussion comment"

    Create a reaction to a [team discussion comment](https://developer.github.com/v3/teams/discussion_comments/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with a `Status: 200 OK` means that you already added the reaction type to this team discussion comment.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Delete team discussion comment reaction"

    **Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.

Delete a reaction to a [team discussion comment](https://developer.github.com/v3/teams/discussion_comments/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:reaction_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get a discussion comment"

    Get a specific comment on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "PATCH Update a discussion comment"

    Edits the body text of a discussion comment. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Delete a discussion comment"

    Deletes a comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:comment_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List discussion comments"

    List all comments on a team discussion. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `direction` | `string` | Yes | One of `asc` (ascending) or `desc` (descending). | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "POST Create a discussion comment"

    Creates a new comment on a team discussion. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "GET List reactions for a team discussion"

    List the reactions to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `content` | `string` | Yes | Returns a single [reaction type](https://developer.github.com/v3/reactions/#reaction-types). Omit this parameter to list all reactions to a team discussion. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "POST Create reaction for a team discussion"

    Create a reaction to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with a `Status: 200 OK` means that you already added the reaction type to this team discussion.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Delete team discussion reaction"

    **Note:** You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id`.

Delete a reaction to a [team discussion](https://developer.github.com/v3/teams/discussions/). OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    | `:reaction_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Get a discussion"

    Get a specific discussion on a team's page. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "PATCH Update a discussion"

    Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Delete a discussion"

    Delete a discussion from a team's page. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:discussion_number` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List discussions"

    List all discussions on a team's page. OAuth access tokens require the `read:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `direction` | `string` | Yes | One of `asc` (ascending) or `desc` (descending). | `desc` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "POST Create a discussion"

    Creates a new discussion post on a team's page. OAuth access tokens require the `write:discussion` [scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

This endpoint triggers [notifications](https://help.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in abuse rate limiting. See "[Abuse rate limits](https://developer.github.com/v3/#abuse-rate-limits)" and "[Dealing with abuse rate limits](https://developer.github.com/v3/guides/best-practices-for-integrators/#dealing-with-abuse-rate-limits)" for details.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    
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

    


=== "GET Get team membership for a user"

    Team members will include the members of child teams.

To get a user's membership with a team, the team must be visible to the authenticated user.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.

**Note:** The `role` for organization owners returns as `maintainer`. For more information about `maintainer` roles, see [Create a team](https://developer.github.com/v3/teams/#create-a-team).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "role": "member",
  "state": "active",
  "url": "https://api.github.com/teams/1/memberships/octocat"
}
    ```

    


=== "PUT Add or update team membership for a user"

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

An organization owner can add someone who is not part of the team's organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the "pending" state until the person accepts the invitation, at which point the membership will transition to the "active" state and the user will be added as a member of the team.

If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/memberships/{username}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Remove team membership for a user"

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:username` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET Check team permissions for a project"

    Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "PUT Add or update team project permissions"

    Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Remove a project from a team"

    Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. This endpoint removes the project from the team, but does not delete the project.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:project_id` | `string` | Yes | (Required)  | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List team projects"

    Lists the organization projects for a team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "GET Check team permissions for a repository"

    Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.

You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://developer.github.com/v3/media/) via the `application/vnd.github.v3.repository+json` accept header.

If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "PUT Add or update team repository permissions"

    To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://developer.github.com/v3/#http-verbs)."

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

For more information about the permission levels, see "[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
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

    


=== "DELETE Remove a repository from a team"

    If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    | `:owner` | `string` | Yes | (Required)  | `<string>` |
    | `:repo` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List team repositories"

    Lists a team's repositories visible to the authenticated user.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "GET List IdP groups for a team"

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

List IdP groups connected to a team on GitHub.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/team-sync/group-mappings`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "PATCH Create or update IdP group connections"

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

Creates, updates, or removes a connection between a team and an IdP group. When adding groups to a team, you must include all new and existing groups to avoid replacing existing groups with the new ones. Specifying an empty `groups` array will remove all connections for a team.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/team-sync/group-mappings`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "groups": [
    {
      "group_description": "\u003cstring\u003e",
      "group_id": "\u003cstring\u003e",
      "group_name": "\u003cstring\u003e"
    },
    {
      "group_description": "\u003cstring\u003e",
      "group_id": "\u003cstring\u003e",
      "group_name": "\u003cstring\u003e"
    }
  ]
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
    },
    {
      "group_description": "The people who make your octoworld come to life.",
      "group_id": "456",
      "group_name": "Octocat docs members"
    }
  ]
}
    ```

    


=== "GET Get a team by name"

    Gets a team using the team's `slug`. GitHub generates the `slug` from the team `name`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "PATCH Update a team"

    To edit a team, the authenticated user must either be an organization owner or a team maintainer.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    
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

    


=== "DELETE Delete a team"

    To delete a team, the authenticated user must be an organization owner or team maintainer.

If you are an organization owner, deleting a parent team will delete all of its child teams as well.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List pending team invitations"

    The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/invitations`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "GET List team members"

    Team members will include the members of child teams.

To list members in a team, the team must be visible to the authenticated user.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `role` | `string` | Yes | Filters members returned by their role in the team. Can be one of:  
\* `member` - normal members of the team.  
\* `maintainer` - team maintainers.  
\* `all` - all members of the team. | `all` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "GET List child teams"

    Lists the child teams of the team specified by `{team_slug}`.

**Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    | `:team_slug` | `string` | Yes | (Required) team_slug parameter | `<string>` |
    
    

    

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

    


=== "GET List teams"

    Lists all teams in an organization that are visible to the authenticated user.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "description": "A great team.",
    "html_url": "https://api.github.com/teams/justice-league",
    "id": 1,
    "members_url": "https://api.github.com/teams/1/members{/member}",
    "name": "Justice League",
    "node_id": "MDQ6VGVhbTE=",
    "parent": null,
    "permission": "admin",
    "privacy": "closed",
    "repositories_url": "https://api.github.com/teams/1/repos",
    "slug": "justice-league",
    "url": "https://api.github.com/teams/1"
  }
]
    ```

    


=== "POST Create a team"

    To create a team, the authenticated user must be a member or owner of `{org}`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see "[Setting team creation permissions](https://help.github.com/en/articles/setting-team-creation-permissions-in-your-organization)."

When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see "[About teams](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)".

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "description": "\u003cstring\u003e",
  "maintainers": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "name": "\u003cstring\u003e",
  "parent_team_id": "\u003cinteger\u003e",
  "permission": "pull",
  "privacy": "\u003cstring\u003e",
  "repo_names": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
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

    


=== "GET Get an organization"

    To see many of the organization response values, you need to be an authenticated organization owner with the `admin:org` scope. When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://help.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).

GitHub Apps with the `Organization plan` permission can use this endpoint to retrieve information about an organization's GitHub plan. See "[Authenticating with GitHub Apps](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/)" for details. For an example response, see "[Response with GitHub plan information](https://developer.github.com/v3/orgs/#response-with-github-plan-information)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "billing_email": "mona@github.com",
  "blog": "https://github.com/blog",
  "collaborators": 8,
  "company": "GitHub",
  "created_at": "2008-01-14T04:33:35Z",
  "default_repository_permission": "read",
  "description": "A great organization",
  "disk_usage": 10000,
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
  "members_allowed_repository_creation_type": "all",
  "members_can_create_internal_repositories": false,
  "members_can_create_private_repositories": false,
  "members_can_create_public_repositories": false,
  "members_can_create_repositories": true,
  "members_url": "https://api.github.com/orgs/github/members{/member}",
  "name": "github",
  "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
  "owned_private_repos": 100,
  "plan": {
    "name": "Medium",
    "private_repos": 20,
    "space": 400
  },
  "private_gists": 81,
  "public_gists": 1,
  "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
  "public_repos": 2,
  "repos_url": "https://api.github.com/orgs/github/repos",
  "total_private_repos": 100,
  "twitter_username": "github",
  "two_factor_requirement_enabled": true,
  "type": "Organization",
  "updated_at": "2014-03-03T18:58:10Z",
  "url": "https://api.github.com/orgs/github"
}
    ```

    


=== "PATCH Update an organization"

    **Parameter Deprecation Notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).

Enables an authenticated organization owner with the `admin:org` scope to update the organization's profile and member privileges.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "billing_email": "\u003cstring\u003e",
  "blog": "\u003cstring\u003e",
  "company": "\u003cstring\u003e",
  "default_repository_permission": "read",
  "description": "\u003cstring\u003e",
  "email": "\u003cstring\u003e",
  "has_organization_projects": "\u003cboolean\u003e",
  "has_repository_projects": "\u003cboolean\u003e",
  "location": "\u003cstring\u003e",
  "members_allowed_repository_creation_type": "\u003cstring\u003e",
  "members_can_create_internal_repositories": "\u003cboolean\u003e",
  "members_can_create_private_repositories": "\u003cboolean\u003e",
  "members_can_create_public_repositories": "\u003cboolean\u003e",
  "members_can_create_repositories": true,
  "name": "\u003cstring\u003e",
  "twitter_username": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "avatar_url": "https://github.com/images/error/octocat_happy.gif",
  "billing_email": "mona@github.com",
  "blog": "https://github.com/blog",
  "collaborators": 8,
  "company": "GitHub",
  "created_at": "2008-01-14T04:33:35Z",
  "default_repository_permission": "read",
  "description": "A great organization",
  "disk_usage": 10000,
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
  "members_allowed_repository_creation_type": "all",
  "members_can_create_internal_repositories": false,
  "members_can_create_private_repositories": false,
  "members_can_create_public_repositories": false,
  "members_can_create_repositories": true,
  "members_url": "https://api.github.com/orgs/github/members{/member}",
  "name": "github",
  "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
  "owned_private_repos": 100,
  "plan": {
    "name": "Medium",
    "private_repos": 20,
    "space": 400
  },
  "private_gists": 81,
  "public_gists": 1,
  "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
  "public_repos": 2,
  "repos_url": "https://api.github.com/orgs/github/repos",
  "total_private_repos": 100,
  "twitter_username": "github",
  "two_factor_requirement_enabled": true,
  "type": "Organization",
  "updated_at": "2014-03-03T18:58:10Z",
  "url": "https://api.github.com/orgs/github"
}
    ```

    


=== "GET List public organization events"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "actor": {
      "avatar_url": "anim officia pariatur nostrud ipsum",
      "display_login": "cillum Excepteur aute pariatur",
      "gravatar_id": "est nisi dolor",
      "id": 95373152,
      "login": "minim fugiat non",
      "url": "elit dolor tempor in aliquip"
    },
    "created_at": "incididunt u",
    "id": "Duis",
    "org": {
      "avatar_url": "id",
      "display_login": "reprehenderit Duis",
      "gravatar_id": "qui dolore aliqu",
      "id": -35339806,
      "login": "quis aute",
      "url": "nulla cillum est dolore magna"
    },
    "payload": {
      "action": "enim in id dolore",
      "comment": {
        "author_association": "eiusmod occaecat mollit",
        "body": "What version of Safari were you using when you observed this bug?",
        "body_html": "Ut",
        "body_text": "deserunt Duis",
        "created_at": "2011-04-14T16:00:49Z",
        "html_url": "ullamco proident elit dolore",
        "id": 42,
        "issue_url": "cupidatat id proident deserunt",
        "node_id": "anim amet",
        "performed_via_github_app": {
          "client_id": "\"Iv1.25b5d1e65ffc4022\"",
          "client_secret": "\"1d4b2097ac622ba702d19de498f005747a8b21d3\"",
          "created_at": "2017-07-08T16:18:44-04:00",
          "description": "",
          "events": [
            "label",
            "deployment"
          ],
          "external_url": "https://example.com",
          "html_url": "https://github.com/apps/super-ci",
          "id": 37,
          "installations_count": 5,
          "name": "Probot Owners",
          "node_id": "MDExOkludGVncmF0aW9uMQ==",
          "owner": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "pem": "\"{{vault:rsa-private-key}}\\n\"",
          "permissions": {
            "deployments": "write",
            "issues": "read"
          },
          "slug": "probot-owners",
          "updated_at": "2017-07-08T16:18:44-04:00",
          "webhook_secret": "\"6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b\""
        },
        "reactions": {
          "+1": -13368948,
          "-1": -90524562,
          "confused": 29335122,
          "eyes": 58121707,
          "heart": -66585006,
          "hooray": 75254661,
          "laugh": 17359216,
          "rocket": 51746123,
          "total_count": 19431373,
          "url": "Ut in sunt fugiat occaecat"
        },
        "updated_at": "2011-04-14T16:00:49Z",
        "url": "https://api.github.com/repositories/42/issues/comments/1",
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
          "site_admin": true,
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        }
      },
      "issue": {
        "active_lock_reason": "too heated",
        "assignee": {
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
          "site_admin": true,
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        },
        "assignees": [
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
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          },
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
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          }
        ],
        "author_association": "in",
        "body": "I\u0027m having a problem with this.",
        "body_html": "labore",
        "body_text": "fugiat dolore consectetur",
        "closed_at": "Excepteur proident",
        "comments": 0,
        "comments_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/comments",
        "created_at": "2011-04-22T13:33:48Z",
        "events_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/events",
        "html_url": "https://github.com/octocat/Hello-World/issues/1347",
        "id": 1,
        "labels": [
          {
            "type": "boolean"
          },
          {
            "type": "boolean"
          }
        ],
        "labels_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/labels{/name}",
        "locked": true,
        "milestone": {
          "closed_at": "2013-02-12T13:22:01Z",
          "closed_issues": 8,
          "created_at": "2011-04-10T20:09:31Z",
          "creator": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "description": "Tracking milestone for version 1.0",
          "due_on": "2012-10-09T23:39:01Z",
          "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
          "id": 1002604,
          "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
          "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
          "number": 42,
          "open_issues": 4,
          "state": "open",
          "title": "v1.0",
          "updated_at": "2014-03-03T18:58:10Z",
          "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1"
        },
        "node_id": "MDU6SXNzdWUx",
        "number": 1347,
        "performed_via_github_app": {
          "client_id": "\"Iv1.25b5d1e65ffc4022\"",
          "client_secret": "\"1d4b2097ac622ba702d19de498f005747a8b21d3\"",
          "created_at": "2017-07-08T16:18:44-04:00",
          "description": "",
          "events": [
            "label",
            "deployment"
          ],
          "external_url": "https://example.com",
          "html_url": "https://github.com/apps/super-ci",
          "id": 37,
          "installations_count": 5,
          "name": "Probot Owners",
          "node_id": "MDExOkludGVncmF0aW9uMQ==",
          "owner": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "pem": "\"{{vault:rsa-private-key}}\\n\"",
          "permissions": {
            "deployments": "write",
            "issues": "read"
          },
          "slug": "probot-owners",
          "updated_at": "2017-07-08T16:18:44-04:00",
          "webhook_secret": "\"6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b\""
        },
        "pull_request": {
          "diff_url": "incididunt adipisicing veniam qui",
          "html_url": "laborum",
          "merged_at": "esse et culpa",
          "patch_url": "minim ut",
          "url": "culpa Duis reprehenderit ut Excepteur"
        },
        "repository": {
          "allow_merge_commit": true,
          "allow_rebase_merge": true,
          "allow_squash_merge": true,
          "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
          "archived": false,
          "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
          "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
          "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
          "clone_url": "https://github.com/octocat/Hello-World.git",
          "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
          "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
          "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
          "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
          "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
          "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
          "created_at": "2011-01-26T19:01:12Z",
          "default_branch": "master",
          "delete_branch_on_merge": false,
          "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
          "description": "This your first repo!",
          "disabled": false,
          "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
          "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
          "fork": true,
          "forks": 74059665,
          "forks_count": 9,
          "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
          "full_name": "octocat/Hello-World",
          "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
          "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
          "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
          "git_url": "git:github.com/octocat/Hello-World.git",
          "has_downloads": true,
          "has_issues": true,
          "has_pages": true,
          "has_projects": true,
          "has_wiki": true,
          "homepage": "https://github.com",
          "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
          "html_url": "https://github.com/octocat/Hello-World",
          "id": 42,
          "is_template": true,
          "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
          "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
          "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
          "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
          "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
          "language": "irure aute commodo",
          "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
          "license": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "master_branch": "id anim in",
          "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
          "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
          "mirror_url": "git:git.example.com/octocat/Hello-World",
          "name": "Team Environment",
          "network_count": -10810678,
          "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
          "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
          "open_issues": 3584172,
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
            "site_admin": true,
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          },
          "permissions": {
            "admin": true,
            "maintain": true,
            "pull": true,
            "push": true,
            "triage": false
          },
          "private": false,
          "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
          "pushed_at": "2011-01-26T19:06:43Z",
          "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
          "size": 108,
          "ssh_url": "git@github.com:octocat/Hello-World.git",
          "stargazers_count": 80,
          "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
          "starred_at": "\"2020-07-09T00:17:42Z\"",
          "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
          "subscribers_count": -4318022,
          "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
          "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
          "svn_url": "https://svn.github.com/octocat/Hello-World",
          "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
          "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
          "temp_clone_token": "labore dolore",
          "template_repository": {
            "allow_merge_commit": false,
            "allow_rebase_merge": false,
            "allow_squash_merge": false,
            "archive_url": "nulla sed fugiat Lorem",
            "archived": true,
            "assignees_url": "sit ut",
            "blobs_url": "ex ipsum voluptate",
            "branches_url": "ullamco amet sunt",
            "clone_url": "sit pariatur dolore nisi",
            "collaborators_url": "moll",
            "comments_url": "Duis aute eu",
            "commits_url": "labore fugiat",
            "compare_url": "quis id",
            "contents_url": "aute in minim",
            "contributors_url": "consequat Duis Lorem voluptate",
            "created_at": "veniam",
            "default_branch": "officia et Excepteur do ex",
            "delete_branch_on_merge": true,
            "deployments_url": "ex ipsum minim",
            "description": "cupidatat enim Ut",
            "disabled": true,
            "downloads_url": "officia incididunt nisi Ut",
            "events_url": "qui",
            "fork": true,
            "forks_count": -6817855,
            "forks_url": "in incididunt non",
            "full_name": "Duis ipsum amet proident dolor",
            "git_commits_url": "dolor sint enim sed voluptate",
            "git_refs_url": "irure cupidatat aliquip voluptate",
            "git_tags_url": "commodo",
            "git_url": "quis anim nisi dolore deserunt",
            "has_downloads": true,
            "has_issues": false,
            "has_pages": true,
            "has_projects": false,
            "has_wiki": false,
            "homepage": "Lorem aliquip",
            "hooks_url": "qui commodo consequat dolore elit",
            "html_url": "quis et",
            "id": -74448652,
            "is_template": true,
            "issue_comment_url": "deserunt Excepteur occaecat",
            "issue_events_url": "fugiat laborum",
            "issues_url": "proident p",
            "keys_url": "sunt dolor enim amet",
            "labels_url": "ullamco laboris",
            "language": "sunt sit",
            "languages_url": "id aute voluptate",
            "merges_url": "nostrud paria",
            "milestones_url": "in officia",
            "mirror_url": "do",
            "name": "reprehenderit cupidatat",
            "network_count": -69044006,
            "node_id": "labore proident aliqua",
            "notifications_url": "dolor qui deserunt tem",
            "open_issues_count": 22674481,
            "owner": {
              "avatar_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "events_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "followers_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "following_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "gists_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "gravatar_id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "html_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "login": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "node_id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "organizations_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "received_events_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "repos_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "site_admin": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "starred_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "subscriptions_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "type": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            },
            "permissions": {
              "admin": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "pull": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "push": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            },
            "private": true,
            "pulls_url": "et aute",
            "pushed_at": "tempor do ex culpa elit",
            "releases_url": "ex",
            "size": 39472844,
            "ssh_url": "esse ut dolor",
            "stargazers_count": -71285277,
            "stargazers_url": "ad dolore eu",
            "statuses_url": "id nisi eiusmod",
            "subscribers_count": -65005951,
            "subscribers_url": "aute voluptate ullamco sed",
            "subscription_url": "tempor consequat qui elit",
            "svn_url": "ullamco sunt qui dolore eiusmod",
            "tags_url": "in laborum",
            "teams_url": "eiusmod eu",
            "temp_clone_token": "nostrud magna dolore cupidatat",
            "template_repository": "Excepteur sit elit mollit",
            "topics": [
              {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            ],
            "trees_url": "enim pariatur nulla in et",
            "updated_at": "in quis cillum sunt",
            "url": "anim quis Lorem do",
            "visibility": "sunt commodo",
            "watchers_count": -20279907
          },
          "topics": [
            "aute in",
            "do laborum fugiat dolore culpa"
          ],
          "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
          "updated_at": "2011-01-26T19:14:43Z",
          "url": "https://api.github.com/repos/octocat/Hello-World",
          "visibility": "public",
          "watchers": 95751259,
          "watchers_count": 80
        },
        "repository_url": "https://api.github.com/repos/octocat/Hello-World",
        "state": "open",
        "timeline_url": "reprehenderit",
        "title": "Found a bug",
        "updated_at": "2011-04-22T13:33:48Z",
        "url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
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
          "site_admin": true,
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        }
      },
      "pages": [
        {
          "action": "proident laborum aute",
          "html_url": "amet",
          "page_name": "dolore ",
          "sha": "commodo sunt non",
          "summary": "et qui",
          "title": "exercitation"
        },
        {
          "action": "magna consequat",
          "html_url": "qui sunt Duis",
          "page_name": "commodo nisi proident",
          "sha": "cillum esse in qui",
          "summary": "nulla aute dolore tempor",
          "title": "consequat reprehe"
        }
      ]
    },
    "public": false,
    "repo": {
      "id": 7809622,
      "name": "sunt aliqua ipsum tempor",
      "url": "mollit nisi"
    },
    "type": "labore magna"
  },
  {
    "actor": {
      "avatar_url": "mollit elit nulla",
      "display_login": "dolor occaecat",
      "gravatar_id": "dolore",
      "id": 84442394,
      "login": "ut",
      "url": "labore in"
    },
    "created_at": "labore id tempor",
    "id": "minim aute qui enim Lorem",
    "org": {
      "avatar_url": "aute exercitation in ut nostrud",
      "display_login": "eu velit nisi",
      "gravatar_id": "proident culpa",
      "id": 65537797,
      "login": "ipsum",
      "url": "voluptate labore"
    },
    "payload": {
      "action": "ex Excepteur vo",
      "comment": {
        "author_association": "sint aliquip dolor sunt elit",
        "body": "What version of Safari were you using when you observed this bug?",
        "body_html": "Duis exercitation",
        "body_text": "quis dolore occaecat consequat",
        "created_at": "2011-04-14T16:00:49Z",
        "html_url": "in Lorem",
        "id": 42,
        "issue_url": "est amet Lorem",
        "node_id": "ad et",
        "performed_via_github_app": {
          "client_id": "\"Iv1.25b5d1e65ffc4022\"",
          "client_secret": "\"1d4b2097ac622ba702d19de498f005747a8b21d3\"",
          "created_at": "2017-07-08T16:18:44-04:00",
          "description": "",
          "events": [
            "label",
            "deployment"
          ],
          "external_url": "https://example.com",
          "html_url": "https://github.com/apps/super-ci",
          "id": 37,
          "installations_count": 5,
          "name": "Probot Owners",
          "node_id": "MDExOkludGVncmF0aW9uMQ==",
          "owner": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "pem": "\"{{vault:rsa-private-key}}\\n\"",
          "permissions": {
            "deployments": "write",
            "issues": "read"
          },
          "slug": "probot-owners",
          "updated_at": "2017-07-08T16:18:44-04:00",
          "webhook_secret": "\"6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b\""
        },
        "reactions": {
          "+1": -93375299,
          "-1": -63132563,
          "confused": -30251332,
          "eyes": 66357128,
          "heart": -25918793,
          "hooray": 65956382,
          "laugh": 84247895,
          "rocket": 23108649,
          "total_count": -99329732,
          "url": "in amet dolor"
        },
        "updated_at": "2011-04-14T16:00:49Z",
        "url": "https://api.github.com/repositories/42/issues/comments/1",
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
          "site_admin": true,
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        }
      },
      "issue": {
        "active_lock_reason": "too heated",
        "assignee": {
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
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        },
        "assignees": [
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
            "site_admin": true,
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          },
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
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          }
        ],
        "author_association": "et tempor minim dolor",
        "body": "I\u0027m having a problem with this.",
        "body_html": "non consectetur",
        "body_text": "ea quis in",
        "closed_at": "Excepteur",
        "comments": 0,
        "comments_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/comments",
        "created_at": "2011-04-22T13:33:48Z",
        "events_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/events",
        "html_url": "https://github.com/octocat/Hello-World/issues/1347",
        "id": 1,
        "labels": [
          {
            "type": "boolean"
          },
          {
            "type": "boolean"
          }
        ],
        "labels_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/labels{/name}",
        "locked": true,
        "milestone": {
          "closed_at": "2013-02-12T13:22:01Z",
          "closed_issues": 8,
          "created_at": "2011-04-10T20:09:31Z",
          "creator": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "description": "Tracking milestone for version 1.0",
          "due_on": "2012-10-09T23:39:01Z",
          "html_url": "https://github.com/octocat/Hello-World/milestones/v1.0",
          "id": 1002604,
          "labels_url": "https://api.github.com/repos/octocat/Hello-World/milestones/1/labels",
          "node_id": "MDk6TWlsZXN0b25lMTAwMjYwNA==",
          "number": 42,
          "open_issues": 4,
          "state": "open",
          "title": "v1.0",
          "updated_at": "2014-03-03T18:58:10Z",
          "url": "https://api.github.com/repos/octocat/Hello-World/milestones/1"
        },
        "node_id": "MDU6SXNzdWUx",
        "number": 1347,
        "performed_via_github_app": {
          "client_id": "\"Iv1.25b5d1e65ffc4022\"",
          "client_secret": "\"1d4b2097ac622ba702d19de498f005747a8b21d3\"",
          "created_at": "2017-07-08T16:18:44-04:00",
          "description": "",
          "events": [
            "label",
            "deployment"
          ],
          "external_url": "https://example.com",
          "html_url": "https://github.com/apps/super-ci",
          "id": 37,
          "installations_count": 5,
          "name": "Probot Owners",
          "node_id": "MDExOkludGVncmF0aW9uMQ==",
          "owner": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "pem": "\"{{vault:rsa-private-key}}\\n\"",
          "permissions": {
            "deployments": "write",
            "issues": "read"
          },
          "slug": "probot-owners",
          "updated_at": "2017-07-08T16:18:44-04:00",
          "webhook_secret": "\"6fba8f2fc8a7e8f2cca5577eddd82ca7586b3b6b\""
        },
        "pull_request": {
          "diff_url": "veniam nostrud ad reprehenderit",
          "html_url": "Excepteur magna minim inc",
          "merged_at": "do dolor veniam quis",
          "patch_url": "labore consectetur exercitation fugiat",
          "url": "ex"
        },
        "repository": {
          "allow_merge_commit": true,
          "allow_rebase_merge": true,
          "allow_squash_merge": true,
          "archive_url": "http://api.github.com/repos/octocat/Hello-World/{archive_format}{/ref}",
          "archived": false,
          "assignees_url": "http://api.github.com/repos/octocat/Hello-World/assignees{/user}",
          "blobs_url": "http://api.github.com/repos/octocat/Hello-World/git/blobs{/sha}",
          "branches_url": "http://api.github.com/repos/octocat/Hello-World/branches{/branch}",
          "clone_url": "https://github.com/octocat/Hello-World.git",
          "collaborators_url": "http://api.github.com/repos/octocat/Hello-World/collaborators{/collaborator}",
          "comments_url": "http://api.github.com/repos/octocat/Hello-World/comments{/number}",
          "commits_url": "http://api.github.com/repos/octocat/Hello-World/commits{/sha}",
          "compare_url": "http://api.github.com/repos/octocat/Hello-World/compare/{base}...{head}",
          "contents_url": "http://api.github.com/repos/octocat/Hello-World/contents/{+path}",
          "contributors_url": "http://api.github.com/repos/octocat/Hello-World/contributors",
          "created_at": "2011-01-26T19:01:12Z",
          "default_branch": "master",
          "delete_branch_on_merge": false,
          "deployments_url": "http://api.github.com/repos/octocat/Hello-World/deployments",
          "description": "This your first repo!",
          "disabled": true,
          "downloads_url": "http://api.github.com/repos/octocat/Hello-World/downloads",
          "events_url": "http://api.github.com/repos/octocat/Hello-World/events",
          "fork": false,
          "forks": -2768827,
          "forks_count": 9,
          "forks_url": "http://api.github.com/repos/octocat/Hello-World/forks",
          "full_name": "octocat/Hello-World",
          "git_commits_url": "http://api.github.com/repos/octocat/Hello-World/git/commits{/sha}",
          "git_refs_url": "http://api.github.com/repos/octocat/Hello-World/git/refs{/sha}",
          "git_tags_url": "http://api.github.com/repos/octocat/Hello-World/git/tags{/sha}",
          "git_url": "git:github.com/octocat/Hello-World.git",
          "has_downloads": true,
          "has_issues": true,
          "has_pages": false,
          "has_projects": true,
          "has_wiki": true,
          "homepage": "https://github.com",
          "hooks_url": "http://api.github.com/repos/octocat/Hello-World/hooks",
          "html_url": "https://github.com/octocat/Hello-World",
          "id": 42,
          "is_template": true,
          "issue_comment_url": "http://api.github.com/repos/octocat/Hello-World/issues/comments{/number}",
          "issue_events_url": "http://api.github.com/repos/octocat/Hello-World/issues/events{/number}",
          "issues_url": "http://api.github.com/repos/octocat/Hello-World/issues{/number}",
          "keys_url": "http://api.github.com/repos/octocat/Hello-World/keys{/key_id}",
          "labels_url": "http://api.github.com/repos/octocat/Hello-World/labels{/name}",
          "language": "irure adipisicing ullamco consectetur",
          "languages_url": "http://api.github.com/repos/octocat/Hello-World/languages",
          "license": {
            "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
          },
          "master_branch": "occaeca",
          "merges_url": "http://api.github.com/repos/octocat/Hello-World/merges",
          "milestones_url": "http://api.github.com/repos/octocat/Hello-World/milestones{/number}",
          "mirror_url": "git:git.example.com/octocat/Hello-World",
          "name": "Team Environment",
          "network_count": 50789411,
          "node_id": "MDEwOlJlcG9zaXRvcnkxMjk2MjY5",
          "notifications_url": "http://api.github.com/repos/octocat/Hello-World/notifications{?since,all,participating}",
          "open_issues": -70107099,
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
            "site_admin": true,
            "starred_at": "\"2020-07-09T00:17:55Z\"",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "type": "User",
            "url": "https://api.github.com/users/octocat"
          },
          "permissions": {
            "admin": false,
            "maintain": false,
            "pull": false,
            "push": true,
            "triage": false
          },
          "private": false,
          "pulls_url": "http://api.github.com/repos/octocat/Hello-World/pulls{/number}",
          "pushed_at": "2011-01-26T19:06:43Z",
          "releases_url": "http://api.github.com/repos/octocat/Hello-World/releases{/id}",
          "size": 108,
          "ssh_url": "git@github.com:octocat/Hello-World.git",
          "stargazers_count": 80,
          "stargazers_url": "http://api.github.com/repos/octocat/Hello-World/stargazers",
          "starred_at": "\"2020-07-09T00:17:42Z\"",
          "statuses_url": "http://api.github.com/repos/octocat/Hello-World/statuses/{sha}",
          "subscribers_count": 96412870,
          "subscribers_url": "http://api.github.com/repos/octocat/Hello-World/subscribers",
          "subscription_url": "http://api.github.com/repos/octocat/Hello-World/subscription",
          "svn_url": "https://svn.github.com/octocat/Hello-World",
          "tags_url": "http://api.github.com/repos/octocat/Hello-World/tags",
          "teams_url": "http://api.github.com/repos/octocat/Hello-World/teams",
          "temp_clone_token": "officia pariatur nisi incididunt",
          "template_repository": {
            "allow_merge_commit": true,
            "allow_rebase_merge": true,
            "allow_squash_merge": false,
            "archive_url": "",
            "archived": false,
            "assignees_url": "nisi amet dolor eiusmod dolore",
            "blobs_url": "cupidatat ex aliqua laboris",
            "branches_url": "fugiat incididunt cillum commodo",
            "clone_url": "in eiusmod nostrud quis in",
            "collaborators_url": "eiusmod tempor voluptate aliqua",
            "comments_url": "sed veniam id",
            "commits_url": "sed amet",
            "compare_url": "ut aliqua ullamco mini",
            "contents_url": "in v",
            "contributors_url": "sit",
            "created_at": "aliqua",
            "default_branch": "ullamco",
            "delete_branch_on_merge": false,
            "deployments_url": "consequat cillum tempor",
            "description": "sit est Duis enim consequat",
            "disabled": false,
            "downloads_url": "occaecat reprehenderit",
            "events_url": "est",
            "fork": true,
            "forks_count": -44453726,
            "forks_url": "sit",
            "full_name": "labore Duis",
            "git_commits_url": "officia in et non",
            "git_refs_url": "esse",
            "git_tags_url": "a",
            "git_url": "ut ",
            "has_downloads": false,
            "has_issues": true,
            "has_pages": true,
            "has_projects": false,
            "has_wiki": true,
            "homepage": "aute voluptate",
            "hooks_url": "proident Excepteur ut exercitation",
            "html_url": "qui",
            "id": -23559911,
            "is_template": false,
            "issue_comment_url": "elit Duis Ut dolore exercitation",
            "issue_events_url": "sit voluptate",
            "issues_url": "non anim aliqua mollit",
            "keys_url": "in nostrud nulla Duis laborum",
            "labels_url": "sed",
            "language": "est qui",
            "languages_url": "dolor Duis Excepteur",
            "merges_url": "sunt irure",
            "milestones_url": "aute",
            "mirror_url": "deserunt culpa sunt",
            "name": "ut proident ex quis",
            "network_count": 73783930,
            "node_id": "amet",
            "notifications_url": "consequat",
            "open_issues_count": 8382001,
            "owner": {
              "avatar_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "events_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "followers_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "following_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "gists_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "gravatar_id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "html_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "login": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "node_id": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "organizations_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "received_events_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "repos_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "site_admin": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "starred_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "subscriptions_url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "type": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "url": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            },
            "permissions": {
              "admin": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "pull": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              "push": {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            },
            "private": false,
            "pulls_url": "quis elit ad Ut",
            "pushed_at": "id labore",
            "releases_url": "pariatur",
            "size": 87085671,
            "ssh_url": "Lorem ad velit esse",
            "stargazers_count": -23546435,
            "stargazers_url": "amet ea",
            "statuses_url": "mollit",
            "subscribers_count": 71791566,
            "subscribers_url": "tempor pariatur",
            "subscription_url": "quis a",
            "svn_url": "non et consequat elit enim",
            "tags_url": "veniam in",
            "teams_url": "sint officia do laboris",
            "temp_clone_token": "aliqua enim dolore labore",
            "template_repository": "non nisi laborum dolor enim",
            "topics": [
              {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              },
              {
                "value": "\u003cError: Too many levels of nesting to fake this schema\u003e"
              }
            ],
            "trees_url": "labore nisi cillum Ut",
            "updated_at": "sint proident",
            "url": "non consectetur id",
            "visibility": "est Lorem",
            "watchers_count": 85435987
          },
          "topics": [
            "oc",
            "volupt"
          ],
          "trees_url": "http://api.github.com/repos/octocat/Hello-World/git/trees{/sha}",
          "updated_at": "2011-01-26T19:14:43Z",
          "url": "https://api.github.com/repos/octocat/Hello-World",
          "visibility": "public",
          "watchers": 89851252,
          "watchers_count": 80
        },
        "repository_url": "https://api.github.com/repos/octocat/Hello-World",
        "state": "open",
        "timeline_url": "do",
        "title": "Found a bug",
        "updated_at": "2011-04-22T13:33:48Z",
        "url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
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
          "site_admin": true,
          "starred_at": "\"2020-07-09T00:17:55Z\"",
          "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
          "type": "User",
          "url": "https://api.github.com/users/octocat"
        }
      },
      "pages": [
        {
          "action": "labore adipisicing irure in",
          "html_url": "officia nulla laboris sit",
          "page_name": "repreh",
          "sha": "aute velit",
          "summary": "veniam do ut",
          "title": "sed in"
        },
        {
          "action": "ea velit nisi",
          "html_url": "Excepteur sunt Lorem ",
          "page_name": "cillum consectetur exercitation ad Lorem",
          "sha": "dolor",
          "summary": "officia irure vol",
          "title": "ut laboris anim"
        }
      ]
    },
    "public": false,
    "repo": {
      "id": -29038580,
      "name": "laborum adipisicing pariatur t",
      "url": "in"
    },
    "type": "ipsum elit cupidatat sed"
  }
]
    ```

    


=== "GET Get an organization installation for the authenticated app"

    Enables an authenticated GitHub App to find the organization's installation information.

You must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "access_tokens_url": "https://api.github.com/installations/1/access_tokens",
  "account": {
    "avatar_url": "https://github.com/images/error/hubot_happy.gif",
    "events_url": "https://api.github.com/orgs/github/events",
    "followers_url": "https://api.github.com/users/github/followers",
    "following_url": "https://api.github.com/users/github/following{/other_user}",
    "gists_url": "https://api.github.com/users/github/gists{/gist_id}",
    "gravatar_id": "",
    "html_url": "https://github.com/github",
    "id": 1,
    "login": "github",
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "organizations_url": "https://api.github.com/users/github/orgs",
    "received_events_url": "https://api.github.com/users/github/received_events",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "site_admin": false,
    "starred_url": "https://api.github.com/users/github/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/github/subscriptions",
    "type": "Organization",
    "url": "https://api.github.com/orgs/github"
  },
  "app_id": 1,
  "app_slug": "github-actions",
  "created_at": "2018-02-09T20:51:14Z",
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
  "repository_selection": "all",
  "single_file_name": null,
  "target_id": 1,
  "target_type": "Organization",
  "updated_at": "2018-02-09T20:51:14Z"
}
    ```

    


=== "GET List app installations for an organization"

    Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed on repositories in the organization. You must be an organization owner with `admin:read` scope to use this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "installations": [
    {
      "access_tokens_url": "https://api.github.com/app/installations/25381/access_tokens",
      "account": {
        "avatar_url": "https://avatars3.githubusercontent.com/u/6811672?v=4",
        "events_url": "https://api.github.com/users/octo-org/events{/privacy}",
        "followers_url": "https://api.github.com/users/octo-org/followers",
        "following_url": "https://api.github.com/users/octo-org/following{/other_user}",
        "gists_url": "https://api.github.com/users/octo-org/gists{/gist_id}",
        "gravatar_id": "",
        "html_url": "https://github.com/octo-org",
        "id": 6811672,
        "login": "octo-org",
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjY4MTE2NzI=",
        "organizations_url": "https://api.github.com/users/octo-org/orgs",
        "received_events_url": "https://api.github.com/users/octo-org/received_events",
        "repos_url": "https://api.github.com/users/octo-org/repos",
        "site_admin": false,
        "starred_url": "https://api.github.com/users/octo-org/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/octo-org/subscriptions",
        "type": "Organization",
        "url": "https://api.github.com/users/octo-org"
      },
      "app_id": 2218,
      "app_slug": "github-actions",
      "created_at": "2017-05-16T08:47:09.000-07:00",
      "events": [
        "deployment",
        "deployment_status"
      ],
      "html_url": "https://github.com/organizations/octo-org/settings/installations/25381",
      "id": 25381,
      "permissions": {
        "deployments": "write",
        "metadata": "read",
        "pull_requests": "read",
        "statuses": "read"
      },
      "repositories_url": "https://api.github.com/installation/repositories",
      "repository_selection": "selected",
      "single_file_name": null,
      "target_id": 6811672,
      "target_type": "Organization",
      "updated_at": "2017-06-06T11:23:23.000-07:00"
    }
  ],
  "total_count": 1
}
    ```

    


=== "GET List organization issues assigned to the authenticated user"

    List issues in an organization assigned to the authenticated user.

**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this
reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by
the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull
request id, use the "[List pull requests](https://developer.github.com/v3/pulls/#list-pull-requests)" endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `filter` | `string` | Yes | Indicates which sorts of issues to return. Can be one of:  
\* `assigned`: Issues assigned to you  
\* `created`: Issues created by you  
\* `mentioned`: Issues mentioning you  
\* `subscribed`: Issues you're subscribed to updates for  
\* `all`: All issues the authenticated user can see, regardless of participation or creation | `assigned` |
    | `state` | `string` | Yes | Indicates the state of the issues to return. Can be either `open`, `closed`, or `all`. | `open` |
    | `labels` | `string` | Yes | A list of comma separated label names. Example: `bug,ui,@high` | `<string>` |
    | `sort` | `string` | Yes | What to sort results by. Can be either `created`, `updated`, `comments`. | `created` |
    | `direction` | `string` | Yes | One of `asc` (ascending) or `desc` (descending). | `desc` |
    | `since` | `string` | Yes | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "active_lock_reason": "too heated",
    "assignee": {
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
    "assignees": [
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
    ],
    "author_association": "collaborator",
    "body": "I\u0027m having a problem with this.",
    "closed_at": null,
    "comments": 0,
    "comments_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/comments",
    "created_at": "2011-04-22T13:33:48Z",
    "events_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/events",
    "html_url": "https://github.com/octocat/Hello-World/issues/1347",
    "id": 1,
    "labels": [
      {
        "color": "f29513",
        "default": true,
        "description": "Something isn\u0027t working",
        "id": 208045946,
        "name": "bug",
        "node_id": "MDU6TGFiZWwyMDgwNDU5NDY=",
        "url": "https://api.github.com/repos/octocat/Hello-World/labels/bug"
      }
    ],
    "labels_url": "https://api.github.com/repos/octocat/Hello-World/issues/1347/labels{/name}",
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
    "node_id": "MDU6SXNzdWUx",
    "number": 1347,
    "pull_request": {
      "diff_url": "https://github.com/octocat/Hello-World/pull/1347.diff",
      "html_url": "https://github.com/octocat/Hello-World/pull/1347",
      "patch_url": "https://github.com/octocat/Hello-World/pull/1347.patch",
      "url": "https://api.github.com/repos/octocat/Hello-World/pulls/1347"
    },
    "repository": {
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
    },
    "repository_url": "https://api.github.com/repos/octocat/Hello-World",
    "state": "open",
    "title": "Found a bug",
    "updated_at": "2011-04-22T13:33:48Z",
    "url": "https://api.github.com/repos/octocat/Hello-World/issues/1347",
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

    


=== "GET List IdP groups for an organization"

    Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

List IdP groups available in an organization. You can limit your page results using the `per_page` parameter. GitHub generates a url-encoded `page` token using a cursor value for where the next page begins. For more information on cursor pagination, see "[Offset and Cursor Pagination explained](https://dev.to/jackmarchant/offset-and-cursor-pagination-explained-b89)."

The `per_page` parameter provides pagination for a list of IdP groups the authenticated user can access in an organization. For example, if the user `octocat` wants to see two groups per page in `octo-org` via cURL, it would look like this:

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:org` | `string` | Yes | (Required)  | `<string>` |
    
    

    

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

    

