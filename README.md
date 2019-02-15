# Website for Network Theory Group

This repository hosts the website for [Network Theory Group](https://network-theory-group.github.io), which is based on [bibtex-js](https://github.com/pcooksey/bibtex-js).

## How to Update 

+ Adding a new "paper" belonging to existing categories: for example, adding a new paper to EEC
    + find/create the bib entry for the "paper"
    + add the following customized "key-value" pairs
      ```
      tag = {EEC},
      available = {https://dl.acm.org/citation.cfm?id=2591976},
      file = {folder/filename}
      ```
      Note that, the value of key "tag" is the category to which this paper belongs (**it is required**), and the value of key "available" is the URL from which we may access the FullText PDF of this paper, and the value of key "file" is where you store the FullText PDF (for internal use only).
 + Adding a new "paper" belonging to new categories: for example, adding a new paper to Coflow
    + Add the following HTML codes insides `<div class="sections tag"></div>` in [index.html](./index.html)
      ```html
            <div class="section coflow">
              <h2>Coflow</h2><hr/>
              <div class="sort year" extra="ASC number">
                <div class="templates"></div>
              </div>
            </div>
      ```
      Note that the class attributes (i.e., `"section coflow"`) for the top-level `div`: the first one (i.e., "section") is fixed, the following one is the category name (MUST be consistent with the bib entry's "tag" key). The contents wrapped inside the `<h2>` is the description for the category. You SHOULD not change the inner `div` unless you know what you are doing.
     + make the bib entry for this paper, which is the same as before.
     
     
  
  ## TODO
  
  + [ ] Add navigation
  + [X] Change the site to MVC style so that it is easier to maintain.
  
  

