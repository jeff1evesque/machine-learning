### Simple clone

```bash
cd /[destination-directory]
sudo git clone https://[account]@github.com/[account]/machine-learning.git
cd machine-learning
git remote add upstream https://github.com/[account]/machine-learning.git
```

**Note:** `[destination-directory]` corresponds to the desired directory path,
 where the project repository resides.  `[account]` corresponds to the git
 username, where the repository is being cloned from.  If the original
 repository was forked, then use your git username, otherwise, use
 `jeff1evesque`.

### Commit hash

```bash
cd /[destination-directory]
sudo git clone https://[account]@github.com/[account]/machine-learning.git
cd machine-learning
git remote add upstream https://github.com/[account]/machine-learning.git
# stop vagrant
vagrant halt
# ensure diffs don't prevent checkout, then checkout hash
git checkout -- .
git checkout [hash]
```

**Note:** the hashes associated with a release, can be found under the
 corresponding tag value, on the [release](https://github.com/jeff1evesque/machine-learning/releases)
 page.

**Note:** `[destination-directory]` corresponds to the desired directory path,
 where the project repository resides.  `[account]` corresponds to the git
 username, where the repository is being cloned from.  If the original
 repository was forked, then use your git username, otherwise, use
 `jeff1evesque`.
