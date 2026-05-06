{{- define "ai-service.name" -}}
{{- default .Chart.Name .Values.nameOverride -}}
{{- end -}}

{{- define "ai-service.fullname" -}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{- if hasPrefix $name .Release.Name -}}
{{- .Release.Name | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name $name | trimSuffix "-" -}}
{{- end -}}
{{- end -}}

{{- define "ai-service.selectorLabels" -}}
app.kubernetes.io/name: {{ include "ai-service.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
