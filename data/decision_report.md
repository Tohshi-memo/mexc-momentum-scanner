# Decision Report

- generated_at: 2026-05-17T19:48:29.310324+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4418**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4418, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 4/13 | 30.8% | +1.50% | **+0.46%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.81% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.87% | **+1.86%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.61% | **+1.83%** |
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +3.01% | **+1.29%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.41% | **+1.20%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.05** / 初期 $100.00 (+21.05%)
- 確定: 415件 (Win 108 / Loss 140 / Flat 167) / skip 564件
- 成長率目線: 平均log +0.000460 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $121.05

## 4. Latest Market Context

- 更新: 2026-05-17T19:48:27.017031+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=78357.2
- Funnel: target 760 → liquid 123 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +16.75% | $2,233,209.27 |
| UB/USDT:USDT | +9.91% | $13,219,033.17 |
| BILL/USDT:USDT | +9.29% | $33,472,804.02 |
| HYPE/USDT:USDT | +6.65% | $243,710,271.00 |
| ASTEROID/USDT:USDT | +5.68% | $4,127,380.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENDLE/USDT:USDT | below_1h_threshold | +2.55% | +2.38% |
| TONCOIN/USDT:USDT | below_1h_threshold | +2.54% | +2.37% |
| VVV/USDT:USDT | below_1h_threshold | +2.46% | +2.29% |
| HYPE/USDT:USDT | below_1h_threshold | +2.20% | +2.03% |
| BILL/USDT:USDT | below_1h_threshold | +2.02% | +1.85% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
