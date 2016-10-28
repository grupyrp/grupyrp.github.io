# node-promise-es6
[![Build Status](https://travis-ci.org/vinsonchuong/node-promise-es6.svg?branch=master)](https://travis-ci.org/vinsonchuong/node-promise-es6)

ES6 promise adapters for the [Node.js API](https://nodejs.org/api/) for use
with [ES7 async/await](https://github.com/lukehoban/ecmascript-asyncawait).

## Installing
`node-promise-es6` is available as an
[npm package](https://www.npmjs.com/package/node-promise-es6).

## Usage

### Wrapped APIs

#### fs
```js
import {fs} from 'node-promise-es6';

async function run() {
  console.log(await fs.readdir('.'));
}
```

#### child_process
```js
import {childProcess} from 'node-promise-es6';

async function run() {
  const {stdout, stderr} = await childProcess.exec('ls .');
  console.log(stdout, stderr);
}
```

### Utilities

#### promisify
```js
import {promisify} from 'node-promise-es6';

function callbackFn(x, y, callback) {
  callback(null, x, y);
}

async function run() {
  const promiseFn = promisify(callbackFn, ['x', 'y']);
  const {x, y} = await promiseFn(1, 2);
  console.log(x === 1 && y === 2);
}
```

A helper for wrapping Node.js-style callback-taking functions (error object as
first argument) in a Promise API.

## Development
### Getting Started
The application requires the following external dependencies:
* Node.js

The rest of the dependencies are handled through:
```bash
npm install
```

Run tests with:
```bash
npm test
```
