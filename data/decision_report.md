# Decision Report

- generated_at: 2026-06-14T00:44:03.928657+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6622**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=6622, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.38% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.57% | **+0.47%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.33% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.42% | **+0.71%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.52%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.83% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.55** / 初期 $100.00 (+68.55%)
- 確定: 1495件 (Win 402 / Loss 477 / Flat 616) / skip 1688件
- 成長率目線: 平均log +0.000349 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $168.55

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 33件 (Win 11 / Loss 11 / Flat 11) / skip 0件
- 成長率目線: 平均log -0.000393 / 幾何平均 -0.039% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0214 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T00:43:58.912985+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.14% price=64508.0
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +30.64% | $2,748,293.66 |
| H/USDT:USDT | +20.01% | $18,016,787.54 |
| RIF/USDT:USDT | +19.04% | $13,201,308.19 |
| MEGA/USDT:USDT | +15.65% | $3,295,127.26 |
| BTW/USDT:USDT | +11.65% | $1,827,698.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +2.78% | +2.64% |
| CHZ/USDT:USDT | below_1h_threshold | +2.69% | +2.55% |
| ALGO/USDT:USDT | below_1h_threshold | +2.68% | +2.54% |
| MEGA/USDT:USDT | below_1h_threshold | +2.67% | +2.53% |
| BSB/USDT:USDT | below_1h_threshold | +2.17% | +2.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
