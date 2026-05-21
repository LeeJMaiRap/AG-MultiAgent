#!/usr/bin/env node
const fs=require("fs"); const p=__dirname+"/todo-real.json";
const [,,cmd,...args]=process.argv; const d=fs.existsSync(p)?JSON.parse(fs.readFileSync(p,"utf8")):[];
const save=()=>fs.writeFileSync(p,JSON.stringify(d,null,2));
if(cmd==="add"){const t=args.join(" ").trim(); if(!t){console.error("ERR missing text"); process.exit(1);} d.push({id:d.length+1,text:t,done:false}); save(); console.log("OK add");}
else if(cmd==="list"){if(!d.length) console.log("EMPTY"); else d.forEach(x=>console.log(`${x.id}. [${x.done?"x":" "}] ${x.text}`));}
else if(cmd==="done"){const id=Number(args[0]); if(!Number.isInteger(id)||id<1||id>d.length){console.error("ERR invalid id"); process.exit(1);} d[id-1].done=true; save(); console.log("OK done");}
else{console.log("USAGE add <text> | list | done <id>"); process.exit(1);} 
