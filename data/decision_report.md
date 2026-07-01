# Decision Report

- generated_at: 2026-07-01T16:57:04.199937+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8002**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8002, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +6.91% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.47% | **+0.65%** |
| LIMIT_8PCT | 2/20 | 10.0% | +6.03% | **+0.60%** |
| LIMIT_7PCT | 3/20 | 15.0% | +0.67% | **+0.10%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -0.83% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +2.00% | **+0.80%** |
| MARKET_LONG | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.18% | **+0.59%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.76% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$268.04** / 初期 $100.00 (+168.04%)
- 確定: 2399件 (Win 731 / Loss 794 / Flat 874) / skip 2164件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: M/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $268.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.74** / 初期 $100.00 (+6.74%)
- 確定: 520件 (Win 131 / Loss 123 / Flat 266) / skip 893件
- 成長率目線: 平均log +0.000125 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0309 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: M/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $106.74

## 5. Latest Market Context

- 更新: 2026-07-01T16:56:59.468463+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=59843.1
- Funnel: target 825 → liquid 151 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +3.47% | $6,508,202.91 |
| BASED/USDT:USDT | +2.46% | $15,756,499.73 |
| TOWNS/USDT:USDT | +2.36% | $1,120,491.32 |
| RAVE/USDT:USDT | +2.26% | $6,640,565.76 |
| IN/USDT:USDT | +1.75% | $21,983,933.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +3.48% | +3.93% |
| BASED/USDT:USDT | below_1h_threshold | +2.47% | +2.92% |
| TOWNS/USDT:USDT | below_1h_threshold | +2.36% | +2.82% |
| RAVE/USDT:USDT | below_1h_threshold | +2.27% | +2.73% |
| IN/USDT:USDT | below_1h_threshold | +1.76% | +2.21% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
