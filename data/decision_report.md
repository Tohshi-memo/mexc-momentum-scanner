# Decision Report

- generated_at: 2026-09-20T00:46:49.985360+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15115**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=15115, expectancy=-0.00%
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
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.04% | **+0.62%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.78% | **+0.74%** |
| MARKET_LONG | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | -0.22% | **-0.17%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,198.24** / 初期 $100.00 (+1098.24%)
- 確定: 5644件 (Win 1693 / Loss 1829 / Flat 2122) / skip 6032件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,198.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$244.93** / 初期 $100.00 (+144.93%)
- 確定: 3228件 (Win 895 / Loss 762 / Flat 1571) / skip 5298件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0234 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: G/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $244.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.58** / 初期 $100.00 (+21.58%)
- 確定: 2977件 (Win 880 / Loss 1178 / Flat 919) / pending 1件 / skip 3609件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.58

## 6. Latest Market Context

- 更新: 2026-09-20T00:46:36.366184+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=81268.5
- Funnel: target 1050 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.7 >= 65=1, 4h RSI 94.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +67.14% | $1,518,970.86 |
| OFC/USDT:USDT | +51.27% | $1,878,800.93 |
| ONE/USDT:USDT | +19.94% | $47,286,417.73 |
| EVAA/USDT:USDT | +15.50% | $1,362,574.31 |
| CATE/USDT:USDT | +14.11% | $1,299,368.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZIL/USDT:USDT | below_1h_threshold | +3.20% | +3.14% |
| INJ/USDT:USDT | below_1h_threshold | +3.02% | +2.96% |
| OFC/USDT:USDT | below_1h_threshold | +2.67% | +2.62% |
| ALGO/USDT:USDT | below_1h_threshold | +2.54% | +2.49% |
| XPL/USDT:USDT | below_1h_threshold | +2.30% | +2.24% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
