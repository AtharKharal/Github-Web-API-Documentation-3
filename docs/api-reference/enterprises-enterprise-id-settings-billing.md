# enterprises/{enterprise id}/settings/billing API


=== "GET Get GitHub Actions billing for an enterprise"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the summary of the free and paid GitHub Actions minutes used.

Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage does not include the multiplier for macOS and Windows runners and is not rounded up to the nearest whole minute. For more information, see "[Managing billing for GitHub Actions](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)".

The authenticated user must be an enterprise admin.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:enterprise_id` | `string` | Yes | (Required) Unique identifier of the GitHub Enterprise Cloud instance. | `<string>` |
    
    

    

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

    


=== "GET Get GitHub Packages billing for an enterprise"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the free and paid storage used for GitHub Packages in gigabytes.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

The authenticated user must be an enterprise admin.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:enterprise_id` | `string` | Yes | (Required) Unique identifier of the GitHub Enterprise Cloud instance. | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "included_gigabytes_bandwidth": 10,
  "total_gigabytes_bandwidth_used": 50,
  "total_paid_gigabytes_bandwidth_used": 40
}
    ```

    


=== "GET Get shared storage billing for an enterprise"

    **Warning:** The Billing API is currently in public beta and subject to change.

Gets the estimated paid and estimated total storage used for GitHub Actions and Github Packages.

Paid minutes only apply to packages stored for private repositories. For more information, see "[Managing billing for GitHub Packages](https://help.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages)."

The authenticated user must be an enterprise admin.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:enterprise_id` | `string` | Yes | (Required) Unique identifier of the GitHub Enterprise Cloud instance. | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "days_left_in_billing_cycle": 20,
  "estimated_paid_storage_for_month": 15,
  "estimated_storage_for_month": 40
}
    ```

    

