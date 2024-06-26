#!/usr/bin/env python
# coding: utf-8

# # Programming Set 3
# ## This assignment will develop your ability to manipulate data

# # Relationship Status (4/4)

# In[16]:


def relationship_status(from_member, to_member, social_graph):
    
    from_member = str(from_member)
    to_member = str(to_member)
    
    from_follows_to = to_member in social_graph.get(from_member).get('following')
    to_follows_from = from_member in social_graph.get(to_member).get('following')

    if from_follows_to and to_follows_from:
        return "friends"
    elif from_follows_to:
        return "follower"
    elif to_follows_from:
        return "followed by"
    else:
        return "no relationship"


# # Tic Tac Toe (4/4)

# In[ ]:


def tic_tac_toe(board):
    size = len(board)
    
    # rows
    for row in board:
        if all(symbol == row[0] and symbol != "" for symbol in row):
            return row[0]
    
    # columns
    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] != "" for row in range(size)):
            return board[0][col]
    
    # diagonal 1
    if all(board[i][i] == board[0][0] and board[i][i] != "" for i in range(size)):
        return board[0][0]
    
    # diagonal 2
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] != "" for i in range(size)):
        return board[0][size - 1]
    
    return "NO WINNER"


# # ETA (4/4)

# In[45]:


def eta(first_stop, second_stop, route_map):
    eta = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), data in route_map.items():
            if start == current_stop:
                eta += data['travel_time_mins']
                current_stop = end
                break
    return eta

