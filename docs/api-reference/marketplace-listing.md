# marketplace listing API


=== "GET List plans"

    Lists all plans that are part of your GitHub Marketplace listing.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
    "bullets": [
      "Up to 25 private repositories",
      "11 concurrent builds"
    ],
    "description": "A professional-grade CI solution",
    "has_free_trial": true,
    "id": 1313,
    "monthly_price_in_cents": 1099,
    "name": "Pro",
    "number": 3,
    "price_model": "flat-rate",
    "state": "published",
    "unit_name": null,
    "url": "https://api.github.com/marketplace_listing/plans/1313",
    "yearly_price_in_cents": 11870
  }
]
    ```

    


=== "GET List accounts for a plan"

    Returns user and organization accounts associated with the specified plan, including free plans. For per-seat pricing, you see the list of accounts that have purchased the plan, including the number of seats purchased. When someone submits a plan change that won't be processed until the end of their billing cycle, you will also see the upcoming pending change.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `sort` | `string` | Yes | One of `created` (when the repository was starred) or `updated` (when it was last pushed to). | `created` |
    | `direction` | `string` | Yes | To return the oldest accounts first, set to `asc`. Can be one of `asc` or `desc`. Ignored without the `sort` parameter. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:plan_id` | `string` | Yes | (Required) plan_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "id": 4,
    "login": "github",
    "marketplace_pending_change": {
      "effective_date": "2017-11-11T00:00:00Z",
      "id": 77,
      "plan": {
        "accounts_url": "https://api.github.com/marketplace_listing/plans/1111/accounts",
        "bullets": [
          "Up to 10 private repositories",
          "3 concurrent builds"
        ],
        "description": "A professional-grade CI solution",
        "has_free_trial": true,
        "id": 1111,
        "monthly_price_in_cents": 699,
        "name": "Startup",
        "number": 2,
        "price_model": "flat-rate",
        "state": "published",
        "unit_name": null,
        "url": "https://api.github.com/marketplace_listing/plans/1111",
        "yearly_price_in_cents": 7870
      },
      "unit_count": null
    },
    "marketplace_purchase": {
      "billing_cycle": "monthly",
      "free_trial_ends_on": "2017-11-11T00:00:00Z",
      "next_billing_date": "2017-11-11T00:00:00Z",
      "on_free_trial": true,
      "plan": {
        "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
        "bullets": [
          "Up to 25 private repositories",
          "11 concurrent builds"
        ],
        "description": "A professional-grade CI solution",
        "has_free_trial": true,
        "id": 1313,
        "monthly_price_in_cents": 1099,
        "name": "Pro",
        "number": 3,
        "price_model": "flat-rate",
        "state": "published",
        "unit_name": null,
        "url": "https://api.github.com/marketplace_listing/plans/1313",
        "yearly_price_in_cents": 11870
      },
      "unit_count": null,
      "updated_at": "2017-11-02T01:12:12Z"
    },
    "organization_billing_email": "billing@github.com",
    "type": "Organization",
    "url": "https://api.github.com/orgs/github"
  }
]
    ```

    


=== "GET List plans (stubbed)"

    Lists all plans that are part of your GitHub Marketplace listing.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
    "bullets": [
      "Up to 25 private repositories",
      "11 concurrent builds"
    ],
    "description": "A professional-grade CI solution",
    "has_free_trial": true,
    "id": 1313,
    "monthly_price_in_cents": 1099,
    "name": "Pro",
    "number": 3,
    "price_model": "flat-rate",
    "state": "published",
    "unit_name": null,
    "url": "https://api.github.com/marketplace_listing/plans/1313",
    "yearly_price_in_cents": 11870
  }
]
    ```

    


=== "GET List accounts for a plan (stubbed)"

    Returns repository and organization accounts associated with the specified plan, including free plans. For per-seat pricing, you see the list of accounts that have purchased the plan, including the number of seats purchased. When someone submits a plan change that won't be processed until the end of their billing cycle, you will also see the upcoming pending change.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `sort` | `string` | Yes | One of `created` (when the repository was starred) or `updated` (when it was last pushed to). | `created` |
    | `direction` | `string` | Yes | To return the oldest accounts first, set to `asc`. Can be one of `asc` or `desc`. Ignored without the `sort` parameter. | `<string>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    | `page` | `string` | Yes | Page number of the results to fetch. | `1` |
    | `:plan_id` | `string` | Yes | (Required) plan_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "id": 4,
    "login": "github",
    "marketplace_pending_change": {
      "effective_date": "2017-11-11T00:00:00Z",
      "id": 77,
      "plan": {
        "accounts_url": "https://api.github.com/marketplace_listing/plans/1111/accounts",
        "bullets": [
          "Up to 10 private repositories",
          "3 concurrent builds"
        ],
        "description": "A professional-grade CI solution",
        "has_free_trial": true,
        "id": 1111,
        "monthly_price_in_cents": 699,
        "name": "Startup",
        "number": 2,
        "price_model": "flat-rate",
        "state": "published",
        "unit_name": null,
        "url": "https://api.github.com/marketplace_listing/plans/1111",
        "yearly_price_in_cents": 7870
      },
      "unit_count": null
    },
    "marketplace_purchase": {
      "billing_cycle": "monthly",
      "free_trial_ends_on": "2017-11-11T00:00:00Z",
      "next_billing_date": "2017-11-11T00:00:00Z",
      "on_free_trial": true,
      "plan": {
        "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
        "bullets": [
          "Up to 25 private repositories",
          "11 concurrent builds"
        ],
        "description": "A professional-grade CI solution",
        "has_free_trial": true,
        "id": 1313,
        "monthly_price_in_cents": 1099,
        "name": "Pro",
        "number": 3,
        "price_model": "flat-rate",
        "state": "published",
        "unit_name": null,
        "url": "https://api.github.com/marketplace_listing/plans/1313",
        "yearly_price_in_cents": 11870
      },
      "unit_count": null,
      "updated_at": "2017-11-02T01:12:12Z"
    },
    "organization_billing_email": "billing@github.com",
    "type": "Organization",
    "url": "https://api.github.com/orgs/github"
  }
]
    ```

    


=== "GET Get a subscription plan for an account (stubbed)"

    Shows whether the user or organization account actively subscribes to a plan listed by the authenticated GitHub App. When someone submits a plan change that won't be processed until the end of their billing cycle, you will also see the upcoming pending change.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:account_id` | `string` | Yes | (Required) account_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "id": 4,
  "login": "github",
  "marketplace_pending_change": {
    "effective_date": "2017-11-11T00:00:00Z",
    "id": 77,
    "plan": {
      "accounts_url": "https://api.github.com/marketplace_listing/plans/1111/accounts",
      "bullets": [
        "Up to 10 private repositories",
        "3 concurrent builds"
      ],
      "description": "A professional-grade CI solution",
      "has_free_trial": true,
      "id": 1111,
      "monthly_price_in_cents": 699,
      "name": "Startup",
      "number": 2,
      "price_model": "flat-rate",
      "state": "published",
      "unit_name": null,
      "url": "https://api.github.com/marketplace_listing/plans/1111",
      "yearly_price_in_cents": 7870
    },
    "unit_count": null
  },
  "marketplace_purchase": {
    "billing_cycle": "monthly",
    "free_trial_ends_on": "2017-11-11T00:00:00Z",
    "next_billing_date": "2017-11-11T00:00:00Z",
    "on_free_trial": true,
    "plan": {
      "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
      "bullets": [
        "Up to 25 private repositories",
        "11 concurrent builds"
      ],
      "description": "A professional-grade CI solution",
      "has_free_trial": true,
      "id": 1313,
      "monthly_price_in_cents": 1099,
      "name": "Pro",
      "number": 3,
      "price_model": "flat-rate",
      "state": "published",
      "unit_name": null,
      "url": "https://api.github.com/marketplace_listing/plans/1313",
      "yearly_price_in_cents": 11870
    },
    "unit_count": null,
    "updated_at": "2017-11-02T01:12:12Z"
  },
  "organization_billing_email": "billing@github.com",
  "type": "Organization",
  "url": "https://api.github.com/orgs/github"
}
    ```

    


=== "GET Get a subscription plan for an account"

    Shows whether the user or organization account actively subscribes to a plan listed by the authenticated GitHub App. When someone submits a plan change that won't be processed until the end of their billing cycle, you will also see the upcoming pending change.

GitHub Apps must use a [JWT](https://developer.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://developer.github.com/v3/auth/#basic-authentication) with their client ID and client secret to access this endpoint.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:account_id` | `string` | Yes | (Required) account_id parameter | `<integer>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "id": 4,
  "login": "github",
  "marketplace_pending_change": {
    "effective_date": "2017-11-11T00:00:00Z",
    "id": 77,
    "plan": {
      "accounts_url": "https://api.github.com/marketplace_listing/plans/1111/accounts",
      "bullets": [
        "Up to 10 private repositories",
        "3 concurrent builds"
      ],
      "description": "A professional-grade CI solution",
      "has_free_trial": true,
      "id": 1111,
      "monthly_price_in_cents": 699,
      "name": "Startup",
      "number": 2,
      "price_model": "flat-rate",
      "state": "published",
      "unit_name": null,
      "url": "https://api.github.com/marketplace_listing/plans/1111",
      "yearly_price_in_cents": 7870
    },
    "unit_count": null
  },
  "marketplace_purchase": {
    "billing_cycle": "monthly",
    "free_trial_ends_on": "2017-11-11T00:00:00Z",
    "next_billing_date": "2017-11-11T00:00:00Z",
    "on_free_trial": true,
    "plan": {
      "accounts_url": "https://api.github.com/marketplace_listing/plans/1313/accounts",
      "bullets": [
        "Up to 25 private repositories",
        "11 concurrent builds"
      ],
      "description": "A professional-grade CI solution",
      "has_free_trial": true,
      "id": 1313,
      "monthly_price_in_cents": 1099,
      "name": "Pro",
      "number": 3,
      "price_model": "flat-rate",
      "state": "published",
      "unit_name": null,
      "url": "https://api.github.com/marketplace_listing/plans/1313",
      "yearly_price_in_cents": 11870
    },
    "unit_count": null,
    "updated_at": "2017-11-02T01:12:12Z"
  },
  "organization_billing_email": "billing@github.com",
  "type": "Organization",
  "url": "https://api.github.com/orgs/github"
}
    ```

    

