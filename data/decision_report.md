# Decision Report

- generated_at: 2026-09-10T01:16:23.317395+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14137**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14137, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.27% | **+1.14%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.24% | **+1.12%** |
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_5PCT | 7/20 | 35.0% | +2.26% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.31% | **+1.96%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.54% | **+1.46%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.09% | **+0.60%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.52% | **+0.28%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.81% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,029.83** / 初期 $100.00 (+929.83%)
- 確定: 5317件 (Win 1598 / Loss 1715 / Flat 2004) / skip 5381件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,029.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$203.61** / 初期 $100.00 (+103.61%)
- 確定: 2731件 (Win 754 / Loss 639 / Flat 1338) / skip 4817件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0720 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $203.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.00** / 初期 $100.00 (+21.00%)
- 確定: 2642件 (Win 778 / Loss 1009 / Flat 855) / pending 4件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000554 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SOCK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $121.00

## 6. Latest Market Context

- 更新: 2026-09-10T01:16:10.537704+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=78275.3
- Funnel: target 1064 → liquid 164 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +21.99% | $2,822,743.16 |
| SOCK/USDT:USDT | +15.52% | $1,094,466.43 |
| BTR/USDT:USDT | +13.45% | $2,227,220.36 |
| WAVES/USDT:USDT | +7.87% | $1,105,892.68 |
| MINA/USDT:USDT | +4.68% | $1,259,809.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +4.69% | +4.51% |
| VET/USDT:USDT | below_1h_threshold | +2.61% | +2.44% |
| CATE/USDT:USDT | below_1h_threshold | +2.25% | +2.08% |
| AKE/USDT:USDT | below_1h_threshold | +1.59% | +1.42% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
