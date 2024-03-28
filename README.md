# 七並べ (Seven Card Game, Sevens)

This repository contains a Python implementation of the Seven Card game (七並べ or Sevens), a simple card game played with a standard 52-card deck.

The primary purpose of this code is to serve as a foundation for future improvements and refactoring. Potential enhancements include introducing classes for an object-oriented design or redesigning the codebase for functional programming principles. The main focus is on personal learning and growth as a developer.

## Game Rules

- The game is played with a standard 52-card deck (excluding Jokers).
- The objective is to be the first player to get rid of all the cards in your hand.
- The game starts with all players being dealt an equal number of cards.
- The players who have a 7 card place them in the center of the table. The player with the 7 of diamonds starts the game.
- Players take turns playing cards from their hand, following the suit and rank of the cards on the table.
- A card can be played if it is one rank higher or lower than the card at either end of the sequence on the table for the corresponding suit. (The only exception is a 7, which can be played even if the adjacent 6 and 8 are not yet on the table. For all other ranks, at least one of the adjacent cards must already be placed on the table to play them. This rule becomes particularly relevant when hands of defeated players are added to the table, as it may create new sequences and allow previously unplayable cards to be played.)
- If a player cannot play a card, they must pass their turn. A player may also strategically pass even if they have a playable card. However, the number of passes is limited to 3, and on the 4th pass, the player is forced to retire, and all their cards are placed in the appropriate positions on the field.
- The game continues until one player runs out of cards or there is only one player left, at which point that last player is declared the winner.

## How to Play

- Run the game by executing the Python script.
- Enter the name of the human player when prompted. If a name is provided, there will be one human player and two computer players. If no name is provided, all three players will be computer-controlled.
- The game will display the initial state of the table.
- On your turn, choose a card to play by entering its suit (S, H, D, C) and rank (A, 2-9, X, J, Q, K), where X represents the rank of 10. If you cannot play a card, press Enter to pass.
- The game will validate your move and update the table accordingly.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.
