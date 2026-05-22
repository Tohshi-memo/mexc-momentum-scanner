# Decision Report

- generated_at: 2026-05-22T07:38:53.115135+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4674**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=4674, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.97% | **+0.87%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.99% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/9 | 66.7% | +2.77% | **+1.85%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.12% | **+1.01%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.77% | **+0.54%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 548件 (Win 138 / Loss 185 / Flat 225) / skip 687件
- 成長率目線: 平均log +0.000354 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-22T07:38:50.599856+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77447.0
- Funnel: target 768 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1, 4h RSI 67.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +54.13% | $2,866,768.46 |
| NEAR/USDT:USDT | +24.08% | $78,197,385.56 |
| GRASS/USDT:USDT | +19.81% | $4,873,137.61 |
| OPG/USDT:USDT | +19.69% | $1,000,854.50 |
| PLUME/USDT:USDT | +13.10% | $1,854,256.60 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.79% | +2.71% |
| ARKM/USDT:USDT | below_1h_threshold | +2.23% | +2.15% |
| WLD/USDT:USDT | below_1h_threshold | +2.23% | +2.15% |
| NEAR/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |
| ICP/USDT:USDT | below_1h_threshold | +1.82% | +1.74% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
