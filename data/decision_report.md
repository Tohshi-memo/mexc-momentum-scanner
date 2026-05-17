# Decision Report

- generated_at: 2026-05-17T12:12:43.932793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4398**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4398, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.35% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.42% | **+0.34%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.25% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.10** / 初期 $100.00 (+18.10%)
- 確定: 396件 (Win 100 / Loss 137 / Flat 159) / skip 563件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.10

## 4. Latest Market Context

- 更新: 2026-05-17T12:12:41.790376+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78399.2
- Funnel: target 760 → liquid 116 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +46.98% | $10,231,104.57 |
| AIA/USDT:USDT | +26.18% | $13,888,310.78 |
| CGPT/USDT:USDT | +18.37% | $2,381,062.85 |
| KAIA/USDT:USDT | +12.93% | $1,711,384.47 |
| ASTEROID/USDT:USDT | +11.17% | $4,465,332.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +1.85% | +1.81% |
| BEAT/USDT:USDT | below_1h_threshold | +1.72% | +1.68% |
| BSB/USDT:USDT | below_1h_threshold | +1.47% | +1.44% |
| CHZ/USDT:USDT | below_1h_threshold | +1.19% | +1.15% |
| UP/USDT:USDT | below_1h_threshold | +0.76% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
