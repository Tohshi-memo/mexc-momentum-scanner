# Decision Report

- generated_at: 2026-09-10T02:41:28.061611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14144**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14144, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.97% | **+1.09%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.70% | **+0.56%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +3.23% | **+2.91%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.52% | **+2.64%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.11% | **+1.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,048.01** / 初期 $100.00 (+948.01%)
- 確定: 5324件 (Win 1601 / Loss 1717 / Flat 2006) / skip 5381件
- 成長率目線: 平均log +0.000441 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,048.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$206.05** / 初期 $100.00 (+106.05%)
- 確定: 2738件 (Win 757 / Loss 641 / Flat 1340) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0774 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $206.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定: 2649件 (Win 781 / Loss 1011 / Flat 857) / pending 5件 / skip 2962件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000529 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $121.72

## 6. Latest Market Context

- 更新: 2026-09-10T02:41:14.867480+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=78162.8
- Funnel: target 1064 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.3 >= 65=1, 4h RSI 88.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VTHO/USDT:USDT | +47.43% | $1,679,434.10 |
| CATE/USDT:USDT | +30.47% | $2,882,521.05 |
| BTR/USDT:USDT | +23.35% | $2,543,728.51 |
| MINA/USDT:USDT | +3.56% | $1,339,292.63 |
| KAS/USDT:USDT | +3.51% | $4,117,003.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MINA/USDT:USDT | below_1h_threshold | +2.89% | +2.75% |
| INJ/USDT:USDT | below_1h_threshold | +2.04% | +1.91% |
| AERO/USDT:USDT | below_1h_threshold | +1.90% | +1.77% |
| AKE/USDT:USDT | below_1h_threshold | +1.77% | +1.64% |
| VET/USDT:USDT | below_1h_threshold | +1.63% | +1.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
