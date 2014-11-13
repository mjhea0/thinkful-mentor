var items = [
    {id: '0', name: 'Couch', description: 'A versatile couch.'},
    {id: '1', name: 'Calculator Watch', description: 'High-performance timepiece.'},
    {id: '2', name: 'FooBar', description: 'This is a test.'}
];
var _ = require('lodash');

function findOne(req) {
	return _.find(items, {id: req.params.id});
}


// list all
exports.list = function (req, res) {
	res.render('index', {items: items});
};

// show one
exports.show = function (req, res) {
	res.render('show', findOne(req));
};

// render new template, for adding new item
exports.new = function (req, res) {
	res.render('new');
};

// create new
exports.create = function (req, res) {
	var item =
	{
		id: _.uniqueId(),
		name: req.body.name,
		description: req.body.description
	};
    console.log(item) // sanity check
	items.push(item);
	res.redirect('/');
};

// edit
exports.edit = function (req, res) {
	res.render('edit', findOne(req));
};

exports.update = function (req, res) {
	var id = req.params.id;
	var index = _.findIndex(items, {id: id});
	var item =
	{
		id: id,
		name: req.body.name,
		description: req.body.description
	};

	items[index] = item;
	res.redirect('/' + id);
};

exports.delete = function (req, res) {
	_.remove(items, {id: req.params.id});
	res.json({success: true});
};