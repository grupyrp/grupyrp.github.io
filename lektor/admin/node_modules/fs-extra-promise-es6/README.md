# fs-extra-promise-es6
[![Build Status](https://travis-ci.org/vinsonchuong/fs-extra-promise-es6.svg?branch=master)](https://travis-ci.org/vinsonchuong/fs-extra-promise-es6)

An ES6 promise adapter for fs-extra for use with ES7 async/await,

## Installing
`fs-extra-promise-es6` is available as an
[npm package](https://www.npmjs.com/package/fs-extra-promise-es6).

## Usage
```js
import * as fse from 'fs-extra-promise-es6';

async function run() {
  console.log(await fse.readJson('package.json'));
}
run();
```

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
