#!/usr/bin/env node
const fs = require('fs');
const p = __dirname + '/todo-mini.json';
const [,,cmd,...args]=process.argv;
const load=()=>fs.existsSync(p)?JSON.parse(fs.readFileSync(p,'utf8')):[];
const save=(d)=>fs.writeFileSync(p,JSON.stringify(d,null,2));
const d=load();
if(cmd==='add'){const t=args.join(' ').trim(); if(!t){console.error('ERR missing text'); process.exit(1);} d.push({id:d.length+1,text:t}); save(d); console.log('OK add');}
else if(cmd==='list'){if(!d.length) console.log('EMPTY'); else d.forEach(x=>console.log(`${x.id}. ${x.text}`));}
else{console.log('USAGE add <text> | list'); process.exit(1);}
