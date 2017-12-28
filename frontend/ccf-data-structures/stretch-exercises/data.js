var store1 = {
    '2015-01-06': [
        ['Dark Chocolate Crunchies', '4.39', 1],
        ['Mint Wafers', '1.19', 3],
        ['Peppermint Poppers', '2.48', 2],
        ['Peanut Butter Buttered Peanuts', '1.89', 6]
    ],
    '2015-01-07': [
        ['Dark Chocolate Crunchies', '4.39', 4],
        ['Berry Bites', '7.99', 3],
        ['Peppermint Poppers', '2.48', 1],
        ['Caramel Twists', '.60', 7]
    ],
    '2015-01-08': [
        ['Banana Bunches', '4.63', 1],
        ['Peppermint Poppers', '2.48', 3],
        ['Mint Wafers', '1.19', 7],
        ['Dark Chocolate Crunchies', '4.39', 2],
        ['Caramel Twists', '.60', 1]
    ],
    '2015-01-09': [
        ['Caramel Twists', '.60', 3],
        ['Peanut Butter Buttered Peanuts', '1.89', 2]
    ],
    '2015-01-10': [
        ['Peanut Butter Buttered Peanuts', '1.89', 7],
        ['Caramel Twists', '.60', 2],
        ['Berry Bites', '7.99', 3],
        ['Dark Chocolate Crunchies', '4.39', 8],
        ['Mint Wafers', '1.19', 2]
    ]
}

var store2 = {
    'inventory prices': {
        'Dark Chocolate Crunchies': 4.29,
        'Mint Wafers': 1.09,
        'Peppermint Poppers': 2.38,
        'Peanut Butter Buttered Peanuts': 1.79,
        'Berry Bites': 7.89,
        'Caramel Twists': .50,
        'Banana Bunches': 4.53
    },
    'sale dates': {
        'Dark Chocolate Crunchies': ['2015-01-06', '2015-01-06', '2015-01-06', '2015-01-08'],
        'Mint Wafers': ['2015-01-06', '2015-01-07', '2015-01-07', '2015-01-09'],
        'Peppermint Poppers': ['2015-01-08', '2015-01-08', '2015-01-09', '2015-01-09', '2015-01-10', '2015-01-10', '2015-01-10'],
        'Peanut Butter Buttered Peanuts': ['2015-01-07', '2015-01-07'],
        'Berry Bites': ['2015-01-06', '2015-01-09', '2015-01-09', '2015-01-09', '2015-01-10', '2015-01-10'],
        'Caramel Twists': ['2015-01-06', '2015-01-06', '2015-01-07', '2015-01-08', '2015-01-08', '2015-01-09', '2015-01-09', '2015-01-10', '2015-01-10', '2015-01-10'],
        'Banana Bunches': ['2015-01-10', '2015-01-10']
    }
}

var store3 = [{
    'date': '2015-01-06',
    'inventory sold': {
        'Dark Chocolate Crunchies': {
            'cost': 4.29,
            'quantity': 1
        },
        'Mint Wafers': {
            'cost': 1.09,
            'quantity': 0
        },
        'Peppermint Poppers': {
            'cost': 2.38,
            'quantity': 3
        },
        'Peanut Butter Buttered Peanuts': {
            'cost': 1.79,
            'quantity': 2
        },
        'Berry Bites': {
            'cost': 7.89,
            'quantity': 0
        },
        'Caramel Twists': {
            'cost': .50,
            'quantity': 0
        },
        'Banana Bunches': {
            'cost': 4.53,
            'quantity': 1
        }
    }
}, {
    'date': '2015-01-07',
    'inventory sold': {
        'Dark Chocolate Crunchies': {
            'cost': 4.29,
            'quantity': 0
        },
        'Mint Wafers': {
            'cost': 1.09,
            'quantity': 2
        },
        'Peppermint Poppers': {
            'cost': 2.38,
            'quantity': 1
        },
        'Peanut Butter Buttered Peanuts': {
            'cost': 1.79,
            'quantity': 0
        },
        'Berry Bites': {
            'cost': 7.89,
            'quantity': 3
        },
        'Caramel Twists': {
            'cost': .50,
            'quantity': 7
        },
        'Banana Bunches': {
            'cost': 4.53,
            'quantity': 1
        }
    }
}, {
    'date': '2015-01-08',
    'inventory sold': {
        'Dark Chocolate Crunchies': {
            'cost': 4.29,
            'quantity': 1
        },
        'Mint Wafers': {
            'cost': 1.09,
            'quantity': 1
        },
        'Peppermint Poppers': {
            'cost': 2.38,
            'quantity': 0
        },
        'Peanut Butter Buttered Peanuts': {
            'cost': 1.79,
            'quantity': 0
        },
        'Berry Bites': {
            'cost': 7.89,
            'quantity': 0
        },
        'Caramel Twists': {
            'cost': .50,
            'quantity': 2
        },
        'Banana Bunches': {
            'cost': 4.53,
            'quantity': 0
        }
    }
}, {
    'date': '2015-01-09',
    'inventory sold': {
        'Dark Chocolate Crunchies': {
            'cost': 4.29,
            'quantity': 0
        },
        'Mint Wafers': {
            'cost': 1.09,
            'quantity': 3
        },
        'Peppermint Poppers': {
            'cost': 2.38,
            'quantity': 2
        },
        'Peanut Butter Buttered Peanuts': {
            'cost': 1.79,
            'quantity': 1
        },
        'Berry Bites': {
            'cost': 7.89,
            'quantity': 0
        },
        'Caramel Twists': {
            'cost': .50,
            'quantity': 0
        },
        'Banana Bunches': {
            'cost': 4.53,
            'quantity': 1
        }
    }
}, {
    'date': '2015-01-10',
    'inventory sold': {
        'Dark Chocolate Crunchies': {
            'cost': 4.29,
            'quantity': 2
        },
        'Mint Wafers': {
            'cost': 1.09,
            'quantity': 1
        },
        'Peppermint Poppers': {
            'cost': 2.38,
            'quantity': 0
        },
        'Peanut Butter Buttered Peanuts': {
            'cost': 1.79,
            'quantity': 2
        },
        'Berry Bites': {
            'cost': 7.89,
            'quantity': 5
        },
        'Caramel Twists': {
            'cost': .50,
            'quantity': 7
        },
        'Banana Bunches': {
            'cost': 4.53,
            'quantity': 2
        }
    }
}]

var store4 = {
    'Dark Chocolate Crunchies': {
        'cost': 4.34,
        'sold on': ['2015-01-06', '2015-01-06', '2015-01-07', '2015-01-08', '2015-01-08']
    },
    'Mint Wafers': {
        'cost': 1.14,
        'sold on': ['2015-01-06', '2015-01-07', '2015-01-07', '2015-01-07', '2015-01-07', '2015-01-07', '2015-01-09', '2015-01-09', '2015-01-09', '2015-01-09']
    },
    'Peppermint Poppers': {
        'cost': 2.43,
        'sold on': ['2015-01-07', '2015-01-07', '2015-01-08', '2015-01-08', '2015-01-08', '2015-01-09', '2015-01-10', '2015-01-10']
    },
    'Peanut Butter Buttered Peanuts': {
        'cost': 1.84,
        'sold on': ['2015-01-06', '2015-01-06', '2015-01-08']
    },
    'Berry Bites': {
        'cost': 7.94,
        'sold on': ['2015-01-06', '2015-01-06', '2015-01-06', '2015-01-07', '2015-01-07', '2015-01-07', '2015-01-07', '2015-01-08', '2015-01-09', '2015-01-09', '2015-01-09', '2015-01-09', '2015-01-10', '2015-01-10', '2015-01-10', '2015-01-10']
    },
    'Caramel Twists': {
        'cost': .55,
        'sold on': ['2015-01-07', '2015-01-08', '2015-01-08', '2015-01-08', '2015-01-09', '2015-01-10']
    },
    'Banana Bunches': {
        'cost': 4.58,
        'sold on': ['2015-01-06', '2015-01-06', '2015-01-07', '2015-01-10']
    }
}

module.exports = {
    store1: store1,
    store2: store2,
    store3: store3,
    store4: store4
}