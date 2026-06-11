# Decision Report

- generated_at: 2026-06-11T06:06:39.377037+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6313**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6313, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.36% | **-1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.62% | **+0.12%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.11% | **+1.47%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.81% | **+1.09%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1604件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T06:06:35.890696+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=62549.5
- Funnel: target 785 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +133.89% | $59,645,487.66 |
| AIO/USDT:USDT | +65.16% | $4,708,267.82 |
| BEAT/USDT:USDT | +50.29% | $210,606,161.11 |
| COLLECT/USDT:USDT | +37.21% | $1,461,776.36 |
| FIGHT/USDT:USDT | +25.79% | $1,269,802.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.40% | +4.45% |
| SKYAI/USDT:USDT | below_1h_threshold | +3.53% | +3.59% |
| STG/USDT:USDT | below_1h_threshold | +2.42% | +2.48% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.38% | +2.44% |
| COLLECT/USDT:USDT | below_1h_threshold | +1.38% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
