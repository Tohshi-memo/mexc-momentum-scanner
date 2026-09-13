# Decision Report

- generated_at: 2026-09-13T10:11:28.513223+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14409**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.83% / filled 20/20。**
- 全期間 MARKET基準: n=14409, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.83%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.79% | **+1.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| MARKET | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_BB3S | 3/16 | 18.8% | +2.15% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.94% | **+1.07%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.57% | **+0.69%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.66% | **+0.59%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.34% | **+0.26%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5539件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$225.67** / 初期 $100.00 (+125.67%)
- 確定: 2927件 (Win 815 / Loss 695 / Flat 1417) / skip 4893件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1019 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $225.67

## 5. Causal Adaptive DryRun ($100)

- 残高: **$127.05** / 初期 $100.00 (+27.05%)
- 確定: 2852件 (Win 849 / Loss 1102 / Flat 901) / pending 4件 / skip 3030件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000288 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $127.05

## 6. Latest Market Context

- 更新: 2026-09-13T10:11:13.680272+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=76764.8
- Funnel: target 1068 → liquid 130 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.8 >= 65=1, 4h RSI 95.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +229.03% | $90,571,466.41 |
| STEEM/USDT:USDT | +63.94% | $1,497,690.39 |
| ARK/USDT:USDT | +38.30% | $1,335,603.80 |
| VTHO/USDT:USDT | +34.74% | $3,219,210.70 |
| POWR/USDT:USDT | +30.76% | $2,543,294.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KOMA/USDT:USDT | below_1h_threshold | +1.30% | +1.30% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.26% |
| POWR/USDT:USDT | below_1h_threshold | +1.15% | +1.16% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.03% | +1.03% |
| LONGXIA/USDT:USDT | below_1h_threshold | +0.86% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
