module.exports = function(module){
  try{
    if(module[0] in {".":1}){
      module = process.cwd() + module.substr(1);
    }
    return require(module);
  }catch(e){ }
  return null;
};
