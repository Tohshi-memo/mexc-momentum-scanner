# Decision Report

- generated_at: 2026-09-13T10:16:28.158744+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14411**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=14411, expectancy=-0.01%
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
| LIMIT_1PCT | 18/20 | 90.0% | +0.85% | **+0.76%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.33% | **+0.47%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.15% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.79% | **+0.81%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.37% | **+0.67%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.92% | **+0.50%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.44% | **+0.37%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.39% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5431件 (Win 1635 / Loss 1760 / Flat 2036) / skip 5541件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VTHO/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$224.88** / 初期 $100.00 (+124.88%)
- 確定: 2929件 (Win 815 / Loss 696 / Flat 1418) / skip 4893件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0652 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $224.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.83** / 初期 $100.00 (+26.83%)
- 確定: 2853件 (Win 849 / Loss 1103 / Flat 901) / pending 3件 / skip 3031件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $126.83

## 6. Latest Market Context

- 更新: 2026-09-13T10:16:13.554349+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=76765.2
- Funnel: target 1068 → liquid 131 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +277.26% | $91,464,882.88 |
| STEEM/USDT:USDT | +62.27% | $1,524,032.23 |
| ARK/USDT:USDT | +40.69% | $1,351,972.83 |
| VTHO/USDT:USDT | +35.82% | $3,224,091.36 |
| POWR/USDT:USDT | +29.87% | $2,569,118.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STEEM/USDT:USDT | below_1h_threshold | +3.68% | +3.68% |
| THETA/USDT:USDT | below_1h_threshold | +2.25% | +2.25% |
| ARK/USDT:USDT | below_1h_threshold | +2.15% | +2.15% |
| ABNBSTOCK/USDT:USDT | below_1h_threshold | +1.26% | +1.26% |
| KOMA/USDT:USDT | below_1h_threshold | +1.24% | +1.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
