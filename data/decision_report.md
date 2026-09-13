# Decision Report

- generated_at: 2026-09-13T13:51:52.584875+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14438**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.40% / filled 20/20。**
- 全期間 MARKET基準: n=14438, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 15/20 | 75.0% | +2.42% | **+1.81%** |
| MARKET | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_2PCT | 17/20 | 85.0% | +1.19% | **+1.02%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.53% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.85% | **+0.25%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.23% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5432件 (Win 1635 / Loss 1760 / Flat 2037) / skip 5567件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$228.27** / 初期 $100.00 (+128.27%)
- 確定: 2956件 (Win 822 / Loss 704 / Flat 1430) / skip 4893件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0687 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $228.27

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.94** / 初期 $100.00 (+26.94%)
- 確定: 2855件 (Win 850 / Loss 1104 / Flat 901) / pending 1件 / skip 3056件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000319 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UP/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.94

## 6. Latest Market Context

- 更新: 2026-09-13T13:51:39.329526+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=76800.1
- Funnel: target 1068 → liquid 133 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +270.07% | $105,640,114.42 |
| CVC/USDT:USDT | +73.23% | $2,310,605.99 |
| STEEM/USDT:USDT | +42.37% | $2,361,786.61 |
| ARK/USDT:USDT | +32.61% | $2,485,296.63 |
| VTHO/USDT:USDT | +24.82% | $3,431,358.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_relative_strength | +5.08% | +4.98% |
| AR/USDT:USDT | below_1h_threshold | +3.33% | +3.23% |
| LSK/USDT:USDT | below_1h_threshold | +3.23% | +3.13% |
| VTHO/USDT:USDT | below_1h_threshold | +2.66% | +2.56% |
| STEEM/USDT:USDT | below_1h_threshold | +2.21% | +2.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
