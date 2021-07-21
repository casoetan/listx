import { HTMLAttributes } from "react"

interface FolderListerProps extends HTMLAttributes<HTMLDivElement> {
  folderList: any[]
}

const FolderLister = ({ folderList }: FolderListerProps) => {
  return (
    folderList.length ? <table className="table table-hover">
      <thead>
        <tr>
          <th>Name</th>
          <th>Size</th>
          <th>Last Modified</th>
          <th>Item Type</th>
        </tr>
      </thead>

      <tbody>
        {folderList && folderList.map((folder, index) => (
          <tr key={index}>
            <td>{folder.name}</td>
            <td>{folder.size}</td>
            <td>{folder.modified}</td>
            <td><i className={`fas ${folder.is_file ? 'fa-file-alt' : 'fa-folder-open'}`}></i></td>
          </tr>
        ))}
      </tbody>
    </table> : <div>No folders found</div>
  )
}

export default FolderLister
