# Decision Report

- generated_at: 2026-06-07T10:22:20.559516+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5944**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5944, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.79% | **-1.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +2.57% | **+0.90%** |
| LIMIT_BB3S | 9/19 | 47.4% | +1.88% | **+0.89%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.92% | **+0.67%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.67% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +2.12% | **+1.59%** |
| ASK_LONG | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.40% | **+1.20%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.75% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.49** / 初期 $100.00 (-0.51%)
- 確定トレード: 4件 (TP 1 / SL 3 / EXP 0)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.49
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$143.50** / 初期 $100.00 (+43.50%)
- 確定: 1061件 (Win 259 / Loss 324 / Flat 478) / skip 1444件
- 成長率目線: 平均log +0.000340 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.35% 残高後 $143.50

## 4. Latest Market Context

- 更新: 2026-06-07T10:22:17.294116+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=62400.0
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +59.24% | $7,078,397.87 |
| LAB/USDT:USDT | +40.34% | $62,947,324.80 |
| EDEN/USDT:USDT | +36.99% | $3,939,891.25 |
| BSB/USDT:USDT | +32.45% | $6,721,647.12 |
| BIANRENSHENG/USDT:USDT | +23.92% | $1,479,100.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +4.53% | +4.71% |
| VELVET/USDT:USDT | below_1h_threshold | +3.45% | +3.63% |
| FIDA/USDT:USDT | below_1h_threshold | +3.00% | +3.18% |
| BEAT/USDT:USDT | below_1h_threshold | +2.17% | +2.34% |
| BANK/USDT:USDT | below_1h_threshold | +2.07% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
