# licenses API


=== "GET Get all commonly used licenses"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `featured` | `string` | Yes | No description. | `<boolean>` |
    | `per_page` | `string` | Yes | Results per page (max 100) | `30` |
    
    

    

    #### Response Example
    
    ```json
    [
  {
    "key": "mit",
    "name": "MIT License",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "MIT",
    "url": "https://api.github.com/licenses/mit"
  },
  {
    "key": "lgpl-3.0",
    "name": "GNU Lesser General Public License v3.0",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "LGPL-3.0",
    "url": "https://api.github.com/licenses/lgpl-3.0"
  },
  {
    "key": "mpl-2.0",
    "name": "Mozilla Public License 2.0",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "MPL-2.0",
    "url": "https://api.github.com/licenses/mpl-2.0"
  },
  {
    "key": "agpl-3.0",
    "name": "GNU Affero General Public License v3.0",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "AGPL-3.0",
    "url": "https://api.github.com/licenses/agpl-3.0"
  },
  {
    "key": "unlicense",
    "name": "The Unlicense",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "Unlicense",
    "url": "https://api.github.com/licenses/unlicense"
  },
  {
    "key": "apache-2.0",
    "name": "Apache License 2.0",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "Apache-2.0",
    "url": "https://api.github.com/licenses/apache-2.0"
  },
  {
    "key": "gpl-3.0",
    "name": "GNU General Public License v3.0",
    "node_id": "MDc6TGljZW5zZW1pdA==",
    "spdx_id": "GPL-3.0",
    "url": "https://api.github.com/licenses/gpl-3.0"
  }
]
    ```

    


=== "GET Get a license"

    No description.

    
    #### Parameters

    | Parameter | Type | Required | Description | Example |
    | --- | --- | --- | --- | --- |
    | `:license` | `string` | Yes | (Required) license parameter | `<string>` |
    
    

    

    #### Response Example
    
    ```json
    {
  "body": "\n\nThe MIT License (MIT)\n\nCopyright (c) [year] [fullname]\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the \"Software\"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n",
  "conditions": [
    "include-copyright"
  ],
  "description": "A permissive license that is short and to the point. It lets people do anything with your code with proper attribution and without warranty.",
  "featured": true,
  "html_url": "http://choosealicense.com/licenses/mit/",
  "implementation": "Create a text file (typically named LICENSE or LICENSE.txt) in the root of your source code and copy the text of the license into the file. Replace [year] with the current year and [fullname] with the name (or names) of the copyright holders.",
  "key": "mit",
  "limitations": [
    "no-liability"
  ],
  "name": "MIT License",
  "node_id": "MDc6TGljZW5zZW1pdA==",
  "permissions": [
    "commercial-use",
    "modifications",
    "distribution",
    "sublicense",
    "private-use"
  ],
  "spdx_id": "MIT",
  "url": "https://api.github.com/licenses/mit"
}
    ```

    

