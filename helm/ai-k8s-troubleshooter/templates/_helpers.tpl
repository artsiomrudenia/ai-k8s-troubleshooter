{{- define "ai-k8s-troubleshooter.fullname" -}}
{{- default "ai-k8s-troubleshooter" .Release.Name -}}
{{- end -}}
