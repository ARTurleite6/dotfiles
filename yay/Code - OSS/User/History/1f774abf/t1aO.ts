import { readFile } from "fs";

function main() {
    readFile("src/main.ts", (err, data) => {
        if(err) {
            console.log('error reading file');
        } else {
            console.log(data.toString());
        }
    })
}

main();