# Decision Report

- generated_at: 2026-06-14T00:50:23.405514+00:00
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

- 更新: 2026-06-14T00:50:18.922687+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64526.1
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +29.42% | $2,808,503.84 |
| H/USDT:USDT | +21.00% | $18,175,364.51 |
| MEGA/USDT:USDT | +19.50% | $3,324,260.64 |
| RIF/USDT:USDT | +19.42% | $13,225,155.57 |
| BTW/USDT:USDT | +13.64% | $1,881,840.61 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.46% | +4.29% |
| ALGO/USDT:USDT | below_1h_threshold | +2.57% | +2.40% |
| JCT/USDT:USDT | below_1h_threshold | +2.56% | +2.40% |
| CHZ/USDT:USDT | below_1h_threshold | +2.30% | +2.13% |
| BRETT/USDT:USDT | below_1h_threshold | +2.18% | +2.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
