# Decision Report

- generated_at: 2026-06-26T04:33:42.125423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7604**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7604, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.78% | **-1.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.60% | **+0.06%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.44% | **+2.93%** |
| MARKET_LONG | 20/20 | 100.0% | +2.20% | **+2.20%** |
| ASK_LONG | 20/20 | 100.0% | +2.10% | **+2.10%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.22% | **+1.93%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.92% | **+1.61%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$220.62** / 初期 $100.00 (+120.62%)
- 確定: 2134件 (Win 630 / Loss 715 / Flat 789) / skip 2031件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: G/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $220.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.60** / 初期 $100.00 (+7.60%)
- 確定: 380件 (Win 103 / Loss 100 / Flat 177) / skip 635件
- 成長率目線: 平均log +0.000193 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $107.60

## 5. Latest Market Context

- 更新: 2026-06-26T04:33:34.833888+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=59890.0
- Funnel: target 810 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +34.57% | $2,727,578.26 |
| G/USDT:USDT | +28.34% | $5,132,091.77 |
| BEAT/USDT:USDT | +19.14% | $37,844,883.43 |
| IP/USDT:USDT | +16.12% | $5,765,872.22 |
| ARX/USDT:USDT | +16.04% | $2,156,966.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +1.74% | +1.95% |
| PIPPIN/USDT:USDT | below_1h_threshold | +1.22% | +1.44% |
| AAVE/USDT:USDT | below_1h_threshold | +0.97% | +1.18% |
| JTO/USDT:USDT | below_1h_threshold | +0.91% | +1.12% |
| XMR/USDT:USDT | below_1h_threshold | +0.87% | +1.08% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
