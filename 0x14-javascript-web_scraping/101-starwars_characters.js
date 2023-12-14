#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/`process.argv[2]`';
request(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    print(chars, 0);
  }
});

function print (chars, index) {
  request(chars[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < chars.length) {
        print(chars, index + 1);
      }
    }
  });
}
