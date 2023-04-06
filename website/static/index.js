function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function showPasswd(note) {
    var x = document.getElementById(note);
    if (x.type === "password") {
        x.type = "text";
      } 
    else {
        x.type = "password";
      }
    }


 function copyPasswd(note) {
    var copyText = document.getElementById(note);
    copyText.select()
    navigator.clipboard.writeText(copyText.value);
  }

setTimeout(function() {
    $('.alert').alert('close');
}, 3000);



function updateNote(noteId) {
  var username = document.getElementById('username_to_update_' + noteId).value;
  var password = document.getElementById('password_to_update_' + noteId).value;

  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/update-note', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      document.getElementById('username_to_update_' + noteId).value = username;
      document.getElementById('password_to_update_' + noteId).value = password;
      $('#myModal' + noteId).modal('hide');
      location.reload();
    }
  };
  xhr.send(JSON.stringify({
    'noteId': noteId,
    'username': username,
    'password': password
  }));
}

