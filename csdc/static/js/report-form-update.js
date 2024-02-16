const count = document.querySelectorAll(".dynamic-field").length - 1;

if (count < 5) {
  document.getElementById("dynamic-fieldss").innerHTML = `
      <input type="file" id="form-${count}-file" class="form-control" name="form-${count}-file" data-name="form-${count}-file" />`;
}

$(document).ready(function () {
  var buttonAdd = $("#add-button");
  var buttonRemove = $("#remove-button");
  var className = ".dynamic-field";
  var count = 0;
  var field = "";
  var maxFields = 5;

  function newFields() {
    return $(".newFields").length;
  }

  function totalFields() {
    return $(className).length;
  }

  function addNewField() {
    count = totalFields() + 1;
    field = $("#dynamic-fieldss").clone();
    field.attr("id", "dynamic-fieldss");
    field.children("input").attr("id", "form-" + (count - 1) + "-file");
    field.children("input").attr("data-name", "form-" + (count - 1) + "-file");
    field.children("input").attr("name", "form-" + (count - 1) + "-file");
    $(className + ":last").after($(field));
  }

  function removeLastField() {
    if (newFields() > 1) {
      $(className + ":last").remove();
    }
  }

  function enableButtonRemove() {
    if (newFields() === 2) {
      buttonRemove.removeAttr("disabled");
      buttonRemove.addClass("shadow-sm");
    }
  }

  function disableButtonRemove() {
    if (newFields() === 1) {
      buttonRemove.attr("disabled", "disabled");
      buttonRemove.removeClass("shadow-sm");
    }
  }

  function disableButtonAdd() {
    if (totalFields() >= maxFields) {
      buttonAdd.attr("disabled", "disabled");
      buttonAdd.removeClass("shadow-sm");
    }
  }

  function enableButtonAdd() {
    if (totalFields() === maxFields - 1) {
      buttonAdd.removeAttr("disabled");
      buttonAdd.addClass("shadow-sm");
    }
  }

  buttonAdd.click(function () {
    addNewField();
    enableButtonRemove();
    disableButtonAdd();
  });

  buttonRemove.click(function () {
    removeLastField();
    disableButtonRemove();
    enableButtonAdd();
  });

  disableButtonAdd();
});
