import click
import sys
while True:
    ans = click.getchar()
    if(ans == 'a'):
        print ("you win")
    else:
        print ("loser")
