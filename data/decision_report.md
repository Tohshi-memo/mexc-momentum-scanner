# Decision Report

- generated_at: 2026-05-20T20:54:02.347041+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4579**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4579, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.00% | **-0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -1.07% | **-0.48%** |
| LIMIT_6PCT | 10/20 | 50.0% | -1.03% | **-0.52%** |
| LIMIT_7PCT | 9/20 | 45.0% | -1.15% | **-0.52%** |
| LIMIT_5PCT | 12/20 | 60.0% | -0.94% | **-0.56%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.72% | **+2.32%** |
| LIMIT_BB3S_LONG | 7/12 | 58.3% | +3.36% | **+1.96%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.49% | **+1.92%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |

## 2. $100 Live Portfolio

- 残高: **$96.69** / 初期 $100.00 (-3.31%)
- 確定トレード: 57件 (TP 15 / SL 39 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.69
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.11** / 初期 $100.00 (+25.11%)
- 確定: 539件 (Win 138 / Loss 179 / Flat 222) / skip 601件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $125.11

## 4. Latest Market Context

- 更新: 2026-05-20T20:53:59.611390+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=77679.0
- Funnel: target 759 → liquid 127 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.2 >= 65=1, 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +36.94% | $28,213,310.53 |
| FIDA/USDT:USDT | +25.08% | $9,860,870.94 |
| NIL/USDT:USDT | +23.03% | $2,379,393.17 |
| JTO/USDT:USDT | +14.20% | $2,005,057.30 |
| BEAT/USDT:USDT | +10.95% | $1,685,469.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIDA/USDT:USDT | below_1h_threshold | +2.53% | +2.46% |
| BEAT/USDT:USDT | below_1h_threshold | +2.08% | +2.01% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.01% | +1.95% |
| SPACE/USDT:USDT | below_1h_threshold | +1.78% | +1.72% |
| TIA/USDT:USDT | below_1h_threshold | +1.26% | +1.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
