# Decision Report

- generated_at: 2026-11-13T06:16:26.223059+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18787**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=18787, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.11% | **+1.00%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.12% | **+0.95%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.56% | **+1.54%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.42% | **+1.28%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.74% | **+1.22%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.08% | **+1.02%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.41% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,745.98** / 初期 $100.00 (+1645.98%)
- 確定: 7257件 (Win 2091 / Loss 2324 / Flat 2842) / skip 8091件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.27% 残高後 $1,745.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$405.02** / 初期 $100.00 (+305.02%)
- 確定: 4806件 (Win 1296 / Loss 1065 / Flat 2445) / skip 7392件
- 成長率目線: 平均log +0.000291 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0645 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CBRSSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.18% 残高後 $405.02

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6946件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-13T06:16:10.596855+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=68354.2
- Funnel: target 1105 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BARD/USDT:USDT | +48.56% | $10,658,615.36 |
| KOR/USDT:USDT | +36.36% | $1,712,960.05 |
| ARIA/USDT:USDT | +36.34% | $9,362,370.38 |
| AKE/USDT:USDT | +29.37% | $8,438,374.70 |
| GANG/USDT:USDT | +12.31% | $1,175,374.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.17% | +1.82% |
| Q/USDT:USDT | below_1h_threshold | +2.12% | +1.76% |
| GANG/USDT:USDT | below_1h_threshold | +1.87% | +1.52% |
| PEPE/USDT:USDT | below_1h_threshold | +1.82% | +1.47% |
| H/USDT:USDT | below_1h_threshold | +1.78% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
