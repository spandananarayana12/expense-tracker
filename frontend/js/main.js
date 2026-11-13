const API='/api';
function isLoggedIn(){return !!localStorage.getItem('expense_user');}
function currentUser(){try{return JSON.parse(localStorage.getItem('expense_user'))||null}catch{return null}}
function requireAuth(){if(!isLoggedIn() && !location.pathname.endsWith('login.html') && !location.pathname.endsWith('register.html') && !location.pathname.endsWith('index.html') && !location.pathname.endsWith('about.html')) location.href='login.html';}
function logout(){localStorage.removeItem('expense_user');fetch(API+'/auth/logout',{method:'POST'}).finally(()=>location.href='login.html');}
document.addEventListener('DOMContentLoaded',()=>{if(document.querySelector('.layout'))requireAuth();const l=document.getElementById('logout');if(l)l.onclick=logout;});
async function api(path,options={}){const res=await fetch(API+path,{headers:{'Content-Type':'application/json',...(options.headers||{})},...options});let data={};try{data=await res.json()}catch{}if(!res.ok)throw new Error(data.message||'Request failed');return data}
function money(value){return '₹'+Number(value||0).toLocaleString('en-IN',{maximumFractionDigits:2})}
function setMessage(el,msg,type='success'){if(!el)return;el.textContent=msg;el.className='message '+type;setTimeout(()=>{el.textContent=''},3500)}
