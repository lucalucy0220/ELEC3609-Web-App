const editProfileBtn = document.getElementById("editProfile");
const profileImg = document.getElementById("profile-pic");
const clickProfileImage = ()=>{
    document.getElementById('id_picture').click();
}

$(document).ready(function() {
    $("#editProfile").click(function(){
        $("#editing").css("display", $("#editing").css("display") === 'none' ? 'block' : 'none');
        $("#showing").css("display", $("#showing").css("display") === 'none' ? 'block' : 'none');
        $("#editProfile").css("display", $("#editProfile").css("display") === 'none' ? 'block' : 'none');
        $("#saveProfile").css("display", $("#saveProfile").css("display") === 'none' ? 'block' : 'none');
        $(".middle").css("display", $(".middle").css("display") === 'none' ? 'block' : 'none');
        $("#profile-pic").toggleClass("inEditing");
        profileImg.addEventListener("click", clickProfileImage);

    });
    $("#saveProfile").submit(function(){
        $("#showing").css("display", $("#showing").css("display") === 'none' ? 'block' : 'none');
        $("#editProfile").css("display", $("#editProfile").css("display") === 'none' ? 'block' : 'none');
        $("#saveProfile").css("display", $("#saveProfile").css("display") === 'none' ? 'block' : 'none');
        $(".middle").css("display", $(".middle").css("display") === 'none' ? 'block' : 'none');
        $("#profile-pic").toggleClass("inEditing");
        profileImg.removeEventListener("click", clickProfileImage);
    });

});

let file_input = document.querySelector('#id_picture');
let image_preview = document.querySelector('#profile-pic');

const handle_file_preview = (e) => {
  let files = e.target.files;
    if(files.length>0){
        $("#upload-message").css("display", $("#upload-message").css("display") === 'none' ? 'block' : 'none');
    }
}

file_input.addEventListener('change', handle_file_preview);