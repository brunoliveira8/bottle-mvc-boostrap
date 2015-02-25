<p class = "lead">The open items are as follows:</p>
<table class ="table" border="1">
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}</td>
  %end
  </tr>
%end
</table>
%rebase layout/layout
