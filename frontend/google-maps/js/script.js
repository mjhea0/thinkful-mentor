// custom js

$(function() {

  $('map-canvas').hide()

  var employees = [
    {
      name: "David",
      phone: "800-555-5555",
      address: "123 Pleasant St, Morgantown, WV 26505"
    },
    {
      name: "Bob",
      phone: "303-123-4567",
      address: "1090 Ithica Dr, Boulder, CO 80305"
    }
  ];

  myApp();

  function myApp() {
    $('#employee_list').html(render_employee_table(employees));
    $('#add').click(function(){
      render_edit_box('add');
      $('#map-canvas').hide()
      $('#edit-box').slideDown();
    });
  };

  function terminate_employee(index){
    console.log(index);
    employees.splice(index, 1);
    render_employee_table(employees);
  };

  function render_edit_box(type, employee, index){

    var prename="";
    var prephone="";
    var preaddress="";

    if (type == "edit"){
      prename = employee.name;
      prephone = employee.phone;
      preaddress = employee.address;
    };

    var html = '<div><label>Name:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input id="edit_name" value="'
      + prename + '"></div><div><label>Phone:</label>&nbsp;&nbsp;&nbsp;&nbsp;<input id="edit_phone" value = "'
      + prephone + '"></div><div><label>Address:</label>&nbsp;<input id ="edit_address" value = "'
      + preaddress + '"</div><br><br>';

    var button_name = type ==  "add" ? "Add" : "Update";

    html += "<button id='saveit' class='btn btn-default btn-sm'>" + button_name + "</button>&nbsp;";
    html += "<button id='cancel' class='btn btn-default btn-sm'>Cancel</button>";

    $('#edit-box').html(html);

    $("#saveit").click(function(){
      var e = {
        name : $("#edit_name").val(),
        phone : $("#edit_phone").val(),
        address : $("#edit_address").val()
      };
      if (type == "edit"){
        update_employee(e, index);
      } else if (type == "add"){
        add_employee(e);
      }
      $('#edit-box').slideUp();
    })

    $("#cancel").click(function(){
      $('#edit-box').hide();
    })

  }

  function update_employee(employee, index){
    employees[index] = employee;
    render_employee_table(employees);
  }


  function add_employee(employee){
    employees.push(employee);
    var p = render_employee_table(employees);
    $('#employee_list').html(p);
  }

  function render_employee_table(data) {

    var html;
    html = "<table>"

    data.forEach(function(e, index){

      html += "<tr>";
      html += "<td>" + e.name + "</td>";
      html += "<td>" + e.phone + "</td>";
      html += "<td>" + e.address + "</td>";
      html += "<td><button class='delete btn btn-default btn-sm' index ='"+index+"'>Del</button></td>";
      html += "<td><button class='edit btn btn-default btn-sm' index ='"+index+"'>Edit</button></td>";
      html += "<td><button class='location btn btn-default btn-sm' index ='"+index+"'>Find Location</button></td>";
      html += "</tr>";
    })

    html += "</table>";

    $('#employee_list').html(html);

    $('.delete').click(function(){
      console.log('delete clicked');
      terminate_employee($(this).attr("index"));
    });

    $('.edit').click(function(){
      console.log('edit clicked');
      $('#edit-box').slideDown();
      $('#map-canvas').hide()
      render_edit_box("edit", employees[$(this).attr("index")], $(this).attr("index"));
    })

  }

  // google maps
  $(".location").click(function(){

    address = employees[$(this).attr("index")].address
    $('#map-canvas').show()
    $('#edit-box').hide();
    $.getJSON('http://maps.googleapis.com/maps/api/geocode/json?address='+address+'&sensor=false', null, function (data) {
      var p = data.results[0].geometry.location
      var map;
      var myOptions = {
        zoom: 12,
        center: new google.maps.LatLng(p.lat, p.lng)
      };
      var map = new google.maps.Map(document.getElementById('map-canvas'), myOptions);
      var marker = new google.maps.Marker({
        position: new google.maps.LatLng(p.lat, p.lng),
        map: map,
        title: address
      });
    })

  })

});

