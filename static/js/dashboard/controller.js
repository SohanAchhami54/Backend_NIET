app.controller("dashboardController", function ($scope, $http) {
  $scope.showStudent = false;
  $scope.showTeacher = false;
  $scope.showPasswordReset = false;
  $scope.showSubjectTeacher = false;
  $scope.showStudentUpgrade = false;
  $scope.showStudentList = false;
  $scope.showStudentRecord = false;

  $scope.semesterList = null;
  $scope.teacherList = null;
  $scope.subjectList = null;
  $scope.studentListByBatch = null;
  $scope.subjectTeacherList = null;
  $scope.batchSemesterList = null;
  $scope.selectedBatchsemester = null;
  $scope.subjectTeacherDetailList = null;
  $scope.studentNotices = null;
  $scope.studentRecord = null;
  $scope.selectedStudent = null;
  $scope.groupedTeachers = {};

  $scope.student = {
    email: "",
    first_name: "",
    last_name: "",
    photo: "",
    registration_number: "",
    batchsemester: "",
  };
  $scope.teacher = {
    email: "",
    photo: "",
    password: "",
    full_name: "",
  };
  $scope.user = {
    email: "",
    password: "",
    confirm_password: "",
  };
  $scope.subjectteacher = {
    selectedTeacher: "",
    selectedSubject: "",
  };
  $scope.upgrade = {
    registration_number: "",
    batchsemester: "",
  };
  $scope.handleStudent = function () {
    $scope.showStudent = true;
    $scope.showTeacher = false;
    $scope.showPasswordReset = false;
    $scope.showSubjectTeacher = false;
    $scope.showStudentUpgrade = false;
    $scope.showStudentList = false;
    $scope.showStudentRecord = false;
    console.log($scope.showStudent);
  };
  $scope.handleTeacher = function () {
    $scope.showStudent = false;
    $scope.showTeacher = true;
    $scope.showPasswordReset = false;
    $scope.showSubjectTeacher = false;
    $scope.showStudentUpgrade = false;
    $scope.showStudentList = false;
    $scope.showStudentRecord = false;
  };
  $scope.handlePasswordReset = function () {
    $scope.showStudent = false;
    $scope.showTeacher = false;
    $scope.showPasswordReset = true;
    $scope.showSubjectTeacher = false;
    $scope.showStudentUpgrade = false;
    $scope.showStudentList = false;
    $scope.showStudentRecord = false;
  };
  $scope.handleSubjectTeacher = function () {
    $scope.showStudent = false;
    $scope.showTeacher = false;
    $scope.showPasswordReset = false;
    $scope.showSubjectTeacher = true;
    $scope.showStudentUpgrade = false;
    $scope.showStudentList = false;
    $scope.showStudentRecord = false;
  };
  $scope.upgradeStudentSemester = function () {
    $scope.showStudent = false;
    $scope.showTeacher = false;
    $scope.showPasswordReset = false;
    $scope.showSubjectTeacher = false;
    $scope.showStudentUpgrade = true;
    $scope.showStudentList = false;
    $scope.showStudentRecord = false;
  };
  $scope.handleStudentList = function () {
    $scope.showStudent = false;
    $scope.showTeacher = false;
    $scope.showPasswordReset = false;
    $scope.showSubjectTeacher = false;
    $scope.showStudentUpgrade = false;
    $scope.showStudentList = true;
    $scope.showStudentRecord = false;
  };

  $scope.presentCount = function (records) {
    return records.filter(function (record) {
      return record.status === true; // Count where status is 'Present'
    }).length;
  };

  $scope.absentCount = function (records) {
    return records.filter(function (record) {
      return record.status === false; // Count where status is 'Absent'
    }).length;
  };

  // handle student register
  $scope.submitForm = function () {
    var formData = new FormData();

    // Append form fields to FormData
    formData.append("first_name", $scope.student.first_name);
    formData.append("last_name", $scope.student.last_name);
    formData.append("email", $scope.student.email);
    formData.append("file", $scope.student.photo);
    formData.append("registration_number", $scope.student.registration_number);
    formData.append("batchsemester", $scope.student.batchsemester);

    $http({
      method: "POST",
      url: "/dashboard/register/student/",
      data: formData,
      headers: {
        "Content-Type": undefined, // Important for file uploads
      },
      transformRequest: angular.identity,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "Student registered successfully!";
        $scope.errorMessage = null;

        // Reset form data
        $scope.student = {
          email: "",
          full_name: "",
          symbol_number: "",
          registration_number: "",
          batchsemester: "",
        };
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during registration!";
        $scope.successMessage = null;
      }
    );
  };

  $scope.fetchStudentRecord = function (
    batchSemester,
    studentId,
    selectedStudent
  ) {
    $scope.selectedStudent = selectedStudent;
    $scope.showStudentRecord = true;
    $http({
      method: "GET",
      url: `/dashboard/individual/student/record/${batchSemester}/${studentId}/`,
    }).then(
      function successCallback(response) {
        $scope.studentRecord = response.data;
        console.log($scope.studentRecord);

        // setTimeout(function () {
        //   $("#studentDetail").DataTable({
        //     searching: true, // Enable search functionality
        //     paging: true, // Enable pagination
        //     ordering: true, // Enable sorting
        //   });
        // }, 0);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  // fetch student list by Batch
  $scope.fetchStudentListByBatch = function (batch_sem_id) {
    $http({
      method: "GET",
      url: `/dashboard/student/lists/batch/semester/${batch_sem_id}`,
    }).then(
      function successCallback(response) {
        $scope.studentListByBatch = response.data;
        console.log($scope.studentListByBatch);

        setTimeout(function () {
          $("#studentDetail").DataTable({
            searching: true, // Enable search functionality
            paging: true, // Enable pagination
            ordering: true, // Enable sorting
          });
        }, 0);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  // handle student upgrade
  $scope.submitUpgradeForm = function () {
    $http({
      method: "POST",
      url: "/dashboard/upgrade/student/",
      data: $scope.upgrade,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "Student upgraded successfully!";
        $scope.errorMessage = null;

        // Reset form data
        $scope.upgrade = {
          registration_number: "",
          batchsemester: "",
        };
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during upgrade!";
        $scope.successMessage = null;
      }
    );
  };
  // handle teacher register
  $scope.submitTeacherForm = function () {
    var formData = new FormData();

    // Append form fields to FormData
    formData.append("full_name", $scope.teacher.full_name);
    formData.append("password", $scope.teacher.password);
    formData.append("email", $scope.teacher.email);
    formData.append("file", $scope.teacher.photo);

    $http({
      method: "POST",
      url: "/dashboard/register/teacher/",
      data: formData,
      headers: {
        "Content-Type": undefined, // Important for file uploads
      },
      transformRequest: angular.identity,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "Teacher registered successfully!";
        $scope.errorMessage = null;

        // Reset form data
        $scope.teacher = {
          email: "",
          password: "",
          full_name: "",
          photo: "",
        };
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during registration!";
        $scope.successMessage = null;
      }
    );
  };
  $scope.submitPasswordResetForm = function () {
    if ($scope.user.password !== $scope.user.confirm_password) {
      $scope.passwordMismatch = true;
      return;
    } else {
      $scope.passwordMismatch = false;
    }
    $http({
      method: "POST",
      url: "/dashboard/password/reset/",
      data: $scope.user,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "Password reset successfully!";
        $scope.errorMessage = null;

        // Reset form data
        $scope.user = {
          email: "",
          password: "",
          confirm_password: "",
        };
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during reset!";
        $scope.successMessage = null;
      }
    );
  };

  // fetch semesters
  $scope.fetchSemesters = function () {
    $http({
      method: "GET",
      url: "/dashboard/semester/lists/",
    }).then(
      function successCallback(response) {
        $scope.semesterList = response.data;
        console.log($scope.semesterList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchTeachers = function () {
    $http({
      method: "GET",
      url: "/dashboard/teacher/lists/",
    }).then(
      function successCallback(response) {
        $scope.teacherList = response.data;
        console.log($scope.teacherList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchBatchSemester = function () {
    $http({
      method: "GET",
      url: "/dashboard/batch/semester/lists/",
    }).then(
      function successCallback(response) {
        $scope.batchSemesterList = response.data;
        console.log($scope.batchSemesterList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.onSemesterChange = function (selectedSemester) {
    $http({
      method: "GET",
      url: `/dashboard/subject/lists/${selectedSemester}/`,
    }).then(
      function successCallback(response) {
        $scope.subjectList = response.data;
        console.log($scope.subjectList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );

    $http({
      method: "GET",
      url: `/dashboard/subject/teacher/lists/${selectedSemester}/`,
    }).then(
      function successCallback(response) {
        $scope.subjectTeacherList = response.data;
        console.log($scope.subjectTeacherList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  // assign subject teacher

  $scope.submitSubjectTeacherAssignForm = function () {
    $http({
      method: "POST",
      url: "/dashboard/assign/subject/teacher/",
      data: $scope.subjectteacher,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "subject Teacher registered successfully!";
        $scope.errorMessage = null;

        // Reset form data
        $scope.subjectteacher = {
          selectedTeacher: "",
          selectedSubject: "",
        };
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during registration!";
        $scope.successMessage = null;
      }
    );
  };

  $scope.fetchSubjectTeacherDetail = function () {
    $http({
      method: "GET",
      url: "/dashboard/subject/teacher/lists/",
    }).then(
      function successCallback(response) {
        $scope.subjectTeacherDetailList = response.data;
        console.log($scope.subjectTeacherDetailList);

        $scope.subjectTeacherDetailList.forEach(function (item) {
          var teacherName = item.teacher.full_name;
          if (!$scope.groupedTeachers[teacherName]) {
            $scope.groupedTeachers[teacherName] = [];
          }
          $scope.groupedTeachers[teacherName].push(item.subject);
        });
        // setTimeout(function () {
        //   $("#subjectTeacher").DataTable({
        //     searching: true, // Enable search functionality
        //     paging: true, // Enable pagination
        //     ordering: true, // Enable sorting
        //   });
        // }, 0);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchSemesters();
  $scope.fetchTeachers();
  $scope.fetchBatchSemester();
  $scope.fetchSubjectTeacherDetail();
  //   $scope.fetchSubjects();
});

// teacher dashboard controller
app.controller("teacherDashboardController", function ($scope, $http) {
  $scope.showAttendanceCreate = false;
  $scope.showMarksEntry = false;
  $scope.showAttendanceRecord = false;

  $scope.batchSemesterList = null;
  $scope.batchSubjectList = null;
  $scope.batchStudentList = null;
  $scope.selectedSubjectAttendance = null;
  $scope.examTypes = null;
  $scope.examSession = null;
  $scope.selectedSubjectForMarks = null;
  $scope.selectedExamSession = null;
  $scope.selectedExamType = null;
  $scope.records = []; // Initialize records to an empty array
  $scope.dates = [];
  $scope.attendanceRecords = [];

  $scope.attendance = {};
  $scope.marks = {};
  $scope.attendanceStatus = { date: "" };

  $scope.handleAttendaceCreate = function () {
    $scope.showAttendanceCreate = true;
    $scope.showMarksEntry = false;
    $scope.showAttendanceRecord = false;
  };

  $scope.handleMarksEntry = function () {
    $scope.showAttendanceCreate = false;
    $scope.showMarksEntry = true;
    $scope.showAttendanceRecord = false;
  };

  $scope.handleAttendaceShow = function () {
    $scope.showAttendanceCreate = false;
    $scope.showMarksEntry = false;
    $scope.showAttendanceRecord = true;
  };

  $scope.handleSubjectAttendance = function (subject_id) {
    $scope.selectedSubjectAttendance = subject_id;
    console.log($scope.selectedSubjectAttendance);
  };

  $scope.handleAttendanceFetch = function (subject_id) {
    $http({
      method: "GET",
      url: `/dashboard/attendance/record/list/${subject_id}`,
    }).then(
      function successCallback(response) {
        $scope.records = response.data;
        if ($scope.records && $scope.records.length > 0) {
          // Step 1: Extract unique dates
          $scope.dates = [...new Set($scope.records.map((item) => item.day))];

          // Step 2: Transform data to group by students
          let groupedData = {};
          $scope.records.forEach((record) => {
            let regNumber = record.student.registration_number;
            if (!groupedData[regNumber]) {
              groupedData[regNumber] = {
                registration_number: regNumber,
                attendance: {},
              };
            }
            groupedData[regNumber].attendance[record.day] = record.status;
          });

          // Step 3: Convert grouped data into array for ng-repeat
          $scope.attendanceRecords = Object.values(groupedData);
        }
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.handleSubjectMarks = function (subject_id) {
    $scope.selectedSubjectForMarks = subject_id;
    console.log($scope.selectedSubjectForMarks);
  };

  $scope.selectExamType = function (e_id) {
    $scope.selectedExamType = e_id;
    console.log($scope.selectedExamType);
  };

  $scope.selectExamSession = function (session_id) {
    $scope.selectedExamSession = session_id;
    console.log($scope.selectedExamSession);
  };

  $scope.handleBatchSemesterChange = function (selectedBatchsemester) {
    console.log(selectedBatchsemester);
    $http({
      method: "GET",
      url: `/dashboard/subject/lists/batch/semester/${selectedBatchsemester}`,
    }).then(
      function successCallback(response) {
        $scope.batchSubjectList = response.data;
        console.log($scope.batchSubjectList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );

    $http({
      method: "GET",
      url: `/dashboard/student/lists/batch/semester/${selectedBatchsemester}`,
    }).then(
      function successCallback(response) {
        $scope.batchStudentList = response.data;
        console.log($scope.batchStudentList);

        $scope.batchStudentList.forEach(function (obj) {
          $scope.attendance[obj.student.id] = true;
        });

        $scope.batchStudentList.forEach(function (obj) {
          $scope.marks[obj.student.id] = 0.0;
        });
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.saveAttendance = function () {
    var data = {
      subject: $scope.selectedSubjectAttendance,
      attendance: $scope.attendance,
      date: new Date($scope.attendanceStatus.date).toDateString(),
    };

    $http({
      method: "POST",
      url: "/dashboard/student/bulk/attendance/",
      data: data,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "subject Teacher registered successfully!";
        $scope.errorMessage = null;
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during registration!";
        $scope.successMessage = null;
      }
    );
  };
  $scope.submitBulkAttendance = function () {
    var data = {
      subject: $scope.selectedSubjectAttendance,
      attendance: $scope.attendance,
      date: new Date($scope.attendanceStatus.date).toDateString(),
    };
    console.log(data);

    $http({
      method: "POST",
      url: "/dashboard/student/bulk/attendance/",
      data: data,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "subject Teacher registered successfully!";
        $scope.errorMessage = null;
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during registration!";
        $scope.successMessage = null;
      }
    );
  };

  $scope.submitMarksEntry = function () {
    var data = {
      marks: $scope.marks,
      subject: $scope.selectedSubjectForMarks,
      exam_type: $scope.selectedExamType,
      session_id: $scope.selectedExamSession,
    };

    console.log(data);

    $http({
      method: "POST",
      url: "/dashboard/internal/exam/marks/update/",
      data: data,
    }).then(
      function successCallback(response) {
        $scope.successMessage = "Internal Marks updated successfully!";
        $scope.errorMessage = null;
      },
      function errorCallback(response) {
        $scope.errorMessage = "Error occurred during marks update!";
        $scope.successMessage = null;
      }
    );
  };

  $scope.fetchBatchSemester = function () {
    $http({
      method: "GET",
      url: "/dashboard/batch/semester/lists/",
    }).then(
      function successCallback(response) {
        $scope.batchSemesterList = response.data;
        console.log($scope.batchSemesterList);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchExamTypes = function () {
    $http({
      method: "GET",
      url: "/dashboard/exam/types/",
    }).then(
      function successCallback(response) {
        $scope.examTypes = response.data;
        console.log($scope.examTypes);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchExamSession = function () {
    $http({
      method: "GET",
      url: "/dashboard/exam/session/",
    }).then(
      function successCallback(response) {
        $scope.examSession = response.data;
        console.log($scope.examSession);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchBatchSemester();
  $scope.fetchExamTypes();
  $scope.fetchExamSession();
});

// teacher dashboard controller
app.controller("studentDashboardController", function ($scope, $http) {
  $scope.showAttendance = false;
  $scope.showMarks = false;
  $scope.showBatchNotice = false;

  $scope.attendaceRecord = null;
  $scope.internalExamRecord = null;
  $scope.batchNotices = null;

  $scope.handleAttendanceView = function () {
    $scope.showAttendance = true;
    $scope.showMarks = false;
    $scope.showBatchNotice = false;
  };

  $scope.handleMarksView = function () {
    $scope.showAttendance = false;
    $scope.showMarks = true;
    $scope.showBatchNotice = false;
  };
  $scope.handleBatchNoticeView = function () {
    $scope.showAttendance = false;
    $scope.showMarks = false;
    $scope.showBatchNotice = true;
  };

  $scope.fetchAttendance = function () {
    $http({
      method: "GET",
      url: "/dashboard/student/current/attendance/record/",
    }).then(
      function successCallback(response) {
        $scope.attendaceRecord = response.data;
        console.log($scope.attendaceRecord);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchInternalExamRecord = function () {
    $http({
      method: "GET",
      url: "/dashboard/student/internal/exam/record/",
    }).then(
      function successCallback(response) {
        $scope.internalExamRecord = response.data;
        console.log($scope.internalExamRecord);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.fetchStudentNotices = function () {
    $http({
      method: "GET",
      url: "/dashboard/student/notice/list/",
    }).then(
      function successCallback(response) {
        $scope.batchNotices = response.data;
        console.log($scope.batchNotices);
      },
      function errorCallback(response) {
        console.log(response);
      }
    );
  };

  $scope.presentCount = function (records) {
    return records.filter(function (record) {
      return record.status === true; // Count where status is 'Present'
    }).length;
  };

  $scope.absentCount = function (records) {
    return records.filter(function (record) {
      return record.status === false; // Count where status is 'Absent'
    }).length;
  };

  $scope.fetchAttendance();
  $scope.fetchInternalExamRecord();
  $scope.fetchStudentNotices();
});
