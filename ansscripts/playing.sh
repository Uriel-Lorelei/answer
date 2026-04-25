#!/usr/bin/env bash

while [[ $# -gt 0 ]]; do
  case $1 in
    -f|--flag)
      if [[ "$2" == "name" ]]; then
        playerctl metadata --format "{{title}}"
      elif [[ "$2" == "image" ]]; then
        playerctl metadata --format "{{mpris:artUrl}}" | sed 's!file://!!'
      else
        echo "Use image or name after -f."
        exit 1
      fi
      shift 2
      ;;
    *)
      ehco "Unknown flag: $1."
      exit 1
      ;;
  esac
done     
          
    
