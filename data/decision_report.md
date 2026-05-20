# Decision Report

- generated_at: 2026-05-20T20:59:04.323847+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4580**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4580, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -1.50% | **-0.60%** |
| LIMIT_9PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_10PCT | 6/20 | 30.0% | -2.00% | **-0.60%** |
| LIMIT_5PCT | 11/20 | 55.0% | -1.11% | **-0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +3.36% | **+2.14%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.12%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.02% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.11** / 初期 $100.00 (+25.11%)
- 確定: 539件 (Win 138 / Loss 179 / Flat 222) / skip 602件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $125.11

## 4. Latest Market Context

- 更新: 2026-05-20T20:59:01.696408+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=77689.1
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +35.05% | $28,302,477.30 |
| FIDA/USDT:USDT | +27.52% | $9,920,412.49 |
| NIL/USDT:USDT | +20.97% | $2,439,491.40 |
| JTO/USDT:USDT | +15.07% | $2,031,709.77 |
| BEAT/USDT:USDT | +10.72% | $1,702,722.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +4.44% | +4.37% |
| NIL/USDT:USDT | below_1h_threshold | +3.60% | +3.53% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.01% | +1.93% |
| BEAT/USDT:USDT | below_1h_threshold | +1.89% | +1.81% |
| SPACE/USDT:USDT | below_1h_threshold | +1.61% | +1.53% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
