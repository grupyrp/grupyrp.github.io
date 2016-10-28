# register-module
Register a module with Node.js for more concise imports.

## Installing
`register-module` is available as an
[npm package](https://www.npmjs.com/package/register-module).

## Usage
```js
require('register-module')({
  name: 'project',
  path: '/home/vinsonchuong/project',
  main: 'entry.js'
});

// Resolves to '/home/vinsonchuong/project/entry.js'
require('project');

// Resolves to '/home/vinsonchuong/project/lib.js'
require('project/lib');
```
