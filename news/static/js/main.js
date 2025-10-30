

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

  const subscribe = document.getElementById('subscribe')
  const subscribeBtn = document.getElementById('subscribe-btn')
  const message = document.getElementById('dialog-message')

  subscribe.addEventListener('change', (e) => {
    const email = e.target.value

    if (!email.includes('@')) {
      message.innerText = 'Enter a valid email!';
      message.style.color = 'red';
      return
    }
    
    subscribeBtn.disabled = false;
    message.innerText = '';
  })


  //  Jquery
  $('#myForm').on('submit', function(e) {
  e.preventDefault();

  const data = $(this).serialize()
  $.ajax({
    type: 'POST',
    url: '/subscribe/',
    data: data,
    headers: { 'X-CSRFToken': getCookie('csrftoken') },
    success: function(response) {
      console.log('Success:', response);
      message.innerText = 'Subscription Successful! ✅';
      message.style.color = 'green';
      subscribe.value = '';
      subscribeBtn.disabled = true;
      
      setTimeout(() => {
        message.innerText = '';
      }, 7000)
    },
    error: function(xhr, status, error) {
      const res = JSON.parse(xhr.responseText);
      console.log('Status:', res.error);

      message.innerText = res.error;
      message.style.color = 'red';

      subscribe.value = '';
      subscribeBtn.disabled = true;

      setTimeout(() => {
        message.innerText = '';
      }, 5000)
    }
  });
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Share handling


const fb = document.getElementById('fb');
const x = document.getElementById('x');
const whatsapp = document.getElementById('whatsapp');


const share = (platform) => {
  const currentURL = window.location.href;
  let title = currentURL.split('/')[3].split('-');

  let header = ''
  
  for (t = 0; t< title.length; t++) {

    let title1 = title[t].charAt(0).toUpperCase() + title[t].slice(1)
    header += title1

    if (t != title.length) {
      header += ' '
    }
  }

  if (platform === 'x') {
    window.open(`https://x.com/intent/tweet?text=${encodeURIComponent('Updates247: '+header+'.')}&url=${encodeURIComponent(currentURL)}`);
    return 
  } else if (platform === 'whatsapp') {
      window.open(
  `https://api.whatsapp.com/send?text=${encodeURIComponent('Updates247: ' + header)}` +
  '%0A' + // new line
  encodeURIComponent(currentURL)
);
    return 
  }  else if (platform === 'fb') {
    let fbUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + currentURL

    console.log(fbUrl)
window.open(
  fbUrl,
  '_blank'
)
    return;
  }
  return
  
}

fb.addEventListener('click', () => share('fb'))
x.addEventListener('click', () => share('x'))
whatsapp.addEventListener('click', () => share('whatsapp'))
});

