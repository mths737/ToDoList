window.onload = async function() {
  if (document.getElementById('alert') != null) {
    await sleep(2000)
    document.getElementById('alert').style.animation = 'alert-out 0.5s'
    await sleep(500)
    document.getElementById('alert').style.display = 'none'
  }

  if (document.getElementById('msg')) {
    let msg = document.getElementById('msg')
    await sleep(4000)
    msg.style.animation = 'boxMsgOut 2s'
    await sleep(2000)
    msg.style.display = 'none'
  }
}

function sleep(ms) {
    return new Promise(
      resolve => setTimeout(resolve, ms)
    );
}