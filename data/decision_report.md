# Decision Report

- generated_at: 2026-05-26T19:24:17.111915+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4907**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4907, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.11% | **+0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +5.45% | **+0.55%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.40% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +4.23% | **+3.38%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.78% | **+1.25%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.88% | **+0.84%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.86% | **+0.65%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.65% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$97.16** / 初期 $100.00 (-2.84%)
- 確定トレード: 65件 (TP 18 / SL 44 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.16
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.01** / 初期 $100.00 (+30.01%)
- 確定: 678件 (Win 172 / Loss 215 / Flat 291) / skip 790件
- 成長率目線: 平均log +0.000387 / 幾何平均 +0.039% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.61% 残高後 $130.01

## 4. Latest Market Context

- 更新: 2026-05-26T19:24:14.941286+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=75847.5
- Funnel: target 766 → liquid 139 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +6.46% | $7,360,832.23 |
| MUSTOCK/USDT:USDT | +4.47% | $17,670,651.72 |
| USELESS/USDT:USDT | +3.77% | $1,261,103.00 |
| AMDSTOCK/USDT:USDT | +3.46% | $2,025,790.13 |
| TONCOIN/USDT:USDT | +3.37% | $61,998,524.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.37% | +1.33% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.28% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.00% | +0.97% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.84% | +0.80% |
| UB/USDT:USDT | below_1h_threshold | +0.81% | +0.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
