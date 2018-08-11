#include <stdio.h>
#include <stdlib.h>
#include <errno.h>


void bytecheck(char* string1, char* string2)
{
  while (*string1 != '\0' && *string2!= '\0')
    {
      /*      if (*string2 == '\0')
	{ fprintf(stderr, "Error: %d.  'From' and 'to' are not the same length\n", errno);
	exit(1);	}*/
      string1++;
      string2++;
    }
  
  if (*string1!=*string2)
    {
      fprintf(stderr, "Error: %d.  'From' and 'to' are not the same length\n", errno);
      exit(1);
    }
}

void dupcheck(char* string)
{
  char* temp = string;
  while(*string != '\0')
    {
      char chara = *string;
      temp = string;
      while(*temp != '\0')
	{
	  temp++;
	  if (chara == *temp)
	    {
	      fprintf(stderr, "Error: %d.  'From' has duplicate bytes\n", errno);
	      exit(1);
	    }
	}
      string++;
    }
}

int main(int argc, char **argv[])
{

  char* string1 = (char*) argv[1];
  char* string2 = (char*) argv[2];
  char* temp1 = string1;
  char* temp2 = string2;

  
  bytecheck(string1, string2);
  dupcheck(string1);

  
  char c;
  while ((c=getchar())!=EOF)
    {
      string1 = temp1;
      string2 = temp2;
      while (*string1!='\0'){
	if (c== *string1){
	  c = *string2;
	  break;
	}
	string1++;
	string2++;

      }
      putchar(c);
      
    }
    
  //  printf("%s ", b);
  //  printf(argv[1]);
  // printf(argv[2]);

}
