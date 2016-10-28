'use strict';
const Module = require('module').Module;

const modules = [];

const oldResolveFilename = Module._resolveFilename;
Module._resolveFilename = function(request, parent, isMain) {
  for (const {name, path, main} of modules) {
    if (request === name) {
      return oldResolveFilename(`${path}/${main}`, parent, isMain);
    }

    if (request.startsWith(`${name}/`)) {
      return oldResolveFilename(request.replace(name, path), parent, isMain);
    }
  }

  return oldResolveFilename(request, parent, isMain);
};

module.exports = function(moduleDefinition) {
  modules.push(moduleDefinition);
};
