const http=require('http');
function req(method,path,body){return new Promise((resolve,reject)=>{const data=body?Buffer.from(JSON.stringify(body)):null;const r=http.request({hostname:'127.0.0.1',port:20129,path,method,headers:data?{'content-type':'application/json','content-length':data.length}:{}},res=>{let out='';res.on('data',d=>out+=d);res.on('end',()=>{let json;try{json=JSON.parse(out)}catch{} resolve({status:res.statusCode,out,json});});});r.on('error',reject);if(data)r.write(data);r.end();});}
async function wait(ms){return new Promise(r=>setTimeout(r,ms));}
async function runCase(mode, decision){
  await req('POST','/api/runs/start',{task:`e2e ${mode} ${decision}`,mode});
  await wait(mode==='fail-at-qa'?12500:10500);
  const st=await req('GET','/api/state');
  const run=st.json.runs[0];
  if(!run || !run.runId) throw new Error('missing run');
  const mb=await req('GET','/api/mailbox/qa');
  if(mb.status!==200 || !mb.out.includes('handoff')) throw new Error('mailbox handoff missing');
  const rv=await req('POST','/api/review/decision',{runId:run.runId,nodeId:'qa',decision,reason:`e2e ${decision}`});
  if(rv.status!==200 || rv.json.review.decision!==decision) throw new Error('review failed');
  const files=await req('GET',`/api/runs/${run.runId}/files`);
  if(files.status!==200 || !files.out.includes('kind')) throw new Error('files kind missing');
  const prev=await req('GET',`/api/runs/${run.runId}/file/timeline.log`);
  if(prev.status!==200 || prev.json.kind!=='text') throw new Error('preview failed');
  const ex=await req('POST',`/api/runs/${run.runId}/export`);
  if(ex.status!==200 || ex.json.fileName!=='run-report.md') throw new Error('export failed');
  const rp=await req('GET',`/api/runs/${run.runId}/file/run-report.md`);
  if(rp.status!==200 || !rp.out.includes('Mailbox Events')) throw new Error('report content missing');
  return { runId: run.runId, mode, decision, finalStatus: rv.json.run.status, report: ex.json.report };
}
(async()=>{
  const normal=await runCase('normal','accept');
  const retry=await runCase('fail-at-qa','rework');
  console.log('E2E_ACCEPTANCE_OK');
  console.log(JSON.stringify({normal,retry},null,2));
})().catch(e=>{console.error('E2E_ACCEPTANCE_FAIL',e);process.exit(1)});
