# Decision Report

- generated_at: 2026-05-14T16:53:49.136248+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4303**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4303, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.46% | **-0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.37% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.86% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.61** / 初期 $100.00 (+19.61%)
- 確定: 357件 (Win 95 / Loss 127 / Flat 135) / skip 507件
- 成長率目線: 平均log +0.000502 / 幾何平均 +0.050% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDSSTOCK/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.61

## 4. Latest Market Context

- 更新: 2026-05-14T16:53:42.560447+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=81128.3
- Funnel: target 763 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1, 4h RSI 82.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +9.11% | $129,195,516.09 |
| UP/USDT:USDT | +8.77% | $2,102,779.04 |
| ONDSSTOCK/USDT:USDT | +5.32% | $1,154,942.55 |
| TRIA/USDT:USDT | +4.18% | $1,944,490.05 |
| CRCLSTOCK/USDT:USDT | +3.78% | $2,633,405.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TRIA/USDT:USDT | below_1h_threshold | +4.36% | +4.51% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +3.79% | +3.94% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +3.39% | +3.53% |
| CFX/USDT:USDT | below_1h_threshold | +3.37% | +3.51% |
| ASTSSTOCK/USDT:USDT | below_1h_threshold | +3.35% | +3.50% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
