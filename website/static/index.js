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