# Decision Report

- generated_at: 2026-05-30T03:14:44.594133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5098**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5098, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-1.89%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.89% | **-1.89%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +7.43% | **+2.23%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_BB3S | 2/18 | 11.1% | +2.17% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.54% | **+2.54%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.76% | **+1.93%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.57% | **+1.54%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.13% | **+1.41%** |
| LIMIT_6PCT_LONG | 4/20 | 20.0% | +6.19% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.48** / 初期 $100.00 (+26.48%)
- 確定: 756件 (Win 176 / Loss 226 / Flat 354) / skip 903件
- 成長率目線: 平均log +0.000311 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $126.48

## 4. Latest Market Context

- 更新: 2026-05-30T03:14:41.511822+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=73732.3
- Funnel: target 773 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +54.95% | $10,965,195.82 |
| XLM/USDT:USDT | +33.57% | $449,231,990.67 |
| LAB/USDT:USDT | +25.41% | $135,210,381.32 |
| OL/USDT:USDT | +20.53% | $1,534,737.24 |
| BASED/USDT:USDT | +18.49% | $2,544,353.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.72% | +3.75% |
| CLO/USDT:USDT | below_1h_threshold | +1.30% | +1.32% |
| BAT/USDT:USDT | below_1h_threshold | +0.92% | +0.94% |
| BEAT/USDT:USDT | below_1h_threshold | +0.76% | +0.78% |
| OL/USDT:USDT | below_1h_threshold | +0.58% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
