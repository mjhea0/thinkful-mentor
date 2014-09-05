describe("makeEditable", function () {
  var scope, element, compiled, html;

  beforeEach(function(){
    module('myApp');
    module('make-editable-template.html');

    inject(function($rootScope, $compile){
      scope = $rootScope.$new();
      html = '<div make-editable>Content</div>';
      compiled = $compile(html);
      element = compiled(scope);
      scope.$digest();
    });
  });

  it("initial state has edit button text and is not editable", function () {
    expect(element.find('button').text()).toBe('edit');
    expect(element.find('.make-editable').attr('contenteditable')).toBe('false');
  });

  it("after toggleEdit() the button text is save and content is editable", function () {
    element.find('button').click();
    expect(element.find('button').text()).toBe('save');
    expect(element.find('.make-editable').attr('contenteditable')).toBe('true');
  });
});
