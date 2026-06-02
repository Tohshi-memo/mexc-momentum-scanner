# Decision Report

- generated_at: 2026-06-02T01:57:01.016136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5388**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.49% / filled 20/20。**
- 全期間 MARKET基準: n=5388, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+2.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.02% | **+3.02%** |
| MARKET | 20/20 | 100.0% | +2.49% | **+2.49%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.31% | **+1.16%** |
| LIMIT_1PCT | 13/20 | 65.0% | +0.85% | **+0.55%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.84% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.23% | **-0.12%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | -1.62% | **-0.97%** |

## 2. $100 Live Portfolio

- 残高: **$97.11** / 初期 $100.00 (-2.89%)
- 確定トレード: 83件 (TP 24 / SL 56 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.85** / 初期 $100.00 (+31.85%)
- 確定: 902件 (Win 209 / Loss 271 / Flat 422) / skip 1047件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $131.85

## 4. Latest Market Context

- 更新: 2026-06-02T01:56:58.556143+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.62% price=70823.1
- Funnel: target 776 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +49.52% | $9,807,567.06 |
| RIF/USDT:USDT | +16.70% | $1,007,538.54 |
| UB/USDT:USDT | +12.63% | $2,453,050.58 |
| WLD/USDT:USDT | +12.51% | $138,820,133.95 |
| SLX/USDT:USDT | +11.84% | $12,918,271.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +4.08% | +4.70% |
| BILL/USDT:USDT | below_1h_threshold | +3.30% | +3.92% |
| RIF/USDT:USDT | below_1h_threshold | +1.43% | +2.05% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +1.00% | +1.62% |
| NVIDIA/USDT:USDT | below_1h_threshold | +0.56% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
