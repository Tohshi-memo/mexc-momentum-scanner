# Decision Report

- generated_at: 2026-05-14T17:03:26.301818+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4304**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4304, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.14% | **+0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.51% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.03% | **+1.03%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +3.40% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$96.24** / 初期 $100.00 (-3.76%)
- 確定トレード: 43件 (TP 10 / SL 30 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.24
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.45** / 初期 $100.00 (+19.45%)
- 確定: 358件 (Win 95 / Loss 128 / Flat 135) / skip 507件
- 成長率目線: 平均log +0.000496 / 幾何平均 +0.050% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $119.45

## 4. Latest Market Context

- 更新: 2026-05-14T17:03:22.802249+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=81943.1
- Funnel: target 763 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +10.60% | $1,953,728.03 |
| LAB/USDT:USDT | +10.32% | $120,914,738.12 |
| ONDSSTOCK/USDT:USDT | +6.72% | $1,180,483.26 |
| CRCLSTOCK/USDT:USDT | +6.33% | $2,571,763.98 |
| TROLLSOL/USDT:USDT | +6.07% | $2,283,828.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.76% | +3.63% |
| Q/USDT:USDT | below_1h_threshold | +3.12% | +3.00% |
| UP/USDT:USDT | below_1h_threshold | +1.69% | +1.56% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.42% | +1.29% |
| LAB/USDT:USDT | below_1h_threshold | +1.36% | +1.23% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
