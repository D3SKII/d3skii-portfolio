const dialog=document.querySelector('dialog');
const player=dialog?.querySelector('video');
let opener;
document.querySelectorAll('[data-video]').forEach(button=>button.addEventListener('click',()=>{opener=button;player.src=button.dataset.video;player.poster=button.dataset.poster||'';dialog.querySelector('[data-title]').textContent=button.getAttribute('aria-label');dialog.showModal();player.play().catch(()=>{});}));
function closePlayer(){dialog.close()}
dialog?.querySelector('[data-close]').addEventListener('click',closePlayer);
dialog?.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)closePlayer()}});
dialog?.addEventListener('close',()=>{player.pause();player.removeAttribute('src');player.load();opener?.focus()});
