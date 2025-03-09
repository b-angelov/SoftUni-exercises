import {getDate} from "./time.js";

function searchFilter(data, name, search) {
  return data.filter((item) => {
    item = item[name] || [
      item.firstName,
      item.lastName,
      item.email,
      item.phoneNumber,
      getDate(item.createdAt),
    ].join(" ");
    return item.toLowerCase().includes(search.toLowerCase());
  });
}

function sortFilter(data, name, sort) {
  return data.sort((a, b) => {
    a = a[name] || "";
    b = b[name] || "";
    if(!a && !b)return 0;
    if(!a)return 1;
    if(!b)return -1;
    if (sort === "asc") {
      return a.localeCompare(b);
    } else {
      return b.localeCompare(a);
    }
  });
}

function paginationFilter(data, page, limit, currentItemFunc, itemsCountFunc, totalPagesFunc) {
  const totalPages = Math.ceil(data.length / limit)
  const item = (page - 1) * limit
  console.log(item, item + limit)
  currentItemFunc(item)
  itemsCountFunc(data.length)
  totalPagesFunc(totalPages)
  return data.slice(item, item + parseInt(limit));
}

export { searchFilter, sortFilter, paginationFilter };