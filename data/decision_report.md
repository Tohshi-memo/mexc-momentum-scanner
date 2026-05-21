# Decision Report

- generated_at: 2026-05-21T00:18:45.401406+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4586**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4586, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_6PCT | 8/20 | 40.0% | -1.03% | **-0.41%** |
| LIMIT_5PCT | 9/20 | 45.0% | -1.02% | **-0.46%** |
| LIMIT_7PCT | 7/20 | 35.0% | -1.31% | **-0.46%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -1.39% | **-0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.30% | **+2.89%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +3.26% | **+2.12%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.02** / 初期 $100.00 (+22.02%)
- 確定: 544件 (Win 138 / Loss 184 / Flat 222) / skip 603件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIL/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $122.02

## 4. Latest Market Context

- 更新: 2026-05-21T00:18:42.569072+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77605.5
- Funnel: target 759 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +40.34% | $27,959,223.48 |
| NIL/USDT:USDT | +25.70% | $2,990,437.30 |
| FIDA/USDT:USDT | +16.44% | $11,610,754.56 |
| BEAT/USDT:USDT | +14.12% | $1,968,672.91 |
| JTO/USDT:USDT | +10.67% | $2,785,496.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.91% | +3.79% |
| BEAT/USDT:USDT | below_1h_threshold | +3.17% | +3.04% |
| XMR/USDT:USDT | below_1h_threshold | +1.39% | +1.26% |
| EDEN/USDT:USDT | below_1h_threshold | +1.24% | +1.12% |
| SPACE/USDT:USDT | below_1h_threshold | +1.14% | +1.02% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
