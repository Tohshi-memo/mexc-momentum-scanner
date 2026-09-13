# Decision Report

- generated_at: 2026-09-13T10:31:32.281623+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14416**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=14416, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.73% | **+0.66%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.28% | **+0.64%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.94% | **+0.28%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.21%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.84% | **+0.71%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.37% | **+0.67%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.15% | **+0.52%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5546件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$224.84** / 初期 $100.00 (+124.84%)
- 確定: 2934件 (Win 816 / Loss 698 / Flat 1420) / skip 4893件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0694 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_7PCT` TP_HIT account +0.69% 残高後 $224.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.83** / 初期 $100.00 (+26.83%)
- 確定: 2853件 (Win 849 / Loss 1103 / Flat 901) / pending 3件 / skip 3036件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.83

## 6. Latest Market Context

- 更新: 2026-09-13T10:31:19.263965+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=76729.9
- Funnel: target 1068 → liquid 131 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1, 4h RSI 95.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +311.69% | $93,946,057.87 |
| STEEM/USDT:USDT | +67.96% | $1,656,998.11 |
| ARK/USDT:USDT | +42.42% | $1,399,648.47 |
| VTHO/USDT:USDT | +36.50% | $3,242,385.86 |
| POWR/USDT:USDT | +32.07% | $2,591,849.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STORJ/USDT:USDT | below_1h_threshold | +3.98% | +4.03% |
| ARK/USDT:USDT | below_1h_threshold | +3.29% | +3.33% |
| THETA/USDT:USDT | below_1h_threshold | +2.89% | +2.94% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.29% | +2.33% |
| POWR/USDT:USDT | below_1h_threshold | +2.27% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
