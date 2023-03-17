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


  function copypass(note) {
    /* Get the text field */
    var copyText = document.getElementById(note);
  
    /* Select the text field */
    copyText.select();
  
    /* Copy the text inside the text field */
    document.execCommand("copy");
  }