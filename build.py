#!/usr/bin/env python3
import json

with open("/data/telegram_abuse_reports/reports.json") as f:
    reports = json.load(f)

def js_esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

rjs = []
for r in reports:
    rjs.append('{"s":`' + js_esc(r["s"]) + '`,"b":`' + js_esc(r["b"]) + '`}')
rstr = "[" + ",".join(rjs) + "]"

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mass Report Toolkit - @Kont_Media</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0d1117;color:#c9d1d9;font-family:'Segoe UI',Tahoma,sans-serif}
.hero{background:linear-gradient(135deg,#161b22,#1c2333);padding:25px 15px;text-align:center;border-bottom:2px solid #f0883e}
.hero h1{color:#f0883e;font-size:18px;margin-bottom:5px}
.hero p{color:#8b949e;font-size:12px}
.stats{display:flex;gap:10px;justify-content:center;margin-top:10px;flex-wrap:wrap}
.stat{background:#0d1117;border:1px solid #30363d;border-radius:8px;padding:8px 15px;text-align:center}
.stat .n{color:#f0883e;font-size:20px;font-weight:bold}
.stat .l{color:#8b949e;font-size:10px}
.controls{background:#161b22;padding:12px 15px;border-bottom:1px solid #30363d;position:sticky;top:0;z-index:100}
.ci{max-width:1000px;margin:0 auto;display:flex;gap:6px;flex-wrap:wrap;align-items:center}
.ci select{background:#0d1117;border:1px solid #30363d;color:#c9d1d9;padding:7px 10px;border-radius:5px;font-size:12px;flex:1;min-width:200px}
.b{padding:7px 12px;border-radius:5px;border:none;cursor:pointer;font-weight:bold;font-size:11px;color:#fff}
.bg{background:#238636}.bb{background:#1f6feb}.bo{background:#f0883e;color:#000}.br{background:#da3633}
.prog{width:100%;height:3px;background:#21262d;border-radius:2px;margin-top:6px}
.pf{height:100%;background:#238636;border-radius:2px;transition:width .3s;width:0%}
.reports{max-width:1000px;margin:0 auto;padding:12px}
.rc{background:#161b22;border:1px solid #30363d;border-radius:8px;margin-bottom:8px;overflow:hidden}
.rc.sent{border-color:#238636}
.rh{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;cursor:pointer;background:#1c2333}
.rh .rn{color:#f0883e;font-weight:bold;font-size:12px;min-width:30px}
.rh .rs{color:#c9d1d9;font-size:11px;flex:1;margin:0 8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.rh .rb{background:#21262d;color:#8b949e;font-size:9px;padding:2px 6px;border-radius:8px}
.rbs{display:none;padding:14px}
.rbs.open{display:block}
.ep{background:#0d1117;border:1px solid #21262d;border-radius:5px;padding:12px;font-family:Consolas,monospace;font-size:10px;line-height:1.6;white-space:pre-wrap;word-break:break-word;max-height:400px;overflow-y:auto;margin-bottom:8px}
.ep::-webkit-scrollbar{width:4px}
.ep::-webkit-scrollbar-thumb{background:#30363d;border-radius:2px}
.br2{display:flex;gap:5px;flex-wrap:wrap}
.toast{position:fixed;bottom:15px;left:50%;transform:translateX(-50%);background:#238636;color:#fff;padding:8px 20px;border-radius:6px;font-size:12px;font-weight:bold;z-index:999;display:none}
.toast.show{display:block}
.footer{text-align:center;padding:20px;color:#484f58;font-size:10px;border-top:1px solid #21262d}
</style>
</head>
<body>
<div class="hero">
<h1>⚡ Mass Report Toolkit - @Kont_Media</h1>
<p>200 unique reports for abuse@telegram.org | Channel ID: -1002778167643</p>
<div class="stats">
<div class="stat"><div class="n" id="tc">200</div><div class="l">Total</div></div>
<div class="stat"><div class="n" id="sc">0</div><div class="l">Sent</div></div>
<div class="stat"><div class="n" id="rc">200</div><div class="l">Remaining</div></div>
</div></div>
<div class="controls"><div class="ci">
<select id="sel" onchange="show(this.value)"><option value="-1">Select report...</option></select>
<button class="b bg" onclick="rnd()">🎲 Random</button>
<button class="b bb" onclick="cpC()">📋 Copy</button>
<button class="b bo" onclick="sdC()">📧 Send</button>
<button class="b bg" onclick="nx()">⚡ Next Uns</button>
<button class="b br" onclick="rst()">🔄 Reset</button>
</div><div class="prog"><div class="pf" id="pf"></div></div></div>
<div class="reports" id="rpts"></div>
<div class="footer">Send to: abuse@telegram.org | @Kont_Media (ID: -1002778167643) | @Adolf_media | @Shadow_Cyber</div>
<div class="toast" id="toast"></div>
<script>
var R=''' + rstr + ''';
var S=JSON.parse(localStorage.getItem('km_s')||'{}');
var cur=-1;
function init(){
var s=document.getElementById('sel');
for(var i=0;i<R.length;i++){var o=document.createElement('option');o.value=i;o.text='#'+(i+1)+' '+R[i].s.substring(0,60)+'...';s.appendChild(o)}
rn();us()}
function rn(){var c=document.getElementById('rpts');c.innerHTML='';
for(var i=0;i<R.length;i++){var d=document.createElement('div');d.className='rc'+(S[i]?' sent':'');
d.innerHTML='<div class="rh" onclick="tg('+i+')"><span class="rn">#'+(i+1)+'</span><span class="rs">'+R[i].s+'</span><span class="rb">'+(S[i]?'✅ Sent':'Unsent')+'</span></div><div class="rbs" id="b'+i+'"><div class="ep">'+esc(R[i].b)+'</div><div class="br2"><button class="b bb" onclick="cp('+i+')">📋 Copy</button><button class="b bo" onclick="sd('+i+')">📧 Send</button><button class="b bg" onclick="ms('+i+')">✅ Mark Sent</button></div></div>';c.appendChild(d)}}
function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function tg(i){var e=document.getElementById('b'+i);e.classList.toggle('open');cur=i;document.getElementById('sel').value=i}
function show(v){if(v<0)return;cur=+v;document.querySelectorAll('.rbs.open').forEach(function(x){x.classList.remove('open')});document.getElementById('b'+cur).classList.add('open')}
function rnd(){var i=Math.floor(Math.random()*R.length);document.getElementById('sel').value=i;show(i);document.getElementById('rpts').children[i].scrollIntoView({behavior:'smooth',block:'center'})}
function cp(i){navigator.clipboard.writeText(R[i].b).then(function(){ts('#'+(i+1)+' copied')})}
function cpC(){if(cur>=0)cp(cur);else ts('Select a report first')}
function sd(i){window.open('mailto:abuse@telegram.org?subject='+encodeURIComponent(R[i].s)+'&body='+encodeURIComponent(R[i].b),'_blank');ts('Opening email...')}
function sdC(){if(cur>=0)sd(cur);else ts('Select a report first')}
function ms(i){S[i]=1;localStorage.setItem('km_s',JSON.stringify(S));rn();us();ts('#'+(i+1)+' marked sent')}
function nx(){for(var i=0;i<R.length;i++){if(!S[i]){sd(i);cur=i;document.getElementById('sel').value=i;document.getElementById('rpts').children[i].scrollIntoView({behavior:'smooth',block:'center'});return}}ts('All reports sent!')}
function us(){var c=0;for(var k in S)if(S[k])c++;document.getElementById('sc').textContent=c;document.getElementById('rc').textContent=200-c;document.getElementById('pf').style.width=((c/200)*100)+'%'}
function rst(){if(confirm('Reset all tracking?')){S={};localStorage.removeItem('km_s');rn();us();ts('Reset done')}}
function ts(m){var t=document.getElementById('toast');t.textContent=m;t.classList.add('show');setTimeout(function(){t.classList.remove('show')},2000)}
init();
</script>
</body></html>'''

with open("/data/telegram_abuse_reports/index.html", "w") as f:
    f.write(html)
print(f"HTML saved: {len(html)} bytes")
