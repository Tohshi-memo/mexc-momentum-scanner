# Decision Report

- generated_at: 2026-07-16T00:01:19.083216+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8775**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.41% / filled 20/20。**
- 全期間 MARKET基準: n=8775, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.41% | **+2.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.41% | **+2.41%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.43% | **+2.31%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.75% | **+1.40%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.92% | **+1.15%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +0.36% | **+0.20%** |
| LIMIT_BB3S_LONG | 9/9 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | -0.36% | **-0.09%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | -0.58% | **-0.15%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -2.62% | **-0.66%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$339.46** / 初期 $100.00 (+239.46%)
- 確定: 2892件 (Win 905 / Loss 942 / Flat 1045) / skip 2444件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ALLO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.01% 残高後 $339.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.85** / 初期 $100.00 (+6.85%)
- 確定: 739件 (Win 169 / Loss 168 / Flat 402) / skip 1447件
- 成長率目線: 平均log +0.000090 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1134 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EDGE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $106.85

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 183件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000366 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-16T00:01:11.641237+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64733.0
- Funnel: target 871 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +31.64% | $1,771,577.86 |
| ROAM/USDT:USDT | +17.58% | $5,588,867.00 |
| CAP/USDT:USDT | +14.03% | $1,650,927.66 |
| ONDO/USDT:USDT | +10.14% | $39,467,930.00 |
| LAB/USDT:USDT | +9.11% | $15,605,894.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.48% | +1.46% |
| HOME/USDT:USDT | below_1h_threshold | +0.94% | +0.93% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.91% | +0.89% |
| EWY/USDT:USDT | below_1h_threshold | +0.61% | +0.60% |
| ONDO/USDT:USDT | below_1h_threshold | +0.52% | +0.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
