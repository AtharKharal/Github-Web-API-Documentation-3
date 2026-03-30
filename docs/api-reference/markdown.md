# markdown API


=== "POST Render a Markdown document"

    No description.

    

    
    #### Request Body
    
    ```json
    {
  "context": "\u003cstring\u003e",
  "mode": "markdown",
  "text": "\u003cstring\u003e"
}
    ```
    

    #### Response Example
    
    ```json
    {
  "raw": ""
}
    ```

    


=== "POST Render a Markdown document in raw mode"

    You must send Markdown as plain text (using a `Content-Type` header of `text/plain` or `text/x-markdown`) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

    

    
    #### Request Body
    
    ```json
    "\u003cstring\u003e"
    ```
    

    #### Response Example
    
    ```json
    {
  "raw": "anim"
}
    ```

    

