# Decision Report

- generated_at: 2026-07-18T01:56:27.102136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8909**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=8909, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 10/20 | 50.0% | +1.84% | **+0.92%** |
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.73% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.19% | **+1.28%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.23% | **+0.99%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.41% | **+0.99%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.05% | **+0.89%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.48% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$363.90** / 初期 $100.00 (+263.90%)
- 確定: 3024件 (Win 939 / Loss 961 / Flat 1124) / skip 2446件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $363.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.66** / 初期 $100.00 (+11.66%)
- 確定: 871件 (Win 205 / Loss 177 / Flat 489) / skip 1449件
- 成長率目線: 平均log +0.000127 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0083 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $111.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.30** / 初期 $100.00 (-0.70%)
- 確定: 167件 (Win 52 / Loss 88 / Flat 27) / pending 5件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $99.30

## 6. Latest Market Context

- 更新: 2026-07-18T01:56:16.169298+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=63955.9
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 73.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +53.16% | $11,505,480.77 |
| AKE/USDT:USDT | +20.61% | $47,947,962.81 |
| BANK/USDT:USDT | +16.56% | $22,077,367.79 |
| TRADOOR/USDT:USDT | +13.27% | $1,038,727.12 |
| SYN/USDT:USDT | +9.71% | $5,715,690.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +4.79% | +4.67% |
| T/USDT:USDT | below_1h_threshold | +4.76% | +4.64% |
| AKE/USDT:USDT | below_1h_threshold | +4.29% | +4.17% |
| ONDO/USDT:USDT | below_1h_threshold | +2.17% | +2.05% |
| JUP/USDT:USDT | below_1h_threshold | +1.85% | +1.73% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
