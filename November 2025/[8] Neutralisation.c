// https://www.codewars.com/kata/65128732b5aff40032a3d8f0/c

void neutralize (const char *s1, const char *s2, char *s3)
{
  int count;
  for (count = 0; s1[count] != '\0' || s2[count] != '\0'; count++) {
    if (s1[count] == '+' && s2[count] == '+') {
      s3[count] = '+';
    } else if (s1[count] == '-' && s2[count] == '-') {
      s3[count] = '-';
    } else {
      s3[count] = '0';
    }
  }
  s3[count] = '\0';
}
