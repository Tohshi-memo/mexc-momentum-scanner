# Decision Report

- generated_at: 2026-07-16T10:01:17.033252+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8797**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=8797, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.61% | **+0.43%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.17% | **+0.16%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.19% | **+0.83%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +0.32% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$106.87** / 初期 $100.00 (+6.87%)
- 確定トレード: 104件 (TP 38 / SL 64 / EXP 2)
- 最新: ROAM/USDT:USDT SL_HIT PnL -4.00% 残高後 $106.87
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$337.15** / 初期 $100.00 (+237.15%)
- 確定: 2912件 (Win 908 / Loss 945 / Flat 1059) / skip 2446件
- 成長率目線: 平均log +0.000417 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $337.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.12** / 初期 $100.00 (+7.12%)
- 確定: 759件 (Win 173 / Loss 169 / Flat 417) / skip 1449件
- 成長率目線: 平均log +0.000091 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0074 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $107.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.13** / 初期 $100.00 (-1.87%)
- 確定: 69件 (Win 20 / Loss 45 / Flat 4) / pending 1件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000453 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ROAM/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $98.13

## 6. Latest Market Context

- 更新: 2026-07-16T10:01:09.542329+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=64076.3
- Funnel: target 875 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +27.33% | $5,846,729.67 |
| US/USDT:USDT | +16.62% | $15,761,960.73 |
| CAP/USDT:USDT | +15.15% | $2,839,414.13 |
| BANK/USDT:USDT | +12.09% | $2,578,758.67 |
| ONDO/USDT:USDT | +11.82% | $73,538,140.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UNHSTOCK/USDT:USDT | below_1h_threshold | +4.77% | +4.75% |
| ROAM/USDT:USDT | below_1h_threshold | +2.51% | +2.49% |
| AKE/USDT:USDT | below_1h_threshold | +1.27% | +1.25% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.09% | +1.07% |
| BANK/USDT:USDT | below_1h_threshold | +0.61% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
