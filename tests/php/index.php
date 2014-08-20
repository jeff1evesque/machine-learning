
<!DOCTYPE html>
<?php
/**
 *  index.php: prompts users for 'training' / 'analysis' session, prompts users to provide an
 *             upload file / URL to XML dataset, and lastly provides attribute names to be used
 *             during SVM analysis.
 *
 *  @form:     sends form-data to 'logic_loader.py' using the 'post' method.
 *
 *  @datalist: an HTML5 tag that specifies a list of pre-defined options for an input element.
 *             However, is not supported in IE9-, or in Safari.  So, we add the 'select' element
 *             inside the 'datalist' element to provide a graceful degradation.
 *
 *  @input:    uses the 'list' attribute to refer to the datalist element which contains
 *             pre-defined options for the input element.
 */
?>
<html>
  <head>
  </head>
  <body>

    <form action="../../python/logic_loader.py" method="post">

      <input list='session_type' name='svm_session'>
      <datalist id='session_type'>
        <select name='session_type' required>
          <option value='training selected'>
          <option value='analysis'>
        </select>
      </datalist>
      <input type='submit'>

    </form>

  </body>
</html>
