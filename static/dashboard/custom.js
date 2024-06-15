$(document).ready(function () {
  $(".list-group-item").click(function () {
    $(".list-group-item").removeClass("active");
    $(this).addClass("active");
  });

  $("#uploadstudent").on("click", function () {
    $("#uploadform").show();
    $("#facultyuploadform").hide();
  });

  $("#uploadfaculty").on("click", function () {
    $("#uploadform").hide();
    $("#facultyuploadform").show();
  });

  $("#student-upload-form").on("submit", function (e) {
    e.preventDefault();
    var formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/dashboard/bulk/upload/student/", // Make sure this URL is correct
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#message").html(
          '<div class="alert alert-success">Students have been uploaded successfully.</div>'
        );
        $("#student-upload-form")[0].reset();
      },
      error: function (response) {
        $("#message").html(
          '<div class="alert alert-danger">There was an error uploading the students. Please try again.</div>'
        );
      },
    });
  });

  $("#faculty-upload-form").on("submit", function (e) {
    e.preventDefault();
    var formData = new FormData(this);

    $.ajax({
      type: "POST",
      url: "/dashboard/bulk/upload/faculty/", // Make sure this URL is correct
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
        $("#message2").html(
          '<div class="alert alert-success">Faculties have been uploaded successfully.</div>'
        );
        $("#faculty-upload-form")[0].reset();
      },
      error: function (response) {
        $("#message2").html(
          '<div class="alert alert-danger">There was an error uploading the faculties. Please try again.</div>'
        );
      },
    });
  });
});
