# Decision Report

- generated_at: 2026-05-14T13:18:15.109249+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4291**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4291, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=-0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.29% | **-0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_BB3S | 5/12 | 41.7% | +1.66% | **+0.69%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +1.53% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.51% | **+0.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.41% | **+0.33%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +3.28% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$120.37** / 初期 $100.00 (+20.37%)
- 確定: 347件 (Win 95 / Loss 125 / Flat 127) / skip 505件
- 成長率目線: 平均log +0.000534 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $120.37

## 4. Latest Market Context

- 更新: 2026-05-14T13:18:11.328510+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=79813.6
- Funnel: target 763 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +57.61% | $8,040,431.01 |
| TROLLSOL/USDT:USDT | +28.60% | $2,237,815.93 |
| UP/USDT:USDT | +26.70% | $1,748,531.91 |
| PLAY/USDT:USDT | +22.68% | $1,848,675.67 |
| CSCOSTOCK/USDT:USDT | +19.78% | $5,724,265.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.62% | +2.51% |
| IRYS/USDT:USDT | below_1h_threshold | +2.21% | +2.09% |
| TROLLSOL/USDT:USDT | below_1h_threshold | +2.11% | +1.99% |
| CSCOSTOCK/USDT:USDT | below_1h_threshold | +1.47% | +1.35% |
| UP/USDT:USDT | below_1h_threshold | +1.25% | +1.13% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
