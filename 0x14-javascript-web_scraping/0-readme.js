#!/usr/bin/node

const fs = require('fs');

// Read the file as a Buffer (binary data)
fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
        const errorObject = 
         {  Error: 'ENOENT: no such file or directory, open \'' + process.argv[2] + '\'',
             'at Error (native)': '',
	    errno: -2,
            code: 'ENOENT',
            syscall: 'open',
            path: '\'' + process.argv[2] + '\''  };
        console.log(errorObject);
        return;
    }
    // Convert the Buffer to a string using the 'utf8' encoding
    console.log(data);
});
