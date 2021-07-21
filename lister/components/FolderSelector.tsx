import { HTMLAttributes, useCallback, useState } from "react"

interface FolderSelectorProps extends HTMLAttributes<HTMLDivElement> {
  onListContent: (folderPath: string) => void
}

const FolderSelector = ({ onListContent }: FolderSelectorProps) => {
  const [folder, setFolder] = useState('')

  const onFolderChange = useCallback(e => {
    setFolder(e.target.value)
  }, [setFolder])

  return (
    <div>
      <div><label>Enter Folder path</label></div>
      <input type="text" onChange={onFolderChange} />
      <hr />
      <button onClick={() => onListContent(folder)}>List content</button>
    </div>
  )
}

export default FolderSelector
