# Decision Report

- generated_at: 2026-09-12T22:56:23.881489+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14328**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.16% / filled 20/20。**
- 全期間 MARKET基準: n=14328, expectancy=-0.00%
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
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.25% | **+0.90%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.19% | **+0.53%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.56% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.63% | **+1.47%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +1.39% | **+1.11%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.75% | **+0.75%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.85% | **+0.59%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.63% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5429件 (Win 1635 / Loss 1760 / Flat 2034) / skip 5460件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STORJ/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$214.54** / 初期 $100.00 (+114.54%)
- 確定: 2846件 (Win 786 / Loss 660 / Flat 1400) / skip 4893件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1611 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $214.54

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.71** / 初期 $100.00 (+24.71%)
- 確定: 2779件 (Win 824 / Loss 1068 / Flat 887) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000475 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $124.71

## 6. Latest Market Context

- 更新: 2026-09-12T22:56:13.160731+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77202.6
- Funnel: target 1068 → liquid 124 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STORJ/USDT:USDT | +20.53% | $22,870,624.20 |
| LONGXIA/USDT:USDT | +16.60% | $9,852,250.63 |
| REZ/USDT:USDT | +14.20% | $2,025,174.13 |
| LSK/USDT:USDT | +12.72% | $48,369,061.45 |
| RIVER/USDT:USDT | +9.69% | $15,348,908.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRIFFAIN/USDT:USDT | below_1h_threshold | +4.28% | +4.31% |
| AKE/USDT:USDT | below_1h_threshold | +0.98% | +1.00% |
| IOST/USDT:USDT | below_1h_threshold | +0.71% | +0.74% |
| NIULAI/USDT:USDT | below_1h_threshold | +0.46% | +0.48% |
| BSV/USDT:USDT | below_1h_threshold | +0.43% | +0.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
