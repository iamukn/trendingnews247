

document.addEventListener('DOMContentLoaded', () => {
 function shareNews (event) {
    event.stopPropagation(); 
    alert('Sharing coming soon')
}
  const share_btn = document.querySelectorAll('.share-btn')
  
  share_btn.forEach(share => {
    share.addEventListener('click', shareNews)
  });


  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Alert clicked')
  }

  alert('Ran')
});

