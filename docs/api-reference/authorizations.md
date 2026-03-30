# authorizations API


=== "PUT Get-or-create an authorization for a specific app"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

Creates a new authorization for the specified OAuth application, only if an authorization for that application doesn't already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. It returns the user's existing authorization for the application if one is present. Otherwise, it creates and returns a new one.

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://developer.github.com/v3/auth/#working-with-two-factor-authentication)."

**Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:client_id` | `string` | Yes | (Required)  | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "client_secret": "\u003cstring\u003e",
  "fingerprint": "\u003cstring\u003e",
  "note": "\u003cstring\u003e",
  "note_url": "\u003cstring\u003e",
  "scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "app": {
    "client_id": "abcde12345fghij67890",
    "name": "my github app",
    "url": "http://my-github-app.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "id": 1,
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "scopes": [
    "public_repo"
  ],
  "token": "",
  "token_last_eight": "12345678",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/authorizations/1"
}
    ```

    


=== "PUT Get-or-create an authorization for a specific app and fingerprint"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

This method will create a new authorization for the specified OAuth application, only if an authorization for that application and fingerprint do not already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. `fingerprint` is a unique string to distinguish an authorization from others created for the same client ID and user. It returns the user's existing authorization for the application if one is present. Otherwise, it creates and returns a new one.

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://developer.github.com/v3/auth/#working-with-two-factor-authentication)."

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:client_id` | `string` | Yes | (Required)  | `<string>` |
    | `:fingerprint` | `string` | Yes | (Required) fingerprint parameter | `<string>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "client_secret": "\u003cstring\u003e",
  "note": "\u003cstring\u003e",
  "note_url": "\u003cstring\u003e",
  "scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "app": {
    "client_id": "abcde12345fghij67890",
    "name": "my github app",
    "url": "http://my-github-app.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "jklmnop12345678",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "id": 1,
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "scopes": [
    "public_repo"
  ],
  "token": "",
  "token_last_eight": "12345678",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/authorizations/1"
}
    ```

    


=== "GET Get a single authorization"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:authorization_id` | `string` | Yes | (Required) authorization_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "app": {
    "client_id": "abcde12345fghij67890",
    "name": "my github app",
    "url": "http://my-github-app.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "jklmnop12345678",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "id": 1,
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "scopes": [
    "public_repo"
  ],
  "token": "",
  "token_last_eight": "12345678",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/authorizations/1"
}
    ```

    


=== "PATCH Update an existing authorization"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://developer.github.com/v3/auth/#working-with-two-factor-authentication)."

You can only send one of these scope keys at a time.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:authorization_id` | `string` | Yes | (Required) authorization_id parameter | `<integer>` |
    
    

    
    #### Request Body
    
    ```json
    {
  "add_scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "fingerprint": "\u003cstring\u003e",
  "note": "\u003cstring\u003e",
  "note_url": "\u003cstring\u003e",
  "remove_scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ],
  "scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "app": {
    "client_id": "abcde12345fghij67890",
    "name": "my github app",
    "url": "http://my-github-app.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "jklmnop12345678",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "id": 1,
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "scopes": [
    "public_repo"
  ],
  "token": "",
  "token_last_eight": "12345678",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/authorizations/1"
}
    ```

    


=== "DELETE Delete an authorization"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:authorization_id` | `string` | Yes | (Required) authorization_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {}
    ```

    


=== "GET List your authorizations"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "app": {
      "client_id": "abcde12345fghij67890",
      "name": "my github app",
      "url": "http://my-github-app.com"
    },
    "created_at": "2011-09-06T17:26:27Z",
    "fingerprint": "jklmnop12345678",
    "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
    "id": 1,
    "note": "optional note",
    "note_url": "http://optional/note/url",
    "scopes": [
      "public_repo"
    ],
    "token": "",
    "token_last_eight": "12345678",
    "updated_at": "2011-09-06T20:39:23Z",
    "url": "https://api.github.com/authorizations/1"
  }
]
    ```

    


=== "POST Create a new authorization"

    **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://developer.github.com/v3/oauth_authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

**Warning:** Apps must use the [web application flow](https://developer.github.com/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).

Creates OAuth tokens using [Basic Authentication](https://developer.github.com/v3/auth#basic-authentication). If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see "[Working with two-factor authentication](https://developer.github.com/v3/auth/#working-with-two-factor-authentication)."

To create tokens for a particular OAuth application using this endpoint, you must authenticate as the user you want to create an authorization for and provide the app's client ID and secret, found on your OAuth application's settings page. If your OAuth application intends to create multiple tokens for one user, use `fingerprint` to differentiate between them.

You can also create tokens on GitHub from the [personal access tokens settings](https://github.com/settings/tokens) page. Read more about these tokens in [the GitHub Help documentation](https://help.github.com/articles/creating-an-access-token-for-command-line-use).

Organizations that enforce SAML SSO require personal access tokens to be allowed. Read more about allowing tokens in [the GitHub Help documentation](https://help.github.com/articles/about-identity-and-access-management-with-saml-single-sign-on).

    

    
    #### Request Body
    
    ```json
    {
  "client_id": "\u003cstring\u003e",
  "client_secret": "\u003cstring\u003e",
  "fingerprint": "\u003cstring\u003e",
  "note": "\u003cstring\u003e",
  "note_url": "\u003cstring\u003e",
  "scopes": [
    "\u003cstring\u003e",
    "\u003cstring\u003e"
  ]
}
    ```
    

    #### Response Example
    
    ```json
    {
  "app": {
    "client_id": "abcde12345fghij67890",
    "name": "my github app",
    "url": "http://my-github-app.com"
  },
  "created_at": "2011-09-06T17:26:27Z",
  "fingerprint": "",
  "hashed_token": "25f94a2a5c7fbaf499c665bc73d67c1c87e496da8985131633ee0a95819db2e8",
  "id": 1,
  "note": "optional note",
  "note_url": "http://optional/note/url",
  "scopes": [
    "public_repo"
  ],
  "token": "abcdefgh12345678",
  "token_last_eight": "12345678",
  "updated_at": "2011-09-06T20:39:23Z",
  "url": "https://api.github.com/authorizations/1"
}
    ```

    

