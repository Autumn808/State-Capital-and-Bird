"""
//Autumn Capasso
//UMUC SDEV 300
//March 28th 2020
//Python State Capital and Bird List Application
//Week 3, Lab 3
//
"""
# Importing system for system exit method
import sys


def main():
    """ Python State Capital and Bird List Application"""

    # Initialize Selection Value
    selection = -1
    while selection:
        # Menu Display
        print('Welcome to the State Capital and Bird Application')
        print('Please choose from the following selections')
        print('1. Display State Capitals and Birds')
        print('2. Search for a specific state and Bird')
        print('3. Update a Bird for a specific state ')
        print('4. Exit Program')

        # Program takes in selection input
        print('Please enter Selection: ')

        # Conditional statement that creates menu choices
        selection = int(input())

        if selection == 1:
            display_sorted_states()

        if selection == 2:
            search_states()

        if selection == 3:
            update_state_bird()

        if selection == 4:
            end_program()

        else:
            invalid()


def display_sorted_states():
    """Display sorted States Name, Capital and State Flower"""
    state_sorted()


def state_sorted():
    """Sorts state list"""
    for state_name in state_list.keys():
        print("State name:", state_name,
              "\n Capital:", state_list[state_name]['Capital'],
              "\n Bird:", state_list[state_name]['State Bird'])


def search_states():
    """Searches dictionary for the states bird"""
    search_input = str(input('Enter what your searching for: '))
    if search_input in state_list.keys():
        print('State name:', search_input,
              "\n Capital:", state_list[search_input]['Capital'],
              "\n Bird:", state_list[search_input]['State Bird'])
    else:
        print ('Invalid entry ')


def update_state_bird():
    """this function updates the state bird """
    search_input = input('Enter the state to update:')
    if search_input in state_list.keys():
        new_bird = input('Enter Bird name: ')
        state_list[search_input]['State Bird'] = new_bird
        print("State name:", search_input,
              "\n Bird:", state_list[search_input]['State Bird'],
              "\n Has now been updated")
    else:
        print('you entered: ', search_input, invalid())


def invalid():
    """Prints invalid selection when the input doesnt fit the limitations """
    print ('You have entered an invalid selection ')


# Exit Function
def end_program():
    """ Will end program """
    sys.exit()


state_list = {"Alabama": {'Capital': "Montgomery",
                          'State Bird': "Yellowhammer"
                          },
              "Alaska": {'Capital': "Juneau",
                         'State Bird': "Willow Ptarmigan"
                         },
              "Arizona": {'Capital': "Phoenix",
                          'State Bird': "Cactus Wren"
                          },
              "Arkansas": {'Capital': "Little Rock",
                           'State Bird': "Mockingbird"
                           },
              "California": {'Capital': "Sacramento",
                             'State Bird': "California Valley Quail"
                             },
              "Colorado": {'Capital': "Denver",
                           'State Bird': "Lark Bunting"
                           },
              "Connecticut": {'Capital': "Hartford",
                              'State Bird': "Robin"
                              },
              "Delaware": {'Capital': "Dover",
                           'State Bird': "Blue Hen"
                           },
              "Florida": {'Capital': "Tallahassee",
                          'State Bird': "Mockingbird"
                          },
              "Georgia": {'Capital': "Atlanta",
                          'State Bird': " Brown Thrasher"
                          },
              "Hawaii": {'Capital': "Honolulu",
                         'State Bird': "Nene"
                         },
              "Idaho": {'Capital': "Boise",
                        'State Bird': "Mountain Bluebird"
                        },
              "Illinois": {'Capital': "Springfield",
                           'State Bird': "Cardinal"
                           },
              "Indiana": {'Capital': "Indianapolis",
                          'State Bird': "Cardinal"
                          },
              "Iowa": {'Capital': "Des Moines",
                       'State Bird': "Eastern Goldfinch"
                       },
              "Kansas": {'Capital': "Topeka",
                         'State Bird': "Western Meadowlark"
                         },
              "Kentucky": {'Capital': "Frankfort",
                           'State Bird': "Cardinal"
                           },
              "Louisiana": {'Capital': "Baton Rouge",
                            'State Bird': "Eastern Brown Pelican"
                            },
              "Maine": {'Capital': "Augusta",
                        'State Bird': "Chickadee"
                        },
              "Maryland": {'Capital': "Annapolis",
                           'State Bird': " Baltimore Oriole"
                           },
              "Massachusetts": {'Capital': "Boston",
                                'State Bird': "Chickadee"
                                },
              "Michigan": {'Capital': "Lansing",
                           'State Bird': "Robin"
                           },
              "Minnesota": {'Capital': "Saint Paul",
                            'State Bird': "Common Loon"
                            },

              "Mississippi": {'Capital': "Jackson",
                              'State Bird': "Mockingbird"
                              },
              "Missouri": {'Capital': "Jefferson City",
                           'State Bird': "Bluebird"
                           },
              "Montana": {'Capital': "Helena",
                          'State Bird': "Western Meadowlark"
                          },
              "Nebraska": {'Capital': "Lincoln",
                           'State Bird': "Western Meadowlark"
                           },
              "Nevada": {'Capital': "Carson City",
                         'State Bird': "Mountain Bluebird"
                         },
              "New Hampshire": {'Capital': "Concord",
                                'State Bird': "Purple Finch"
                                },
              "New Jersey": {'Capital': "Trenton",
                             'State Bird': "Eastern Goldfinch"
                             },
              "New Mexico": {'Capital': "Santa Fe",
                             'State Bird': "Roadrunner"
                             },
              "New York": {'Capital': "Albany",
                           'State Bird': "Bluebird"
                           },
              "North Carolina": {'Capital': "Raleigh",
                                 'State Bird': "Cardinal"
                                 },
              "Ohio": {'Capital': "Columbus",
                       'State Bird': "Cardinal"
                       },
              "Oklahoma": {'Capital': " Oklahoma City",
                           'State Bird': "Scissor-Tailed Flycatcher"
                           },
              "Oregon": {'Capital': "Salem",
                         'State Bird': "Western Meadowlark"
                         },
              "Pennsylvania": {'Capital': "Harrisburg",
                               'State Bird': "Ruffed Grouse"
                               },
              "Rhode Island": {'Capital': "Providence",
                               'State Bird': "Rhode Island Red"
                               },
              "South Carolina": {'Capital': "Columbia",
                                 'State Bird': "Great Carolina Wren"
                                 },
              "North Dakota": {'Capital': "Bismarck",
                               'State Bird': "Western Meadowlark"
                               },
              "South Dakota": {'Capital': "Pierre",
                               'State Bird': "Ring-Necked Pheasant"
                               },
              "Tennessee": {'Capital': "Nashville",
                            'State Bird': "Mockingbird"
                            },
              "Texas": {'Capital': "Austin",
                        'State Bird': "Mockingbird"
                        },
              "Utah": {'Capital': "Salt Lake City",
                       'State Bird': "California Seagull"
                       },
              "Vermont": {'Capital': "Montpelier",
                          'State Bird': "Hermit Thrush"
                          },
              "Virginia": {'Capital': "Richmond",
                           'State Bird': "Cardinal"
                           },
              "Washington": {'Capital': "Olympia",
                             'State Bird': "Willow Goldfinch"
                             },
              "West Virginia": {'Capital': "Charleston",
                                'State Bird': "Cardinal"
                                },
              "Wisconsin": {'Capital': "Madison",
                            'State Bird': "Robin"
                            },
              "Wyoming": {'Capital': "Cheyenne",
                          'State Bird': "Western Meadowlark"
                          },
              }

if __name__ == '__main__':
    main()
