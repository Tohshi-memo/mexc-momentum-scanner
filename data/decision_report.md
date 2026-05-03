# Decision Report

- generated_at: 2026-05-03T16:42:13.986587+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3087**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3087, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.05% | **+0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +2.13% | **+1.49%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_BB3S | 7/15 | 46.7% | +2.41% | **+1.12%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.41% | **+0.41%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.17% | **+1.59%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.20% | **+1.32%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.61% | **+1.31%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.47% | **+1.03%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.78% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T16:42:05.653413+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=78683.3
- Funnel: target 755 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +16.84% | $329,981,976.92 |
| SKYAI/USDT:USDT | +10.54% | $24,297,013.89 |
| AIOT/USDT:USDT | +5.53% | $2,305,793.08 |
| TAG/USDT:USDT | +2.74% | $10,306,913.84 |
| ASTEROID/USDT:USDT | +1.80% | $2,086,462.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAG/USDT:USDT | below_1h_threshold | +2.74% | +2.67% |
| UB/USDT:USDT | below_1h_threshold | +1.86% | +1.79% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.74% | +1.67% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.50% | +1.43% |
| TST/USDT:USDT | below_1h_threshold | +1.28% | +1.21% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
